#UTF-8

"""DouBan movie"""

import urllib.request as urlrequest
import json

id_list = [26387939,11803087,20451290]

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
