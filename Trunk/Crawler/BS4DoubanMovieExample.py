from bs4 import BeautifulSoup
import urllib.request as urlrequest
url = 'https://movie.douban.com/subject/26387939/'
web_page = urlrequest.urlopen(url).read()
soup = BeautifulSoup(web_page,'html.parser')
name = soup.h1.find(property='v:itemreviewed').string
avg = soup.find_all(class_='ll rating_num')[0].get_text()
print('{} {}'.format(name,avg))