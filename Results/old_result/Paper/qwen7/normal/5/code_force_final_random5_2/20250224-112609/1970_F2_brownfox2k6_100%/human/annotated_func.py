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
                #State: `obj` is a list of two integers where the second element is increased by 1, because the direction `d` is 'R'.
            #State: `obj` is a list of two integers. If the direction `d` is 'L', the second element of `obj` is decremented by 1. If the direction `d` is 'R', the second element of `obj` is incremented by 1.
        #State: Postcondition: `obj` is a list of two integers. If the direction `d` is 'D', the first element of `obj` is increased by 1. If the direction `d` is 'L', the second element of `obj` is decremented by 1. If the direction `d` is 'R', the second element of `obj` is incremented by 1.
    #State: Postcondition: `obj` is a list of two integers. If the direction `d` is 'U', the first element of `obj` is decremented by 1. If the direction `d` is 'D', the first element of `obj` is increased by 1. If the direction `d` is 'L', the second element of `obj` is decremented by 1. If the direction `d` is 'R', the second element of `obj` is incremented by 1.
#Overall this is what the function does:The function accepts a list `obj` containing two integers representing a position on the field and a string `d` representing the direction of movement ('U', 'D', 'L', or 'R'). Depending on the direction, it updates the position by modifying the elements of `obj`. Specifically, if the direction is 'U', the first element of `obj` is decremented by 1; if the direction is 'D', the first element is incremented by 1; if the direction is 'L', the second element is decremented by 1; and if the direction is 'R', the second element is incremented by 1. The function returns the updated position `obj`.

#State of the program right berfore the function call: t is an integer representing the current time step in the game. player is a dictionary mapping player identifiers (e.g., 'R0', 'B0') to their current positions (as a list of two integers [x, y]), and blud is a list of positions (as a list of two integers [x, y]) representing the current positions of the Bludgers.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: `out` is a list containing keys of players whose positions matched any position in `blud` at least once during the loop iterations, `t` is an integer representing the final time step after all iterations, `player` is a dictionary where the positions of players that matched `blud` have been updated to `[-1, -1]`, and `blud` remains unchanged.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: Output State: The loop has executed all its iterations, meaning every player whose position matched any position in `blud` at least once during the loop iterations has been printed as 'ELIMINATED'. The variable `t` now represents the final time step after all iterations have completed. The variable `out` is empty because all players that needed to be eliminated have been processed. The variable `player` remains unchanged, with positions of players that matched `blud` set to `[-1, -1]`. The variable `blud` also remains unchanged.
    #
    #In natural language: After all iterations of the loop have finished, the output state shows that all players whose positions matched any position in `blud` have been eliminated and printed as such. The list `out` is now empty since no more players need to be processed. Variables `player` and `blud` remain in their original states.
#Overall this is what the function does:The function processes a game state at a specific time step `t`. It identifies players whose positions match any of the Bludger positions and marks them as eliminated by setting their positions to `[-1, -1]`. It then prints a message for each eliminated player indicating the time step and player identifier. After processing, it ensures that all players who matched Bludger positions have been eliminated and prints the final state. The function does not return any value.

