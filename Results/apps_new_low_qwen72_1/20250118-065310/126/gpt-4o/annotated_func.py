#State of the program right berfore the function call: Each of the four input lines contains four integers (l, s, r, p) representing the state of the traffic lights for each road part, where l, s, r, and p can be 0 (red light) or 1 (green light).
def func():
    traffic_lights = []
    for _ in range(4):
        traffic_lights.append(list(map(int, input().split())))
        
    #State of the program after the  for loop has been executed: `traffic_lights` is a list containing four sublists, each with four elements: the first sublist remains unchanged, the second sublist is the result of the second input, the third sublist is the result of the third input, and the fourth sublist is the result of the fourth input, `_` is 3. The loop executes 4 times as specified by the range(4).
    accident_possible = False
    for i in range(4):
        l, s, r, p = traffic_lights[i]
        
        if p == 1:
            if l == 1 or s == 1 or r == 1:
                accident_possible = True
                break
            for j in range(3):
                if traffic_lights[(i + j) % 4][j] == 1:
                    accident_possible = True
                    break
            if accident_possible:
                break
        
    #State of the program after the  for loop has been executed: `traffic_lights` is a list containing four sublists, each with four elements, `_` is 3, `i` is 3, `l` is the first element of the fourth sublist, `s` is the second element of the fourth sublist, `r` is the third element of the fourth sublist, `p` is the fourth element of the fourth sublist. If any of the conditions in the loop were met, `accident_possible` is True; otherwise, `accident_possible` remains False.
    if accident_possible :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`traffic_lights` is a list containing four sublists, each with four elements, `_` is 3, `i` is 3, `l` is the first element of the fourth sublist, `s` is the second element of the fourth sublist, `r` is the third element of the fourth sublist, `p` is the fourth element of the fourth sublist. If `accident_possible` is True, it remains True; otherwise, `accident_possible` remains False.
#Overall this is what the function does:The function `func` reads four lines of input, each containing four integers (l, s, r, p) representing the state of traffic lights for each road part, where each integer can be 0 (red light) or 1 (green light). The function checks for the possibility of an accident based on the following conditions:
- If the pedestrian light (p) is green (1), and any of the other lights (l, s, r) in the same road part are green (1), an accident is possible.
- If the pedestrian light (p) is green (1), and any of the corresponding lights (l, s, r) in the next three road parts are green (1), an accident is possible.

If an accident is possible, the function prints 'YES'; otherwise, it prints 'NO'. After the function executes, the state of the program includes:
- `traffic_lights` is a list of four sublists, each containing four integers.
- `accident_possible` is a boolean indicating whether an accident is possible.
- The input values are consumed and no longer available for further processing.

