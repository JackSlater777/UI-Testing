import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.globalsqa.transaction import Transaction, TransactionType
from datetime import datetime


class GlobalsQaSearch:
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    SUBMIT_BTN = (By.CLASS_NAME, "btn.btn-default")
    SUBMIT_MSG = (By.CLASS_NAME, "error.ng-binding")

    def __init__(self, driver):
        self.driver = driver
        self.transactions_str = None
        self.transactions = []
        self.driver.implicitly_wait(time_to_wait=20)
        self.wait = WebDriverWait(driver=driver, timeout=10)

    @allure.step("Загрузка страницы")
    def load(self):
        self.driver.get(url=self.URL)

    def wait_until_element_to_be_clickable(self, args: tuple[str, str]):
        self.wait.until(
            method=EC.element_to_be_clickable(mark=args)
        )

    @allure.step("Авторизация")
    def auth_with_customer_login(self, number: int):
        """Авторизуемся, используя кастомный логин - Harry Potter = 2"""
        self.click_customer_login_button()
        self.choose_customer_name(number=number)
        self.click_login()

    @allure.step("Выбор авторизации через customer login")
    def click_customer_login_button(self) -> None:
        customer_login_button = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="button.btn.btn-primary.btn-lg[ng-click^='customer']"
        )
        customer_login_button.click()

    @allure.step("Выбор customer'a")
    def choose_customer_name(self, number: int) -> None:
        """Выбираем имя пользователя"""
        select = Select(
            self.driver.find_element(
                by=By.ID,
                value='userSelect'
            )
        )
        select.select_by_value(value=str(number))

    @allure.step("Клик кнопки 'логин'")
    def click_login(self) -> None:
        login_button = self.driver.find_element(
            by=By.CLASS_NAME,
            value="btn.btn-default"
        )
        login_button.click()

    @allure.step("Процесс депозита")
    def make_deposit(self, number: int) -> None:
        self.click_deposit_button()
        self.input_deposit_or_withdrawl(number=number)
        self.confirm_deposit_or_withdrawl()
        self.transactions.append(
            Transaction(
                date_time=datetime.now(),
                amount=number,
                transaction_type=TransactionType.DEPOSIT.value
            )
        )

    @allure.step("Процесс снятия")
    def make_withdrawl(self, number: int) -> None:
        self.click_withdrawl_button()
        self.input_deposit_or_withdrawl(number=number)
        self.confirm_deposit_or_withdrawl()
        self.transactions.append(
            Transaction(
                date_time=datetime.now(),
                amount=number,
                transaction_type=TransactionType.WITHDRAWL.value
            )
        )

    @allure.step("Клик кнопки депозита")
    def click_deposit_button(self) -> None:
        deposit_button = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="button[ng-class^='btnClass2']"
        )
        deposit_button.click()
        self.wait.until(
            method=EC.text_to_be_present_in_element(locator=self.SUBMIT_BTN, text_="Deposit")
        )

    @allure.step("Клик кнопки снятия")
    def click_withdrawl_button(self) -> None:
        withdrawl_button = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="button[ng-class^='btnClass3']"
        )
        withdrawl_button.click()
        # TODO: не работает explicit wait! Атрибуты объекта не обновляется! Баг?
        # self.wait.until(
        #     method=EC.text_to_be_present_in_element(locator=self.SUBMIT_BTN, text_="Withdrawl")
        # )
        import time
        time.sleep(1)

    @allure.step("Ввод депозита/снятия")
    def input_deposit_or_withdrawl(self, number: int) -> None:
        field_input = self.driver.find_element(
            by=By.CLASS_NAME,
            value="form-control"
        )
        field_input.clear()  # На всякий случай очищаем
        field_input.send_keys(str(number))

    @allure.step("Подтверждение депозита")
    def confirm_deposit_or_withdrawl(self) -> None:
        submit_button = self.driver.find_element(*self.SUBMIT_BTN)
        submit_button.click()

    @allure.step("Получение баланса")
    def get_balance(self) -> str:
        balance = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div[2]/div/div[2]/strong[2]"
            # TODO: Проблема с нахождением уникального локатора
            # by=By.CSS_SELECTOR,
            # value="strong.ng-binding"
            # body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)
        )
        return balance.text

    @allure.step("Клик кнопки транзакций")
    def click_transactions_button(self) -> None:
        transactions_button = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="button[ng-class^='btnClass1']"
        )
        transactions_button.click()

    @allure.step("Получение транзакций в строковом виде")
    def get_transactions_str_info(self) -> None:
        # TODO: транзакции не успевают прогрузиться?
        self.transactions_str = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="tbody"
        ).text

    @allure.step("Получение транзакций в виде массива строк")
    def get_transactions_array(self) -> list:
        if not self.transactions_str:
            self.get_transactions_str_info()

        return self.transactions_str.split("\n")
