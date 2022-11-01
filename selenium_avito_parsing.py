import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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
# options.add_argument("--headless")
# Альтернативный синтаксис
# options.headless = True


# # Авторизуемся на сайте
try:
    # Идем на нужную страницу avito
    driver.get('https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty')
    print(driver.window_handles)
    print(f"Currently URL is: {driver.current_url}")
    # Ждем 2 секунды
    time.sleep(2)
    # Альтернатива паузе
    # driver.implicitly_wait(2)

    # При клике объявление открывается в новой вкладке, мы явно должны указать, на какой
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - собираем список из объявлений
    # по атрибуту data-marker со значениями item-photo
    data_markers = "//div[@data-marker='item-photo']"
    # Находим поле
    items = driver.find_element(by=By.XPATH, value=data_markers)
    # Открываем вкладку с конкретным товаром (первым в списке)
    items[0].click()
    print(driver.window_handles)
    # Ждем 2 секунды
    time.sleep(2)
    # Все открытые вкладки добавляются в список driver.window_handles
    # Перемещаемся в нужную вкладку
    driver.switch_to.window(driver.window_handles[1])  # [0] - основная страница
    # Ждем 2 секунды
    time.sleep(2)
    print(f"Currently URL is: {driver.current_url}")

    # Парсим имя продавца (div - class: seller-info-name)  ## Можно и через data-marker
    seller_class = 'seller-info-name'
    # Находим нужное поле
    seller = driver.find_element(by=By.CLASS_NAME, value=seller_class)
    # Выводим на печать
    print(f'Seller is: {seller.text}')
    # Ждем 2 секунды
    time.sleep(2)
    # Закрываем текущую вкладку
    driver.close()
    # Переходим на основную страницу
    driver.switch_to.window(driver.window_handles[0])
    # Ждем 2 секунды
    time.sleep(2)
    print(f"Currently URL is: {driver.current_url}")

    # # Открываем следующее объявление
    items[1].click()
    print(driver.window_handles)
    # Ждем 2 секунды
    time.sleep(2)
    # Перемещаемся в нужную вкладку
    driver.switch_to.window(driver.window_handles[1])  # [0] - основная страница
    # Ждем 2 секунды
    time.sleep(2)
    print(f"Currently URL is: {driver.current_url}")

    # Парсим имя продавца (xpath: seller-info-name)  ## Можно и через data-marker
    seller_xpath = "//div[@data-marker='seller-info/name']"
    # Находим нужное поле
    seller = driver.find_element(by=By.XPATH, value=seller_xpath)
    # Выводим на печать
    print(f'Seller is: {seller.text}')

    # Парсим дату публикации объявления (class)
    date_class = "title-info-metadata-item-redesign"
    # Находим нужное поле
    date = driver.find_element(by=By.CLASS_NAME, value=date_class)
    # Выводим на печать
    print(f'An ad date is: {date.text}')
    # Ждем 2 секунды
    time.sleep(2)

    # Парсим дату регистрации пользователя (class)
    joined_date_class = "seller-info-value"
    joined_date = driver.find_element(by=By.CLASS_NAME, value="")[1]
    # Выводим на печать
    print(f'User since: {joined_date.text}')

except TimeoutException:
    print('Timeout exception!')
finally:
    driver.close()
    driver.quit()
