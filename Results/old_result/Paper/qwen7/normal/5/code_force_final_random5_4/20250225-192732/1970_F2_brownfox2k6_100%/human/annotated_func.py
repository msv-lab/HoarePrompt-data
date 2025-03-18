#State of the program right berfore the function call: obj is a list of two integers representing a coordinate (row, column) on the field, and d is a string representing the direction of movement ('U', 'D', 'L', or 'R').
def func_1(obj, d):
    if (d == 'U') :
        obj[0] -= 1
    else :
        if (d == 'D') :
            obj[0] += 1
        else :
            if (d == 'L') :
                obj[1] -= 1
            else :
                if (d == 'R') :
                    obj[1] += 1
                #State: obj is a list of two integers where the second element is increased by 1, and d is 'R'.
            #State: `obj` is a list of two integers. If `d` is 'L', the second element of `obj` is decreased by 1. If `d` is 'R', the second element of `obj` is increased by 1.
        #State: Postcondition: `obj` is a list of two integers representing a coordinate. If `d` is 'D', the first element of `obj` is increased by 1. If `d` is 'L', the second element of `obj` is decreased by 1. If `d` is 'R', the second element of `obj` is increased by 1.
    #State: Postcondition: `obj` is a list of two integers representing a coordinate. If `d` is 'U', `obj` is updated to (1, column). If `d` is 'D', the first element of `obj` is increased by 1. If `d` is 'L', the second element of `obj` is decreased by 1. If `d` is 'R', the second element of `obj` is increased by 1.
#Overall this is what the function does:The function accepts a coordinate `obj` (a list of two integers) and a direction `d` (a string). Based on the direction, it updates the coordinate by changing the row or column value accordingly. If the direction is 'U' or 'D', it modifies the row value; if 'L' or 'R', it modifies the column value. The function returns the updated coordinate. If the direction is invalid, it does not perform any action on the coordinate.

#State of the program right berfore the function call: t is an integer representing the current time step in the game. player is a dictionary mapping player identifiers (e.g., 'R0', 'B0') to their current positions (a list of two integers [x, y]). blud is a list of positions (a list of two integers [x, y]) representing the current positions of the Bludgers on the field.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: The list `out` contains all player identifiers `p` for which `player[p]` was equal to `blud` at any point during the loop's execution. The variable `t` remains an integer. The dictionary `player` no longer contains any keys whose value was `blud` before being set to `[-1, -1]`.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: The loop will continue to execute until `out` is empty. During each iteration, the smallest element in `out` (which is not yet eliminated) is processed. After all iterations, `out` will be empty, and `t` will be incremented for each player in `out`.
#Overall this is what the function does:The function processes a game scenario at a given time step `t`. It identifies players whose positions match the current positions of the Bludgers, marks them as eliminated by setting their positions to `[-1, -1]`, and prints a message for each eliminated player indicating the time step and player identifier. After processing, the function ensures that no players remain in the `player` dictionary with positions matching the Bludgers.

