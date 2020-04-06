#UTF-8

"""DouBan movie"""

import urllib.request as urlrequest
import json

url_kaola = "https://www.kaola.com/category/1472.html?key=&pageSize=60&pageNo=1&sortfield=2&isStock=false&isSelfProduct=false&isPromote=false&isTaxFree=false&factoryStoreTag=-1&isDesc=true&b=&proIds=&source=false&country=&needBrandDirect=false&isNavigation=0&lowerPrice=-1&upperPrice=-1&backCategory=&headCategoryId=&changeContent=type&#topTab"


with open('movie_score.txt','w') as output:
    for id in id_list:
        url = 'https://api.douban.com/v2/movie/{}'.format(id)
        crawl_context = urlrequest.urlopen(url).read()
        #movie = crawl_context.decode('unicode-escape')
        movie = crawl_context.decode('utf-8')
        json_context = json.loads(movie,encoding='utf-8')
        avg = json_context['rating']['average']
        name = json_context['alt_title']
        #print(name)
        output.write('{} {} {}\n'.format(id,name,avg))
