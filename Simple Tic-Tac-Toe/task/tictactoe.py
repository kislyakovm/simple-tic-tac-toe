x = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
queue = 'X'

print('''---------
|       |
|       |
|       |
---------''')


def winner():
    players = ['X', 'O']
    for player in players:
        for i in range(3):
            new_list = [True if x[i][j] == player else False for j in range(3)]
            if all(new_list):
                print(player, 'wins')
                return True

        for j in range(3):
            new_list = [True if x[i][j] == player else False for i in range(3)]
            if all(new_list):
                print(player, 'wins')
                return True

        if x[0][0] == x[1][1] == x[2][2] == player:
            print(player, 'wins')
            return True
        elif x[0][2] == x[1][1] == x[2][0] == player:
            print(player, 'wins')
            return True


def is_more_than_three(i, j):
    if int(i) > 3 or int(j) > 3:
        print('Coordinates should be from 1 to 3!')
        return True


def is_not_integer(i, j):
    try:
        int(i) and int(j)
    except:
        print('You should enter numbers!')
        return True


def is_cell_occupied(i, j):
    if x[i - 1][j - 1] != ' ':
        print('This cell is occupied! Choose another one!')
        return True


def write_to_cell(i, j):
    global queue
    if queue == 'X':
        x[i - 1][j - 1] = 'X'
        queue = 'O'
    else:
        x[i - 1][j - 1] = 'O'
        queue = 'X'


def print_grid():
    print(f'''---------
| {x[0][0]} {x[0][1]} {x[0][2]} |
| {x[1][0]} {x[1][1]} {x[1][2]} |
| {x[2][0]} {x[2][1]} {x[2][2]} |
---------''')


def is_draw():
    if ' ' not in x[0] and ' ' not in x[1] and ' ' not in x[2]:
        print('Draw')
        return True


def input_coordinates():
    while True:
        i, j = input('Enter the coordinates: ').split()

        if is_not_integer(i, j):
            continue

        if is_more_than_three(i, j):
            continue

        i = int(i)
        j = int(j)

        if is_cell_occupied(i, j):
            continue

        write_to_cell(i, j)

        print_grid()

        if winner():
            return

        if is_draw():
            return


input_coordinates()
