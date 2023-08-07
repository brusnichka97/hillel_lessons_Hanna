# 1. Напишіть функцію, яка приймає два аргументи.
# a. Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
# b. Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
# c. В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
# d. Імпортуйте цю функцію, і викличте в іншому файлі

def arguments_for_comparing(first_arg="first", second_arg="second"):
    if isinstance(first_arg, (int, float)) and isinstance(second_arg, (int, float)):
        return first_arg * second_arg
    elif isinstance(first_arg, str) and isinstance(second_arg, str):
        return first_arg + second_arg
    else:
        return(first_arg, second_arg)

result1 = arguments_for_comparing(7, 1.7)
print(result1)

result2 = arguments_for_comparing("name", "second_name")
print(result2)

result3 = arguments_for_comparing(7, 5)
print(result3)

result4 = arguments_for_comparing("name", 5)
print(result4)















