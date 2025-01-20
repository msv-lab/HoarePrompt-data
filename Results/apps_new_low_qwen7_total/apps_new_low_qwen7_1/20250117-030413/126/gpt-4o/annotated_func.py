#State of the program right berfore the function call: The input consists of four lines, each containing four integers representing the state of the traffic lights (l, s, r, p) for each of the four parts of the intersection. The possible values for each light are 0 for red and 1 for green.
def func():
    traffic_lights = []
    for _ in range(4):
        traffic_lights.append(list(map(int, input().split())))
        
    #State of the program after the  for loop has been executed: Output State: `traffic_lights` is a list containing four lists of integers, each list representing the integers entered by the user in each iteration of the loop. The loop will execute exactly 4 times regardless of the input provided because the number of iterations is specified by the `range(4)` function. Therefore, `traffic_lights` will have exactly 4 elements, each being a list of integers entered by the user.
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
        
    #State of the program after the  for loop has been executed: `traffic_lights` is a list containing four lists of integers, `accident_possible` is `True` if any of the conditions described above are met, and `accident_possible` is `False` otherwise.
    if accident_possible :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`traffic_lights` is a list containing four lists of integers, and `accident_possible` is set to `True` if any of the conditions within the if block are met. Otherwise, `accident_possible` remains `False`.
#Overall this is what the function does:The function processes an input consisting of four lines, each containing four integers representing the state of the traffic lights (l, s, r, p) for each of the four parts of the intersection. It checks if there is a possibility of an accident based on the following conditions:
1. If the pedestrian light (p) is green (1), then if any of the left (l), straight (s), or right (r) traffic lights are also green, an accident is considered possible.
2. Additionally, if the pedestrian light is green and any adjacent traffic light in the next intersection segment is also green, an accident is considered possible.
The function outputs 'YES' if an accident is possible based on the given conditions, and 'NO' otherwise. The function does not accept any parameters and does not return any value; instead, it prints the result directly.

