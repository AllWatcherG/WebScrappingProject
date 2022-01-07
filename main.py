import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/gabri/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findAll(attrs='blog-card__content-wrapper'):
    name = element.find('a')
    if name not in results:
        results.append(name.text)
df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')



