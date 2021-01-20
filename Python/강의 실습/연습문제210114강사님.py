from selenium import webdriver
driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
url="http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
driver.get(url) #해당 url을 브라우저에 띄움

# print(driver.current_url)
# driver.implicitly_wait(3)

from bs4 import BeautifulSoup
html=driver.page_source
soup=BeautifulSoup(html, "html.parser")
prod_items=soup.select("li.prod_item")
# print(soup)
print(prod_items)
print(len(prod_items))

