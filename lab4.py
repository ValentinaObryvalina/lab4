def delenye_na_3(number: int):
    return True if number % 3 == 0 else False

def delenye_100(number):
    res = None
    try:
        res = 100 / float(number)
    except ValueError:
        print("В эту функцию нужно передать число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except Exception as e:
        print("Ошибка: ", e)
    return res

def magic_date(date: str):
    try:
        date = date.split(".")
        if int(date[0]) * int(date[1]) == int(date[2][2:]):
            return True
        else:
            return False
    except:
        print("Функция принимает строку с датой в формате dd.mm.yyyy")


def lucky_ticket(ticket: str):
    sum1 = sum([int(i) for i in ticket[:int(len(ticket) / 2)]])
    sum2 = sum([int(i) for i in ticket[int(len(ticket) / 2):]])
    if sum1 == sum2:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Проверка функции деления на три")
    print(delenye_na_3(14))
    print(delenye_na_3(15))

    print("\nПроверка функции деления 100 на число")
    print(delenye_100(10))
    print(delenye_100(0))
    print(delenye_100("s"))

    print("\nПроверка функции магической даты")
    print(magic_date("22.01.2022"))
    print(magic_date("21.01.2022"))

    print("\nПроверка функции счастливого билета")
    print(lucky_ticket("385916"))
    print(lucky_ticket("385916"))

