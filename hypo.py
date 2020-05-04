c0 = int(input('Add a number '))

steps = 0
while True:
    if c0%2 == 0:
        c0 /=2
        steps += 1
        print(c0)
    elif c0 == 1:
        print('steps: ', steps)
        break
    elif 3 * c0 + 1 != 1:
        c0 = 3 * c0 + 1
        steps += 1
        print(c0)
