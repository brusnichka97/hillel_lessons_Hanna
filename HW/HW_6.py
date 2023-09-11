# xn= xn-1 + xn-2
# Написати функцію, яка буде рекурсивно вираховувати число фібоначчі.
#Число фібоначчі - це число, яке дорівнює суммі двох попередніх в послідовності (це і повинно бути в рекурсії). Закінчується на двох одиницях

def fibbonchi(count, curr_num, prev_num):

    new_num = curr_num + prev_num

    prev_num = curr_num
    curr_num = new_num
    print(new_num)

    count = count - 1
    if count == 1:
        return

    fibbonchi(count, curr_num, prev_num)
print(fibbonchi(22,0, 1))







