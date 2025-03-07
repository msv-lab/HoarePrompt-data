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
                #State: `obj` is a list of two integers where the second element is incremented by 1, since the direction `d` is 'R'.
            #State: `obj` is a list of two integers. If the direction `d` is 'L', the second element of `obj` is decremented by 1. If the direction `d` is 'R', the second element of `obj` is incremented by 1.
        #State: Postcondition: `obj` is a list of two integers. If the direction `d` is 'D', the first element of `obj` is increased by 1. If the direction `d` is 'L', the second element of `obj` is decremented by 1. If the direction `d` is 'R', the second element of `obj` is incremented by 1.
    #State: Postcondition: `obj` is a list of two integers. If the direction `d` is 'U', the first element of `obj` is decreased by 1. If the direction `d` is 'D', the first element of `obj` is increased by 1. If the direction `d` is 'L', the second element of `obj` is decremented by 1. If the direction `d` is 'R', the second element of `obj` is incremented by 1.
#Overall this is what the function does:The function `func_1` accepts a list `obj` containing two integers representing a position on a field and a direction string `d` ('U', 'D', 'L', or 'R'). It updates the position in `obj` based on the direction specified and returns the updated position as a list of two integers. If the direction is not one of 'U', 'D', 'L', or 'R', it does not return an error message but simply updates the position according to the valid directions provided.

#State of the program right berfore the function call: t is an integer representing the current time (step) in the game. player is a dictionary where keys are player identifiers (format: R0, R1, ..., B0, B1, ...) and values are the current positions of the players (format: [x, y]). blud is a list of positions where the Bludger is currently located.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: All keys in the `player` dictionary where the value is `blud` will have their corresponding values changed to `[-1, -1]`. The `out` list will contain all the keys from `player` that had their values changed to `blud` during the loop's iterations.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: The `out` list contains all keys from the `player` dictionary that had their values changed to `blud` during the loop's iterations. Since the loop executed 3 times, there must be at least two elements in `out`.
#Overall this is what the function does:The function accepts an integer `t` representing the current time in the game, a dictionary `player` mapping player identifiers to their positions, and a list `blud` of Bludger positions. It identifies all players whose positions match the Bludger positions, marks them as eliminated by setting their positions to `[-1, -1]`, and prints a message indicating each eliminated player along with the current time `t`. After processing, the function does not return any value.

