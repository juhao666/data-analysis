# encoding = 'utf-8'

import urllib.request as urlrequest
from bs4 import BeautifulSoup
import xlwt
import json
import re

def proc_product(product_name,visit_url,xls):
    crawl_context = urlrequest.urlopen(visit_url).read()
    html_context = crawl_context.decode('utf-8')
    soup = BeautifulSoup(html_context,'html.parser')
    all_item_divs = soup.find_all(class_='products_wrap')
    #print(all_item_divs)
    i = 1 # excel row no

    sheet = xls.add_sheet(product_name)
    sheet.write(0,0,'产品名称')
    sheet.write(0,1,'目前价格')
    sheet.write(0,2,'销量')
    sheet.write(0,3,'图片信息')
    if all_item_divs:
        prd_list = all_item_divs[0].find_all('ul')
        if prd_list:
            all_prds = prd_list[0].find_all('li')
            for each_prd in all_prds:
                prd_name=each_prd.find(class_='s_l_name').find('a').get_text()
                prd_price = each_prd.find(class_='search_list_price').get_text()
                prd_sale_cnt = each_prd.find(class_='search_pl').get_text()
                prd_pic = each_prd.find('img')['original']
                prd_price = prd_price.replace('赠','').strip()+'¥'
                Y = [m.start() for m in re.finditer('¥', prd_price)]  
                prd_price = '¥'+prd_price[Y[0]+1:Y[1]]
                prd_name = prd_name.strip()
                #print(prd_name)
                #print(prd_price)
                #print(prd_sale_cnt)
                #print(prd_pic)
   
                sheet.write(i,0,prd_name)
                sheet.write(i,1,prd_price)
                sheet.write(i,2,prd_sale_cnt)
                sheet.write(i,3,prd_pic)     
                i = i + 1
                if i>20:
                	break


hufu = "http://search.jumei.com/?filter=0-41-1&search=%E6%8A%A4%E8%82%A4#search_list_wrap&bid=2_shttp://search.jumei.com/?filter=0-41-1&search=%E6%8A%A4%E8%82%A4#search_list_wrap&bid=2_s"
caizhaung = "http://search.jumei.com/?filter=0-41-1&search=%E5%BD%A9%E5%A6%86#search_list_wrap&bid=2_s"


xls = xlwt.Workbook()
proc_product('护肤',hufu,xls)
proc_product('彩妆',caizhaung,xls)
xls.save('jumei.xls')
print('process succeed!!!')   
