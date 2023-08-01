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

# 4. Написати програму, яка перекладає введену користувачем англійську фразу на українську. Користувач повинен вводити фразу англійською, поки не буде введено слово "закінчити".
# 5. Створити список слів і попросити користувача ввести слово. Програма повинна перевірити, чи є слово в списку, і якщо так, вивести "Так, це слово є у списку", а якщо ні, повідомити про це і попросити ввести ще раз.

fruits_dict = ["apple", "strawberry", "watermelon", "cherry"]
while True:
    word = input("Please enter the word :")
    if word in fruits_dict:
        print("Yes, this word is in the list")
        break
    else:
      print("There is no such word in the list. Please enter another one.")



# 6. Запитати користувача про його ім'я та вік, а потім вивести привітання і повідомлення про те, чи йому більше 18 років.