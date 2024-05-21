from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class TransactionType(Enum):
    DEPOSIT = "Credit"
    WITHDRAWL = "Debit"


@dataclass
class Transaction:
    amount: int
    transaction_type: TransactionType
    date_time: datetime
    formatted_str: str = None
    report_date: str = None

    def __post_init__(self):
        """Формирование строкового представления транзакции для валидации и отчета"""
        date_format = f"{self.convert_int_month_to_str()} {self.date_time.day}, %Y %#I:%M:%S %p"
        self.formatted_str = self.date_time.strftime(date_format) + f" {str(self.amount)} {self.transaction_type}"

        report_date_format = "%d %m %Y %H:%M:%S"
        self.report_date = self.date_time.strftime(report_date_format)

    def convert_int_month_to_str(self):
        month_mapping = {
            1: "Jan",
            2: "Feb",
            3: "Mar",
            4: "Apr",
            5: "May",
            6: "Jun",
            7: "Jul",
            8: "Aug",
            9: "Sep",
            10: "Oct",
            11: "Nov",
            12: "Dec",
        }
        return month_mapping.get(self.date_time.month)
