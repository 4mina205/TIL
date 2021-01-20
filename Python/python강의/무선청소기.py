from selenium import webdriver
driver = webdriver.Chrome('c:/scrap/chromedriver.exe')
url = "http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
driver.get(url)
from bs4 import BeautifulSoup

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup)

prod_items = soup.select('li.prod_item')
print(len(prod_items))
title = prod_items[0].select('p.prod_name > a')[0].text.strip()
print(title)
spec_list = prod_items[0].select('div.spec_list')[0].text.strip()
print(spec_list)
