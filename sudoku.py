def addRow():
    list = []

    while len(list) < 9:
        x = input('Add number: ')
        lst = []
        if len(x) == 9:

            for char in x:
                if char.isdigit():
                    lst.append(int(char))
        else:
            print('ble')
            continue
        list.append(lst)

    print(list)
    return list

def checkSudoku():
    list = addRow()
    dicGlob =  {}
    for i in list:
        dic = {}
        for j in i:
            if j in dic:
                print('Noooo')
                return False
            else:
                dic[j] = 1
    for i in range(9):

        for j in range(9):
            if list[j][i] in dicGlob:
                dicGlob[list[j][i]] += 1
            else:
                dicGlob[list[j][i]] = 1
    print(dicGlob)
    for i in dicGlob.values():
        if i != 9:
            print('Sudoku No')
            return False



    '''TODO: check cross values'''
    crossDic ={}
    for i in range(9):

        if list[i][i] in crossDic:
            print('Sudoku NO')
            return False
#             crossDic[list[i][i]] += 1

        else:
            crossDic[list[i][i]] = 1
#      for i in range(8, 0):
#
#              if list[i][i] in crossDic:
#                  print('Sudoku NO')
#                  return False
#      #             crossDic[list[i][i]] += 1
#
#              else:
#                  crossDic[list[i][i]] = 1
    print('Sudoku OK')


if __name__ == '__main__':

    checkSudoku()