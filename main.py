from calc_core import calc
from input_utils import ask_number

def run_calculator():
    expr = input("Введите выражение (или 'exit'): ").strip()
    if expr == "exit":
        return
    try:
        result = calc(expr)
        print(f"Ответ: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Ошибка: {e}")

def run_discriminant():
    a = ask_number("\nВведите a: ")
    b = ask_number("Введите b: ")
    c = ask_number("Введите c: ")
    if a == 0:
        print("a не может быть 0 — это не квадратное уравнение")
        return
    D = b ** 2 - 4 * a * c
    if D < 0:
        print('Нет решений')
    elif D == 0:
        x = -b / (2 * a)
        print(f'x = {x}')
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print(f'x1 = {x1}, x2 = {x2}')

def run_pythagoras():
    print('\n0 - выход')
    print("1 - гипотенуза")
    print("2 - катет")
    number = ask_number("Что нужно найти?:  ")
    if number == 0:
        print('Выход')
    elif number == 1:
        leg1 = ask_number("Введите первый катет: ")
        leg2 = ask_number("Введите второй катет: ")
        hypotenuse = (leg1 ** 2 + leg2 ** 2) ** 0.5
        print(f"Гипотенуза: {hypotenuse}")
    elif number == 2:
        hypotenuse = ask_number("Введите гипотенузу: ")
        leg1 = ask_number("Введите катет: ")
        if hypotenuse < leg1:
            print("Гипотенуза не может быть меньше катета")
            return
        leg2 = (hypotenuse ** 2 - leg1 ** 2) ** 0.5
        print(f"Второй катет: {leg2}")
    else:
        print("Неверное число")

def main():
    while True:
        print("\n0 - Выход")
        print("1 - Калькулятор")
        print("2 - Дискриминант")
        print("3 - Теорема Пифагора")
        try:
            choice = int(input("Выбор: "))
        except ValueError:
            print("Это не число, попробуйте ещё")
            continue
        if choice == 0:
            print("Пока!")
            break
        elif choice == 1:
            run_calculator()
        elif choice == 2:
            run_discriminant()
        elif choice == 3:
            run_pythagoras()
        else:
            print("Нет такого пункта")
if __name__ == "__main__":
    main()
