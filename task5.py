number = int(input("Введите значение рейтинга: "))
my_list = [7, 5, 3, 3, 2]
for x in my_list:
    current_index = my_list.index(x)
    if number >= x:
        my_list.insert(current_index, number)
        break
    elif current_index == len(my_list) - 1:
        my_list.append(number)
        break