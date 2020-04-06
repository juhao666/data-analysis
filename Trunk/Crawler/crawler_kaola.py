# encoding = 'utf-8'

import urllib.request as urlrequest
from bs4 import BeautifulSoup
import xlwt
import json


def proc_product(product_name,visit_url,xls):
    crawl_context = urlrequest.urlopen(visit_url).read()
    html_context = crawl_context.decode('utf-8')
    soup = BeautifulSoup(html_context,'html.parser')
    all_item_divs = soup.find_all(class_='goods')
    #print(all_item_divs)
    i = 1 # excel row no

    sheet = xls.add_sheet(product_name)
    sheet.write(0,0,'产品名称')
    sheet.write(0,1,'目前价格')
    sheet.write(0,2,'销量')
    sheet.write(0,3,'图片信息')
    for each_item_div in all_item_divs:
        #col_idx = 0
        img = each_item_div.find(class_='img')
        prd_name = img.find('img')['alt']
        prd_pic = 'http:'+img.find('img')['data-src']
        prd_price = each_item_div.find(class_='desc clearfix').find(class_ = 'cur').get_text()
        prd_sale_cnt = each_item_div.find(class_ = 'goodsinfo clearfix').find(class_="comments").get_text()
        sheet.write(i,0,prd_name)
        sheet.write(i,1,prd_price)
        sheet.write(i,2,prd_sale_cnt)
        sheet.write(i,3,prd_pic)
        #int(prd_name)
        #print(prd_pic)
        #print(prd_price)
        #print(prd_sale_cnt)        
        i = i + 1
        if i>20:
        	break


hufu = "https://www.kaola.com/category/1472.html?key=&pageSize=60&pageNo=1&sortfield=2&isStock=false&isSelfProduct=false&isPromote=false&isTaxFree=false&factoryStoreTag=-1&isDesc=true&b=&proIds=&source=false&country=&needBrandDirect=false&isNavigation=0&lowerPrice=-1&upperPrice=-1&backCategory=&headCategoryId=&changeContent=type&#topTab"
caizhaung = "https://www.kaola.com/category/1473.html?key=&pageSize=60&pageNo=1&sortfield=2&isStock=false&isSelfProduct=false&isPromote=false&isTaxFree=false&factoryStoreTag=-1&isDesc=true&b=&proIds=&source=false&country=&needBrandDirect=false&isNavigation=0&lowerPrice=-1&upperPrice=-1&backCategory=&headCategoryId=&changeContent=type&#topTab"

xls = xlwt.Workbook()
proc_product('护肤',hufu,xls)
proc_product('彩妆',caizhaung,xls)
xls.save('kaola.xls')
print('process succeed!!!')   
