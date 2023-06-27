from bs4 import BeautifulSoup

with open('itgen.html', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

p = soup.find_all(name='p')[-1].text.split()
p_p = ''
for i, j in enumerate(p):
    if j == '':
        p.remove(j)
    else:
        if i == 0:
            p_p += j
        else:
            p_p += ' ' + j
print(p_p)
