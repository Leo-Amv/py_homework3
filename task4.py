# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


try:
    string = ''
    number = int(input('\nEnter number:\t'))
    while number != 0:
        string += str(number % 2)
        number = int(number/2)
    print(f'\nBinary number:\t{string[::-1]}\n')
except ValueError:
    print('Incorrect data! You must enter number, try again!')
