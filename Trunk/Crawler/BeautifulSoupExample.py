from bs4 import BeautifulSoup
import urllib.request as urlrequest
url = 'http://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996'
web_page = urlrequest.urlopen(url).read()
#print(web_page)
soup = BeautifulSoup(web_page,'html.parser')
#forecast_text = soup.find(id='seven-day-forecast-container').get_text()
#forecast_text.split('\n')

#forecast_text = soup.find(id='seven-day-forecast-container').prettify()
#print(forecast_text)

forecast_text = soup.find(id='seven-day-forecast-container')
date_list = forecast_text.find_all(class_='period-name')
desc_list = forecast_text.find_all(class_='short-desc')
temp_list = forecast_text.find_all(class_='temp')

for i in range(9):
    date = date_list[i].get_text()
    desc = desc_list[i].get_text()
    temp = temp_list[i].get_text()
    print('{} {} {}'.format(date,desc,temp))
    



