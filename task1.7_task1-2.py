
data_list = []
check_list = ['+' , '-' , '*' , '/']
data = input('Введите данные для проведения расчета: ')
for index in data:
    data_list.append(index)
    if ' ' in data_list:
        data_list.remove(' ')
try:
    if len(data_list) > 3:
        raise Exception('Расчет выполнен только для первых двух чисел')
except Exception as e:
    print(e)
def calculating(symb1, symb2, symb3):
    try:
        if symb1 == '+':
            return print(int(symb2) + int(symb3))
        if symb1 == '*':
            return print(int(symb2) * int(symb3))
        if symb1 == '/':
            return print(int(symb2) / int(symb3))
        if symb1 == '-':
            return print(int(symb2) - int(symb3))
    except ZeroDivisionError:
        print('На ноль делить нельзя!!!')
    except ValueError:
        print('Операции возможно выполнить только с числами. Количество чисел = двум!!!')
try:
    calculating(data_list[0], data_list[1], data_list[2])
except IndexError:
    print('Неверное количество элементов. Пример формата ввода: * 6 7')
try:
    assert data_list[0] in check_list , 'Недоступная операция. Возможно использование следующих знаков: + , - , * , /'
except AssertionError as e:
    print(e)
