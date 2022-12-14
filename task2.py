# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from math import ceil


def product_of_pairs(list_numbers):
    product = list()
    for i in range(ceil(len(list_numbers)/2)):
        product.append(list_numbers[i]*list_numbers[-i-1])
    return product


try:
    list_numbers = list(int(i) for i in (
        input('\nEnter numbers separated by a space:\t').split()))
    print('\nResulting list of numbers -->\t', list_numbers)
    print(
        f'\nProduct of pairs -->\t{product_of_pairs(list_numbers)}\n')
except ValueError:
    print('Incorrect data! You must enter number, try again!')
