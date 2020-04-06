import urllib
from bs4 import BeautifulSoup
import xlwt
import json
import re

i = 1

def parse(url, sheet):
    #body
    headers={'Accept': 'application/json, text/javascript', 
             'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
             #'cookie': 's_ViewType=10; _lxsdk_cuid=1714a6f6dc576-0351aabd617323-5463377a-a41c3-1714a6f6dc6c8; _lxsdk=1714a6f6dc576-0351aabd617323-5463377a-a41c3-1714a6f6dc6c8; _hc.v=9b3f5fce-2b77-d20f-1b3b-ebf7c793f66e.1586091755; wed_user_path=2786|0; aburl=1; cy=17; cye=xian; dplet=4a206248cf9cd97ea5b23332ab9c74c6; dper=017c7cde4689ccbe3b4e92a96c6e578e4d48e3d871c987831fb9f5436f0c11b16b545df35a4c190b74969ae455872e22b081eb71864dd6ce179556929ab51251f1f2a3a60191e17c2887ae86e185543122365cdcd5dc61d0347d49212cc710c4; ll=7fd06e815b796be3df069dec7836c3df; ua=%E7%82%AC%E7%81%8F; ctu=51082c643abca2e4a4729d35da419781a5baa93bd770d869eb48bf863a23f42c; _lxsdk_s=1714a6f6dc7-af0-f8f-b5a%7C%7C232'}
             'Cookie': '__mta=174477597.1586091888987.1586097193584.1586106048720.9; s_ViewType=10; _lxsdk_cuid=1714a6f6dc576-0351aabd617323-5463377a-a41c3-1714a6f6dc6c8; _lxsdk=1714a6f6dc576-0351aabd617323-5463377a-a41c3-1714a6f6dc6c8; _hc.v=9b3f5fce-2b77-d20f-1b3b-ebf7c793f66e.1586091755; aburl=1; cy=17; cye=xian; dplet=4a206248cf9cd97ea5b23332ab9c74c6; dper=017c7cde4689ccbe3b4e92a96c6e578e4d48e3d871c987831fb9f5436f0c11b16b545df35a4c190b74969ae455872e22b081eb71864dd6ce179556929ab51251f1f2a3a60191e17c2887ae86e185543122365cdcd5dc61d0347d49212cc710c4; ll=7fd06e815b796be3df069dec7836c3df; ua=%E7%82%AC%E7%81%8F; ctu=51082c643abca2e4a4729d35da419781a5baa93bd770d869eb48bf863a23f42c; wed_user_path=2786|0; _lxsdk_s=1714b4998ae-7bb-d2d-21e%7C%7C5'
             }
    req=urllib.request.Request(url,headers=headers)
    
    response = urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    
 
    soup = BeautifulSoup(html,'html.parser')
    all_item_divs = soup.find_all(class_='txt')
    #print(all_item_divs )
    if all_item_divs:
        for item in all_item_divs:
            all_topics = item.find_all('a')
       
            for topic in all_topics:
                click = topic['data-click-name']
                title=''
                href=''
                phone =''
                like =''
                price ='' 
                if click == "shop_title_click":
                    title = topic['title']
                    href = topic['href']
                    #print('{0} {1}'.format(title,href))
                    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:67.0) Gecko/20100101 Firefox/67.0'}
                    req_shop=urllib.request.Request(href,headers=headers)
                    resp_shop = urllib.request.urlopen(req_shop)
                    html_shop=resp_shop.read().decode('utf-8')
                    soup_shop = BeautifulSoup(html_shop ,'html.parser')
                    like_price = soup_shop.find_all(class_='rst-taste')
                    shop_info = soup_shop.find_all(class_='shopinfor')     
                    print(shop_info)                         
                    if shop_info:
                        phone = shop_info[0].find_all('p')[0].get_text()
                        #print(phone)
                        if like_price:
                            like = like_price[0].find_all('a')[0].get_text()
                            #print(like)
                            price = like_price[0].find_all('strong')[0].get_text()
                            #print(price)
                    else:                                         
                        like_price = soup_shop.find_all(class_='comment-rst')
                        shop_infos = soup_shop.find_all(class_='shop-info-content')
                        if like_price:
                            like = like_price[0].find('a').get_text()
                            #print(like)
                            price = like_price[0].find('dd').get_text()
                            #print(price)
                        for shop_info in shop_infos:
                            #print(shop_info)
                            for x in shop_info.find_all('a'):
                                #print(x)
                                if x.has_attr('data-real'):
                                    phone = x['data-real']
                                    #print(phone)
                    print('{0} {1} {2} {3} {4}'.format(title,href,like,price,phone))
                    global i
                    sheet.write(i,0,title)
                    sheet.write(i,1,href)
                    sheet.write(i,2,like)
                    sheet.write(i,3,price)
                    sheet.write(i,4,phone)
                    
                    i = i + 1

xls = xlwt.Workbook()
sheet = xls.add_sheet('ctx')
sheet.write(0,0,'title')
sheet.write(0,1,'url')
sheet.write(0,2,'like')
sheet.write(0,3,'price')
sheet.write(0,4,'phone')
url = "http://www.dianping.com/search/keyword/17/0_%E6%9C%88%E5%AD%90%E4%BC%9A%E6%89%80/o3p"
for n in range(1,10):
    url = url+str(n)
    parse(url, sheet)
xls.save('dianping.xls')
print('running over')