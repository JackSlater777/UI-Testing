from datetime import date


def get_tomorrow_fibonacci_number() -> int:
    """Расчет числа фибоначчи завтрашнего дня"""
    today = date.today().day
    return calc_fibonacci(n=today)


def calc_fibonacci(n: int) -> int:
    """Расчет числа фибоначчи с заданным порядковым индексом"""
    if n == 0:
        return 0

    if n in (1, 2):
        return 1

    return calc_fibonacci(n - 1) + calc_fibonacci(n - 2)
