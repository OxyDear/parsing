import requests
import os
import csv
import json
from datetime import datetime
import duolingo


def get_info_duo():
    data = open('config.txt', encoding='utf-8')
    login, password = data.read().split()

    lingo = duolingo.Duolingo(login, password)
    lg = lingo.get_languages(abbreviations=True)
    len_topics = len(lingo.get_known_topics(lg[0]))
    len_unknown_topics = len(lingo.get_unknown_topics(lg[0]))
    daily_exp = lingo.get_daily_xp_progress()
    skill_list = lingo.get_learned_skills(lg[0])
    words = lingo.get_vocabulary(lg[0])
    count = 0
    my_word = words['vocab_overview'][0]

    file = open('words.txt', 'a', encoding='utf-8')
    for index, word in enumerate(words['vocab_overview']):
        file.write(f'{list(lingo.get_translations([word["word_string"]], source=lg[0], target="ru").keys())[0]} - ')
        for i in lingo.get_translations([word["word_string"]], source=lg[0], target="ru")[word["word_string"]]:
            if i == lingo.get_translations([word["word_string"]], source=lg[0], target="ru")[word["word_string"]][-1]:
                file.write(i + '\n')
            else:
                file.write(f'{i}, ')

        count_add = str(len(words["vocab_overview"]))

        print(
            f'{str(index + 1)} из {count_add}. Выполнено на {str((((index + 1) / (len(words["vocab_overview"]))) * 100))[0:4]}%')

    # for skill in skill_list:
    #     print(skill['words'])
    #     count += len(skill['words'])

    print(len_topics,
          len_unknown_topics,
          daily_exp,
          count)


def collect_info():
    headers = {
        'accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange; v = b3; q = 0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru - RU, ru; q = 0.9, en - US; q = 0.8, en; q = 0.7',
    }

    date = datetime.now().strftime('%d_%m_%Y')
    response = requests.get(url='https://www.duolingo.com/vocabulary/overview?_=1665248469447', headers=headers)

    with open(f'info_{date}_.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def main():
    # collect_info()
    get_info_duo()


if __name__ == '__main__':
    main()
