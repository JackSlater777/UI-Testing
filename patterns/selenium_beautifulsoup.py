from bs4 import BeautifulSoup


with open("blank/index.html") as file:
    # Помещаем код html-страницы в переменную
    src = file.read()


soup = BeautifulSoup(src, 'lxml')  # второй параметр - парсер
