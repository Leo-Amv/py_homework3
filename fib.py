def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def minusfib(fib):
    minfib = list.copy(fib)
    minfib[1::2] = (i*(-1) for i in minfib[1::2])
    return minfib[::-1]


fib = list()
zero = list()
zero.append(0)
try:
    k = int(input('\nEnter number k:\t'))

    for i in range(1, k+1):
        fib.append(fibonacci(i))

    print(f'\nFibonacci list: {minusfib(fib)+zero+fib}\n')
except ValueError:
    print('Incorrect data! You must enter number, try again!')
