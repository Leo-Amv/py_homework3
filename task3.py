# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


def diff_float_parts(list_numbers):
    float_parts = list()
    for i in range(len(list_numbers)):
        if list_numbers[i] % 1 != 0:
            float_parts.append(round((list_numbers[i] % 1), 4))
    print(f'\nMax part: {max(float_parts)}\nMin part: {min(float_parts)}')
    return round(max(float_parts)-min(float_parts), 4)


try:
    list_numbers = list(float(i) for i in (
        input('\nEnter float numbers separated by a space:\t').split()))
    print('\nResulting list of numbers -->\t', list_numbers)
    print(
        f'\nThe difference between the maximum and minimum part -->\t{diff_float_parts(list_numbers)}\n')
except ValueError:
    print('Incorrect data! You must enter number, try again!')
