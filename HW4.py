#task 1
while True:
    first_word = input("Enter word with 'o': ")
    if 'o' in first_word.lower():
        print("Thank you!")
        break
    else:
        print("Your word doesn't have 'o', please enter another one.")

#task 2
data_list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
str_data_list = []
for item in data_list:
    if isinstance(item, str):
        str_data_list.append(item)

print(str_data_list)


#tast3
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
number_list_2 = []
for item in number_list:
    if isinstance(item, int) and item % 2 == 0:
        number_list_2.append(item)
# print(number_list_2)
print(sum(number_list_2))




