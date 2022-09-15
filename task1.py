# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


# ПРОСТОЙ ВАРИАНТ РЕШЕНИЯ ЗАДАЧИ :  print(sum(list_numbers[1::2]))

def Sum_odd_positions(list_numbers):
    sum = 0
    for i in range(1, len(list_numbers)):
        if i % 2 != 0:
            sum += list_numbers[i]
    return sum


try:
    list_numbers = list(int(i) for i in (
        input('\nEnter numbers separated by a space:\t').split()))
    print('\nResulting list of numbers -->\t', list_numbers)
    print('\nNumbers in odd positions -->\t', *list_numbers[1::2])
    print(
        f'\nSum of numbers in odd positions -->\t{Sum_odd_positions(list_numbers)}\n')
except ValueError:
    print('Incorrect data! You must enter number, try again!')
