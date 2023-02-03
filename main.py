table_ = [['-'] * 3 for i in range(3)]

count = 0


def func_table(l):
    print(' ', '0', '1', '2')
    num = 0
    for i in l:
        print(num, *i)
        num += 1


def func_step():
    step = input('введите координаты х и y через пробел: ').split()
    if len(step) == 2:
        if step[0].isdigit() and step[1].isdigit():
            step = list(map(int, step))
            if 0 <= step[0] < 3 and 0 <= step[1] < 3:
                return step[0], step[1]
    else:
        return func_step()


while not any([table_[0][0] == table_[1][1] == table_[2][2] != '-',
               table_[0][2] == table_[1][1] == table_[2][0] != '-',
               table_[0][0] == table_[0][1] == table_[0][2] != '-',
               table_[1][0] == table_[1][1] == table_[1][2] != '-',
               table_[2][0] == table_[2][1] == table_[2][2] != '-',
               table_[0][0] == table_[1][0] == table_[2][0] != '-',
               table_[0][1] == table_[1][1] == table_[2][1] != '-',
               table_[0][2] == table_[1][2] == table_[2][2] != '-',
               count == 9]):
    func_table(table_)
    y, x = func_step()
    if table_[x][y] == '-':
        if count % 2:
            table_[x][y] = '0'
        else:
            table_[x][y] = 'X'
        count += 1
    else:
        print('Клетка занята')

if any([table_[0][0] == table_[1][1] == table_[2][2] == '0',
        table_[0][2] == table_[1][1] == table_[2][0] == '0',
        table_[0][0] == table_[0][1] == table_[0][2] == '0',
        table_[1][0] == table_[1][1] == table_[1][2] == '0',
        table_[2][0] == table_[2][1] == table_[2][2] == '0',
        table_[0][0] == table_[1][0] == table_[2][0] == '0',
        table_[0][1] == table_[1][1] == table_[2][1] == '0',
        table_[0][2] == table_[1][2] == table_[2][2] == '0']):
    print('Победитель - Нолик')
elif any([table_[0][0] == table_[1][1] == table_[2][2] == 'x',
          table_[0][2] == table_[1][1] == table_[2][0] == 'X',
          table_[0][0] == table_[0][1] == table_[0][2] == 'X',
          table_[1][0] == table_[1][1] == table_[1][2] == 'X',
          table_[2][0] == table_[2][1] == table_[2][2] == 'X',
          table_[0][0] == table_[1][0] == table_[2][0] == 'X',
          table_[0][1] == table_[1][1] == table_[2][1] == 'X',
          table_[0][2] == table_[1][2] == table_[2][2] == 'X']):
    print('Победитель - Крестик')
else:
    print('Ничья')
