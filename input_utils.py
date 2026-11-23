import math
def parse_number(text):
        text = text.strip().replace(',', '.')
        if not text:
            raise ValueError('Пустой ввод')
        number = float(text)
        if not math.isfinite(number):
            raise ValueError('Не конечное число')
        return number
def ask_number(prompt: str) -> float:
    while True:
        try:
            return parse_number(input(prompt))
        except ValueError as e:
            print(f'Ошибка: {e}, попробуйте еще')