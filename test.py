import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from path_to_website import path_to_website
from path_to_webdriver import path_to_webdriver


# Указываем путь к веб-драйверу
driver = webdriver.Chrome(
    executable_path=path_to_webdriver
)


try:
    # Открываем в браузере тестируемый сайт
    driver.get(path_to_website)
    # Ждем 5 секунд
    time.sleep(5)
except TimeoutException:
    print('Timeout exception!')
finally:
    driver.close()
    driver.quit()

# Ищем на сайте различные элементы
# name = 'search'
# elem = driver.find_element(by=By.NAME, value=name)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
