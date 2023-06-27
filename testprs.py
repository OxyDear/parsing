# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
import json
import csv

# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)

# with open('index.html', encoding='utf-8') as file:
#     src = file.read()
#
# soup = BS(src, 'lxml')
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
#
# all_categories = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')
#
#     all_categories[item_text] = item_href
#
# with open('all_categories.json', 'w') as file:
#     json.dump(all_categories, file, indent=4, ensure_ascii=False)


with open('all_categories.json') as file:
    all_categories = json.load(file)

iter_count = int(len(all_categories))-1
count = 0
print(iter_count)

for name, href in all_categories.items():

    rep = [',', ' ', '-', "'"]
    for item in rep:
        if item in name:
            name = name.replace(item, '_')

    req = requests.get(url=href, headers=headers)
    src = req.text

    with open(f'data/{count}_{name}.html', 'w', encoding='utf-8') as file:
        file.write(src)

    with open(f'data/{count}_{name}.html', encoding='utf-8') as file:
        src = file.read()

    soup = BS(src, 'lxml')

    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue

    table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f'data/{count}_{name}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )

        product_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

        products_info = []
        for item in product_data:
            product_tds = item.find_all('td')

            title = product_tds[0].find('a').text
            calories_data = product_tds[1].text
            proteins_data = product_tds[2].text
            fats_data = product_tds[3].text
            carbohydrates_data = product_tds[4].text

            products_info.append(
                {
                    'Title': title,
                    'Calories': calories_data,
                    'Proteins': proteins_data,
                    'Fats': fats_data,
                    'Carbohydrates': carbohydrates_data
                }
            )

            with open(f'data/{count}_{name}.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        title,
                        calories_data,
                        proteins_data,
                        fats_data,
                        carbohydrates_data
                    )
                )

        with open(f'data/{count}_{name}.json', 'a', encoding='utf-8') as file:
            json.dump(products_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f'Iteration {count}. {name} written...')
    iter_count = iter_count - 1

    if iter_count == 0:
        print('The work is done')
        break

    print(f'Iterations left: {iter_count}')
