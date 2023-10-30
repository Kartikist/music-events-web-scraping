import requests
import selectorlib
from datetime import datetime
from emailsend import send_email

URL = 'https://programmer100.pythonanywhere.com/'
HEADERS = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

current_time = str(datetime.now())

def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("temp.yaml")
    value = extractor.extract(source)["temperature"]
    return value


    
def store(extracted):
    with open("temp.txt", 'a') as file:
        file.write(current_time +','+ extracted + '\n')
        
def send():
    with open("temp.txt", 'r') as file:
        a = file.readlines()
        
    date_list = []
    temp_list = []
    b = a[1:]
    b = [i.rstrip() for i in b]
    for i in b:
        date, temp = i.split(',')
        date_list.append(date)
        temp_list.append(temp)

    return date_list, temp_list

if __name__ == '__main__':
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)