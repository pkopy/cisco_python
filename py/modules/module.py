# print("I like to be a module.")
# print(__name__)

#!/usr/bin/env python3
__counter = 0

def sum1(list):
    global __counter
    __counter += 1
    sum = 0
    for elem in list:
        sum += elem
    return sum

def prod1(list):
    global __counter
    __counter += 1
    prod = 1
    for elem in list:
        prod *= elem
    return prod

if __name__ == '__main__':
    print('I prefer to be a module, but I can do some tests for you')
    l = [i+1 for i in range(5)]
    print(sum1(l) == 15)
    print(prod1(l) == 120)