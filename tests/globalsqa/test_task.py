import allure
from pages.globalsqa.search import GlobalsQaSearch
from framework.csv_dump import CsvDumper
from framework.fibonacci import get_tomorrow_fibonacci_number

# Команда на запуск теста:
# pytest tests/globalsqa/test_task.py::TestTask::test_task_positive --alluredir=output --clean-alluredir

# Просмотр отчета на localhost:
# allure serve output


@allure.feature("Тестовое задание")
class TestTask:
    @allure.story("Тестовое задание - позитивный кейс")
    def test_task_positive(self, driver_init):
        globalsqa_page = GlobalsQaSearch(driver=driver_init)
        globalsqa_page.load()
        globalsqa_page.auth_with_customer_login(number=2)  # 2 - Harry Potter
        globalsqa_page.make_deposit(number=get_tomorrow_fibonacci_number())
        globalsqa_page.make_withdrawl(number=get_tomorrow_fibonacci_number())

        # Валидация баланса
        assert globalsqa_page.get_balance() == "0", "Баланс не равен нулю!"

        # Валидация транзакций
        globalsqa_page.click_transactions_button()
        globalsqa_page.get_transactions_array()
        assert len(globalsqa_page.transactions) == 2, "Количество транзакций отличается от ожидаемого!"
        for actual_transaction, expected_transaction in zip(
                globalsqa_page.transactions,
                globalsqa_page.get_transactions_array()
        ):
            assert actual_transaction.formatted_str == expected_transaction, \
                "Информация о транзакции отличается от ожидаемой!"

        # Оформление csv-файла с информацией о транзакциях, прикрепление к отчету
        csv_dumper = CsvDumper()
        csv_dumper.write_transactions(
            browser_name=driver_init.caps.get("browserName"),
            transactions=globalsqa_page.transactions
        )
        csv_dumper.attach()
