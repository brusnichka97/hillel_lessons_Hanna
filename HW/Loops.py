# 1. Вимагати від користувача ввести пароль, який містить певну кількість символів або відповідає певним критеріям безпеки (наприклад, наявність прописних і маленьких літер, цифр та спеціальних символів).

# while True:
#     password = input("Enter password (with 8 symbols, at least one capital, one number and one special symbol)")
#     if len(password) < 8:
#         print("Password has to contain more than 8 symbols.")
#     elif not any(char.isdigit() for char in password):
#         print("Password has to contain at least one number")
#     elif not any(char.isupper() for char in password):
#         print("Password has to contain at least one upper letter")
#     elif not any(char.islower() for char in password):
#         print("Password has to contain at least one lower letter")
#     elif not any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/~`' for char in password):
#         print("Password has to contain at least one special symbol")
#     else:
#         print("Thank you! Your password is correct.")
#     break

# 2. Попросити користувача ввести число, і якщо воно менше за 100, повідомляти йому про це і просити ввести число знову.

# while True:
#     test_number = int(input("Enter number that more than 100 :"))
#     if test_number <= 100:
#         print("You number is less than 100, please enter enother one.")
#     else:
#         print("Thank you!")
#         break

# 3. Створити програму, яка грає в гру "вгадай число". Комп'ютер обирає випадкове число, а користувач повинен вгадати його. Комп'ютер дає підказки (тип "більше" або "менше"), доки користувач не вгадає число.
# import random
# secret_number = random.randint(1, 100)
#
# print("Hi! Guess the number.")
# while True:
#     guess = int(input("Enter your number: "))
#
#     if guess == secret_number:
#         print("Congrats, you guessed number!")
#         break
#     elif guess < secret_number:
#         print("Your number is less")
#     elif guess > secret_number:
#         print("Your number is more")

# 4. Написати програму, яка перекладає введену користувачем англійську фразу на українську. Користувач повинен вводити фразу англійською, поки не буде введено слово "закінчити".

# 5. Створити список слів і попросити користувача ввести слово. Програма повинна перевірити, чи є слово в списку, і якщо так, вивести "Так, це слово є у списку", а якщо ні, повідомити про це і попросити ввести ще раз.

# fruits_dict = ["apple", "strawberry", "watermelon", "cherry"]
# while True:
#     word = input("Please enter the word :")
#     if word in fruits_dict:
#         print("Yes, this word is in the list")
#         break
#     else:
#       print("There is no such word in the list. Please enter another one.")
#


# 6. Запитати користувача про його ім'я та вік, а потім вивести привітання і повідомлення про те, чи йому більше 18 років.
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# while age >= 18:
#     print("Hi, your age is more than 18.")
#     break
# else:
#     print("Hi, your age is under 18.")

#Задання: Перевірити, що всі елементи списку є унікальними (не повторюються).
# start_list = [1, 2, 4, "one", "one", 4]
# is_unique = True
# for value in start_list:
#     if start_list.count(start_list) >1:
#         is_unique = False
#         break
# print("is unique", is_unique)
#
# # Припустимо, що у нас є список зі значень
# values = [10, 20, 30, 40, 50]

# # Завдання: Перевірити, що всі елементи у списку є унікальними
# is_unique = True
# for value in values:
#     if values.count(value) > 1:
#         is_unique = False
#         break
#
# print("Всі елементи у списку є унікальними:", is_unique)

