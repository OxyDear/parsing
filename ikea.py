import requests
from bs4 import BeautifulSoup as BS
import json
import lxml.html

url = 'https://www.ikea.cn/cn/en/'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-language': 'en-US',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# req = requests.get(url=url, headers=headers)
# src = req.text

with open('ikea.json', encoding='utf-8') as file:
    src = json.load(file)

for i in src:
    for name, index in i.items():
        print(name, index)

# tree = lxml.html.fromstring('ikea.html')
# print(tree.xpath('/html/body/div[1]/main/div/main/div/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]'))
# soup = BS(src, 'lxml')
# storage_and_organisation = soup.find(class_='i-layout i-layout--pc').find(class_='i-layout__header') \
#     .find(class_='nav-header').find(class_='nav-header_container').find(class_='move-hover').find(
#     class_='header_container_bottom')
# # # .find(class_='header_container_bottom').find(class_='header_container_bottom_content')\
# # # .find(class_='nav-header-category-box').find(class_='sub-list').find(class_='sub-title')
# #
# print(storage_and_organisation)
