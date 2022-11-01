from selenium import webdriver

# Указываем путь к веб-драйверу
driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)
# Открываем браузер на данной странице
# Это специальный сайт для практики автотестирования
driver.get('http://tutorialsninja.com/demo/')


from selenium.webdriver.common.keys import Keys
