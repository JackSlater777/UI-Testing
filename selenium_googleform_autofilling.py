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
options.add_argument("--headless")
# Альтернативный синтаксис
# options.headless = True


# # Автоматически заполняем google-form'у
try:
    # Идем на страницу формы
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSenPnjUqt-X_LrCwCbfdMJj-ibCC_Bi4elAzC6FM4TBX0We9w/viewform')
    # Ждем 3 секунды
    time.sleep(3)

    # # Заполняем поле с текстом
    # То, что вводим
    name = 'Ivan'
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - copy - copy xpath
    name_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    # Находим поле
    name_input = driver.find_element(by=By.XPATH, value=name_xpath)
    # На всякий случай очищаем поле
    name_input.clear()
    # Вводим в окошко заданное значение
    name_input.send_keys(name)
    # Ждем 2 секунды
    time.sleep(2)

    # # Заполняем поле с выбором (точкой)
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - copy - copy xpath
    choice_xpath = '//*[@id="i5"]/div[3]/div'
    # Находим поле
    choice_input = driver.find_element(by=By.XPATH, value=choice_xpath)
    # Имитируем клик
    choice_input.click()
    # Ждем 2 секунды
    time.sleep(2)

    # # Нажимаем кнопку отправить (submit)
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - copy - copy xpath
    submit_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    # Находим поле
    submit_input = driver.find_element(by=By.XPATH, value=submit_xpath)
    # Имитируем клик
    submit_input.click()
    # Ждем 2 секунды
    time.sleep(2)

    # # Валидация отправки
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - edit as html - копируем строку класса
    validation_class = '.vHW8K'  # ТОЧКА ВПЕРЕДИ СТРОКИ!!!
    # Находим поле
    get_validation = driver.find_element(by=By.CSS_SELECTOR, value=validation_class)
    if get_validation.text == 'Ответ записан.':
        print('Test was successful')
    else:
        print('Test was NOT successful!')

except TimeoutException:
    print('Timeout exception!')
finally:
    driver.close()
    driver.quit()
