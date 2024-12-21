# Условная конструкция. Операторы if, elif, else
print('Найдём, сколько одинаковых чисел Вы ввели?')
first = int(input('first number: '))
second = int(input('second number: '))
third = int(input('third number: '))
if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0, ', нет одинаковых')