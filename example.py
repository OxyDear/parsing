#  -*- coding: utf-8 -*-

import requests
import json
import os
import csv
from datetime import datetime


def collect_info():
    # proxies = {
    #     'https': f'http://{os.getenv("LOGIN")}:{os.getenv("PASSWORD")}@proxy:port'
    # }

    t_date = datetime.now().strftime('%d_%m_%Y')

    response = requests.get(url='https://www.lifetime.plus/api/analysis2')

    # with open(f'info_{t_date}.json', 'w') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    categories = response.json()['categories']
    result = []

    for c in categories:
        c_name = c.get('name').strip()
        c_items = c.get('items')

        for item in c_items:
            item_name = item.get('name').strip()
            item_price = item.get('price')
            item_desc = item.get('description').strip()

            if 'β' in item_desc:
                item_desc = item_desc.replace('β', 'B')

            if 'γ' in item_desc:
                item_desc = item_desc.replace('γ', 'Y')

            item_wt = item.get('days')
            item_bio = item.get('biomaterial')

            result.append(
                [c_name, item_name, item_bio, item_desc, item_price, item_wt]
            )

    with open(f'result_{t_date}.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Категория',
                'Анализ',
                'Биоматериал',
                'Описание',
                'Стоимость',
                'Готовность дней'
            )
        )

        writer.writerows(
            result
        )


def make_request():
    response = requests.delete('https://reqres.in/api/users/2')

    print('response: 👉️', response)  # response: 👉️ <Response [204]>
    print('response.text: 👉️', response.text)  # response.text: 👉️ ""

    # response.status_code: 👉️ 204
    print('response.status_code: 👉️', response.status_code)

    print('response.headers: 👉️', response.headers)

    if (response.status_code != 204
            and 'content-type' in response.headers
            and 'application/json' in response.headers['content-type']):
        parsed = response.json()
        print('✅ parsed response: 👉️', parsed)
    else:
        # 👇️ this runs
        print('⛔️ conditions not met')


def main():
    collect_info()
    make_request()


if __name__ == '__main__':
    main()
