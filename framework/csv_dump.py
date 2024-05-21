import csv
import allure


class CsvDumper:
    def __init__(self):
        self.csv_file = None

    @allure.step("Запись транзакций в файл")
    def write_transactions(self, browser_name: str, transactions: list):
        self.csv_file = f"{browser_name}_transactions_info.csv"
        with open(self.csv_file, mode='w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=";")
            filewriter.writerow(["date", "amount", "transaction type"])  # Add headers
            for actual_transaction in transactions:
                filewriter.writerow(
                    [actual_transaction.report_date, actual_transaction.amount, actual_transaction.transaction_type]
                )

    @allure.step("Прикрепление файла к отчету")
    def attach(self):
        allure.attach.file(source=self.csv_file, attachment_type=allure.attachment_type.CSV)
