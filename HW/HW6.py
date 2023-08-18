# xn= xn-1 + xn-2
# Написати функцыю, яка буде рекурсивно вираховувати число фібоначчі.
#
# Число фібоначчі - це число, яке дорівнює суммі двох попередніх в послідовності (це і повинно бути в рекурсії). Закінчується на двох одиницях
def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci_sequence(n-1)) + (fibonacci_sequence(n-2))

n = 8
result = fibonacci_sequence(n)
print(result)

while True:
    fibonacci_sequence(n) != 1













