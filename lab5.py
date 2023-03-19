def spisok_is_pyati():
    nums = [3, 5, 9, 15, 4]
    number = int(input("введите число: "))
    if number in nums:
        print(nums, "\n", number, "\n", "Поздравляю, Вы угадали число!")
    else:
        print(f"{nums}\n {number}\n Нет такого числа!")


def random_spisok():
    c = ["6", "7", "8", "9", "6", "3", '8', '7']
    start = 1
    for index in range(len(c)):
        if c[index] in c[start:]:
            print(c[index])
        start += 1


def dni_nedeli():
    dni = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    vopros = int(input("Сколько выходных дней в неделю Вы хотите? "))
    print(dni[:len(dni)-vopros-1:-1])
#

def spisok_stud():
    n = ['ivanov', 'ayzyak', 'belikova', 'ivshina', 'obryvalina', 'ishin', 'korobkov', 'akhmedov', 'yastrebova', 'dementyeva']
    d = ['sidorov', 'petrov', 'vasechkin', 'tolstoy', 'miroshevich', 'larina', 'zaykin', 'maltsev', 'fedorov', 'vagner']
    team = []
    for index in range(5):
        team.append(n[index])
        team.append(d[index])
    team = tuple(team)
    print(n + d)
    print(team)
    print(len(team))
    team = tuple(sorted(team))
    print(team)
    if "ivanov" in team:
        print("Иванов есть в списке")
    else:
        print("Иванова нет в списке")


if __name__ == "__main__":
    # spisok_is_pyati()
    # random_spisok()
    # dni_nedeli()
    spisok_stud()







    






