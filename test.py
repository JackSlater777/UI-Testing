# Запуск через терминал
# pytest -s -v test.py
# -v - более детальный принт результата теста
# -s - отображение принтов внутри тестов
# --duration=int -vv - все тесты, прохождение которых займет более int секунд, будут отмечены, как slowest

# Для генерации файлов отчета allure
# pytest -s -v test.py --alluredir=results
# Не забыть добавить папку results в .gitignore
# Для отображения отчета в браузере в командной строке в папке с проектом
# allure serve results

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from path_to_website import path_to_website
from path_to_webdriver import path_to_webdriver


class TestSelenium:

    """Добавление айфона в корзину"""
    def test_add_to_shopping_cart(self):
        # Указываем путь к веб-драйверу
        driver = webdriver.Chrome(
            executable_path=path_to_webdriver
        )
        # Полноэкранный режим
        driver.maximize_window()
        # Открываем в браузере тестируемый сайт
        driver.get(path_to_website)
        # Ищем на странице поисковую строку
        search_field = driver.find_element(By.NAME, 'search')
        # Печатаем в неё слово "iphone"
        search_field.send_keys("iphone")
        # Нажимаем ENTER
        search_field.send_keys(Keys.RETURN)
        # Страница меняется - выдаются результаты поиска айфонов
        # Ищем на странице кнопку Add to cart - добавить в корзину
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
        # Кликаем кнопку
        add_to_cart_button.click()
        # 1 айфон добавился в корзину
        # Ищем на странице ссылку корзины
        shopping_cart_link = driver.find_element(By.LINK_TEXT, 'Shopping Cart')
        # Кликаем на неё
        shopping_cart_link.click()
        # Делаем проверку на наличие текста на странице (модель айфона)
        assert "product 11" in driver.page_source
        # Закрываем браузер
        driver.close()
        # Выключаем веб-драйвер
        driver.quit()

    def test_delete_from_shopping_cart(self):
        """Удаление из корзины"""
        assert True


if __name__ == '__main__':
    pytest.TestSelenium()
