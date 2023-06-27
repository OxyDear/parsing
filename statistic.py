import matplotlib.pyplot as plt
import config


file = open('messages.txt', 'r', encoding='utf-8')

all_msg = 0
count = 0

for word in file.read().split():
    for index in list(config.words.keys()):
        if index in word.lower():
            print(word)
            config.words[index] += 1

    all_msg += 1

for w in list(config.words.values()):
    count += w

for a, b in list(config.words.items())[0:11]:
    plt.text(a, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=11)  # ha Текст указывается в середине столбца, va указывает положение текста, а fontsize указывает размер шрифта

# Установить данные по осям X и Y, оба могут быть списком или кортежем
x_axis = tuple(list(config.words.keys())[0:11])
y_axis = tuple(list(config.words.values())[0:11])

plt.bar(x_axis, y_axis)  # Если цвет не указан, все столбцы будут одного цвета

plt.xlabel("Слова")  # Укажите описание информации по оси X
plt.ylabel("Количество")  # Укажите информацию описания оси Y
plt.title('Статистика слов используемых в чате')  # Укажите информацию описания диаграммы
plt.ylim(0, 300)  # Укажите высоту оси Y
plt.savefig('images/{}.png'.format('words1'))  # Сохранить как картинку
plt.show()

for a, b in list(config.words.items())[11:]:
    plt.text(a, b + 0.05, '%.f' % b, ha='center', va='bottom', fontsize=11)

x_axis2 = tuple(list(config.words.keys())[11:])
y_axis2 = tuple(list(config.words.values())[11:])

plt.bar(x_axis2, y_axis2)  # Если цвет не указан, все столбцы будут одного цвета

plt.xlabel("Слова")  # Укажите описание информации по оси X
plt.ylabel("Количество")  # Укажите информацию описания оси Y
plt.title('Статистика слов используемых в чате')  # Укажите информацию описания диаграммы
plt.ylim(0, 300)  # Укажите высоту оси Y
plt.savefig('images/{}.png'.format('words2'))  # Сохранить как картинку
plt.show()

print(config.words, all_msg, count, count / all_msg)
