def simulate(number: str):
#     print(number.split())
    list = []
    for char in number:
        if char.isdigit():
            list.append(int(char))
        print(char)
    listOfDigits = [['###','# #', '# #', '# #','###'],['#','#','#', '#', '#'],['###','  #', '###', '#  ', '###'],['###','  #', '###', '  #', '###'],
    ['# #','# #', '###', '  #', '  #'], ['###','#  ', '###', '  #', '###'], ['###','#  ', '###', '# #', '###'], ['###','  #', '  #', '  #', '  #'],
    ['###','# #', '###', '# #', '###'], ['###','# #', '###', '  #', '###']
    ]

    for elem in range(5):
        for item in list:
            print(listOfDigits[item][elem], end = ' ')
        print()
    print(list)

simulate('0123456789')