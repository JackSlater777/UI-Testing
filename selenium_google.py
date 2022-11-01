import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# Указываем явно PATH, где лежит драйвер
os.environ['PATH'] += os.pathsep + r'C:\Program Files\Google\Chrome\Application'
# Создаем объект для работы с веб-драйвером Chrome
# driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver = webdriver.Chrome()

# Отключение режима web driver'a
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

# Запуск браузера в фоновом режиме
options.add_argument("--headless")
# Альтернативный синтаксис
# options.headless = True

# # Вводим cheese! в поисковую строку и смотрим результат
try:
    # Идем на домашнюю страницу google
    driver.get('http://www.google.com')
    # Выводим в консоль заголовок страницы - "Google"
    print(driver.title)
    # Ищем элемент, чей атрибут name == 'q' ('q' - имя окна поиска qooqle)
    inputElement = driver.find_element(by=By.NAME, value='q')
    # Вводим текст в окно поиска
    inputElement.send_keys('cheese!')
    # Выполняем submit (нажатие Enter или кнопки Поиск) для поиска # (хотя google сейчас выполняет поиск и без submit)
    inputElement.submit()
    # ждем обновления страницы (заголовок обычно обновляется последним)
    WebDriverWait(driver, 10).until(EC.title_contains('cheese!'))
    # Выводим в консоль текущий заголовок - "cheese! - Поиск в Google"
    print(driver.title)
    # Ждем 3 секунды
    time.sleep(3)
    # driver.refresh()  # Обновление страницы браузера
    # driver.get_screenshot_as_file('1.png')  # Скриншот окна
    # driver.save_screenshot('2.png')  # Сохранение скриншота окна

except TimeoutException:
    print('Timeout exception!')
finally:
    driver.close()
    driver.quit()
