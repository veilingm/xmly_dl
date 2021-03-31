from bs4 import BeautifulSoup
import urllib
from urllib import request

headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}
xmly_url = "https://www.ximalaya.com/xiangsheng/39488639/317045722"
xmly_url2 = "https://www.ximalaya.com/renwenjp/31891686/397666167"


req = request.Request(xmly_url, headers=headers)
tmp = request.urlopen(req);
page = request.urlopen(req).read()
page = page.decode('utf-8')


print(page)

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')
