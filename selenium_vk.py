import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle


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

# # Авторизуемся на сайте
try:
    # Идем на домашнюю страницу vk
    driver.get('https://www.vk.com')
    # Ждем 3 секунды
    time.sleep(3)

    print("Passing authetification...")
    # # Заполняем поле с логином
    # То, что вводим
    email = 'your email'
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - выделяем id
    email_id = 'index_email'
    # Находим поле
    email_input = driver.find_element(by=By.ID, value=email_id)
    # На всякий случай очищаем поле
    email_input.clear()
    # Вводим в окошко заданное значение
    email_input.send_keys(email)
    # Ждем 2 секунды
    time.sleep(2)

    # # Заполняем поле с паролем
    # То, что вводим
    password = 'your password'
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - выделяем id
    password_id = 'index_pass'
    # Находим поле
    password_input = driver.find_element(by=By.ID, value=password_id)
    # На всякий случай очищаем поле
    password_input.clear()
    # Вводим в окошко заданное значение
    password_input.send_keys(password)
    # Ждем 2 секунды
    time.sleep(2)

    # # Жмем кнопку авторизации
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - выделяем id
    login = 'index_login_button'
    # Находим поле
    login_button = driver.find_element(by=By.ID, value=login)
    # Имитируем клик
    login_button.click()
    # Ждем 2 секунды
    time.sleep(2)

    # # Более изящная альтернатива - авторизация по нажатию клавиши Enter (после ввода пароля)
    password_input.send_keys(Keys.ENTER)
    # Ждем 2 секунды
    time.sleep(2)

    # # Автоматически сохраняем Cookies, чтобы не логиниться заново каждый раз
    # Записываем cookies в файл
    pickle.dump(driver.get_cookies(), open(f'{email}_cookies', 'wb'))
    # В папке появится файл с cookies
    # Чтобы подгрузить их, перепишем код после открытия окна driver.get('https://www.vk.com')
    for cookie in pickle.load(open(f'{email}_cookies', 'rb')):
        # Загружаем cookies
        driver.add_cookie(cookie)
    # Ждем 2 секунды
    time.sleep(2)
    # Если по каким-то причинам не логинится после загрузке кук, используем browser.delete_all_cookies()
    # перед тем как будем загружать свои куки, то есть перед циклом for
    # Обновляем страницу - она обновится с cookies - должна произойти автоматическая авторизация
    # Код авторизации больше не нужен, достаточно подгружать файл с cookies
    driver.refresh()
    # Ждем 2 секунды
    time.sleep(2)

    print("Going to the profile page...")
    # # Заходим в "мою страницу" и запускаем видео
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - выделяем верхний id
    profile_page_id = 'l_pr'
    # Находим поле
    profile_page = driver.find_element(by=By.ID, value=profile_page_id)
    # Имитируем клик
    profile_page.click()
    # Ждем 2 секунды
    time.sleep(2)
    # Запускаем видео, размещенное на странице
    print("Start watching the video...")
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - выделяем класс
    video_class = 'VideoPreview__thumbWrap'
    # Находим поле
    video = driver.find_element(by=By.CLASS_NAME, value=video_class)
    # Имитируем клик
    video.click()
    # Ждем 2 секунды
    time.sleep(2)
    # Мьютим аудио
    print("Muting the audio...")
    # Чтобы получить html-код окна, жмем ПКМ, inspect (просмотреть код) - выделяем верхний id
    mute_audio_xpath = '/some_xpath'
    # Находим поле
    mute_audio = driver.find_element(by=By.XPATH, value=mute_audio_xpath)
    # Имитируем клик
    mute_audio.click()
    # Ждем 2 секунды
    time.sleep(2)
    print("Finish watching the video...")

except TimeoutException:
    print('Timeout exception!')
finally:
    driver.close()
    driver.quit()
