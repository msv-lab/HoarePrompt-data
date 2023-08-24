n = int(input())

# read the initial positions of the tanks
tanks = {}
for i in range(n):
    r, c = map(int, input().split())
    tanks[(r, c)] = i + 1

# check if there are any tanks to be moved
if len(tanks) == n:
    print(0)
else:
    # initialize counters for the number of moves and the list of moves
    moves = 0
    move_list = []

    # create a mapping from rows and columns to the tanks in them
    row_tanks = {i: set() for i in range(1, n + 1)}
    col_tanks = {i: set() for i in range(1, n + 1)}
    for pos, tank in tanks.items():
        r, c = pos
        row_tanks[r].add(tank)
        col_tanks[c].add(tank)

    # iterate through each row and column
    for i in range(1, n + 1):
        # if the row has more than one tank, move them all down
        if len(row_tanks[i]) > 1:
            for tank in row_tanks[i]:
                moves += 1
                move_list.append((tank, 'D'))
            # update the row and column mappings
            for tank in row_tanks[i]:
                row_tanks[i].remove(tank)
                row_tanks[i + 1].add(tank)
        # if the column has more than one tank, move them all down
        if len(col_tanks[i]) > 1:
            for tank in col_tanks[i]:
                moves += 1
                move_list.append((tank, 'D'))
            # update the row and column mappings
            for tank in col_tanks[i]:
                col_tanks[i].remove(tank)
                col_tanks[i + 1].add(tank)

    # print the number of moves and the move list
    print(moves)
    for move in move_list:
        print(move[0], move[1])