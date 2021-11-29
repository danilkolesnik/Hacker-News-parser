from bs4 import BeautifulSoup
import requests
import time

url = 'https://news.ycombinator.com'
i = 1

for i in range(1000):
    if i >= 2:
        url = f'https://news.ycombinator.com/news?p={i}'
    request = requests.get(url)

    # весь код, который нужно парсить
    soup = BeautifulSoup(request.text, 'html.parser')

    titles = soup.find_all("td", class_='title')

    for title in titles:
        title = title.find('a', class_='titlelink')
        if title is not None and 'github.com' in str(title):
            sublink = title.get('href')

            with open("Results.txt", 'a') as file:
                print(str(title.text) + ' ---> ' + str(sublink),
                      file=file, sep="\n \n \n",)
    i += 1
    time.sleep(1)
    print(f'Iteration {i} Done')
