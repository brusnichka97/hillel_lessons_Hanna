# Create a file with numbers (in a few rows)
#
# Read this file, and print the sum of all numbers (create a new function for it)
#
# Use try\except block to avoid other symbols except numbers in the file

numbers_list = []
try:
    with open("numbers.txt") as file:
        for line in file:
            line_numbers = line.split()
            for num in line_numbers:
               try:
                  numbers_list.append(int(num))
               except:
                   pass
finally: sum(numbers_list)
print(sum(numbers_list))


    # except:
    #  print("smth")

# numbers_list = []
# try:
#     with open("numbers.txt") as file:
#         for line in file:
#             line_numbers = line.split()
#             for num in line_numbers:
#                 try:
#                     numbers_list.append(float(num))
#                 except ValueError:
#                     pass
# except FileNotFoundError:
#     print("Файл 'numbers.txt' не знайдено.")
# except Exception as e:
#     print(f"Виникла помилка: {e}")
#
# print("Список чисел:", numbers_list)