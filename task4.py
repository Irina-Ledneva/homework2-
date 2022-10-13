word = input("Введите слова через пробел: ").split()
number = 1
for i in word:
    print(f'{number}. {i[0:10]}')
    number += 1