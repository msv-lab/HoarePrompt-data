#State of the program right berfore the function call: obj is a list of two integers representing a position on the field, and d is a string representing the direction of movement ('U', 'D', 'L', or 'R').
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
                #State: Postcondition: `obj` is a list of two integers where the second element is increased by 1, since the direction `d` is 'R' and there is no else part in the code.
            #State: Postcondition: `obj` is a list of two integers, where the second element is either reduced by 1 if the direction `d` is 'L', or increased by 1 if the direction `d` is 'R'.
        #State: Postcondition: `obj` is a list of two integers. If the direction `d` is 'D', the first element of `obj` is increased by 1. If `d` is 'L', the second element of `obj` is reduced by 1. If `d` is 'R', the second element of `obj` is increased by 1.
    #State: Postcondition: `obj` is a list of two integers. If the direction `d` is 'U', the first element of `obj` is decreased by 1. If `d` is 'D', the first element of `obj` is increased by 1. If `d` is 'L', the second element of `obj` is reduced by 1. If `d` is 'R', the second element of `obj` is increased by 1.
#Overall this is what the function does:The function `func_1` accepts a parameter `obj`, which is a list of two integers representing a position on the field, and a parameter `d`, which is a string representing the direction of movement ('U', 'D', 'L', or 'R'). Depending on the direction, it updates the position by moving up ('U'), down ('D'), left ('L'), or right ('R'). If the direction is not one of the specified ones, it does not change the position and returns the original position as a list of two integers.

#State of the program right berfore the function call: t is an integer representing the current time step in the game. player is a dictionary mapping player identifiers (strings like 'R0', 'B0') to their current positions (a list of two integers [x, y]). blud is a list of players who are currently in the same position as a Bludger.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: Output State: `out` is a list containing all player identifiers (strings like 'R0', 'B0') that were in the same position as a Bludger (`blud`), `t` is an integer representing the current time step in the game, `player` is a dictionary mapping player identifiers to their new positions, where players who were in the same position as a Bludger are now mapped to `[-1, -1]`.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: Output State: The variable `out` will contain a list of player identifiers (strings like 'R0', 'B0') that were in the same position as a Bludger (`blud`) at each time step `t`, and these players will be printed with the message "ELIMINATED" along with the current time step `t`. The variable `t` will be incremented for each iteration of the loop, and the dictionary `player` will map the eliminated players to `[-1, -1]`. All players that were in the same position as a Bludger at any time step will be listed in `out` and printed as eliminated.
#Overall this is what the function does:The function processes the game state at a given time step `t`. It identifies players who are in the same position as a Bludger (`blud`) and marks them as eliminated by setting their positions to `[-1, -1]`. It then prints a message indicating that these players have been eliminated along with the current time step `t`. The function returns a list `out` containing the identifiers of all eliminated players.

