#State of the program right berfore the function call: The input consists of four lines, each containing four integers representing the state of the traffic lights (l, s, r, p) for each of the four road parts in a counter-clockwise order. The possible values for each light are 0 for red and 1 for green.
def func():
    traffic_lights = []
    for _ in range(4):
        traffic_lights.append(list(map(int, input().split())))
        
    #State of the program after the  for loop has been executed: Let's analyze the given Python loop and the provided initial state and output states step-by-step.
    #
    #### Step 1: Analyze the Code and Initial State
    #
    #The loop is defined as follows:
    #```python
    #for _ in range(4):
    #    traffic_lights.append(list(map(int, input().split())))
    #```
    #
    #**Initial State:** `traffic_lights` is an empty list.
    #
    #### Step 2: Track Variable Changes
    #
    #- **Variable `traffic_lights`:** This list will be modified in every iteration of the loop.
    #- **Variable `_`:** This is a loop variable used to track the iteration count. It starts from 0 and increments by 1 with each iteration.
    #- **Input from `input().split()`:** This part of the code takes input from the user, splits it into a list of strings, and then converts each string to an integer using `map(int, ...)`. The resulting list is appended to `traffic_lights`.
    #
    #### Step 3: Summarize the Loop Behavior
    #
    #- The loop runs exactly 4 times regardless of the input.
    #- In each iteration, a new list of integers is appended to `traffic_lights`.
    #- Since the loop always runs 4 times, `traffic_lights` will contain exactly 4 lists, each created from the input provided in each iteration.
    #
    #### Step 4: Verify Relationships
    #
    #- After the loop completes, `traffic_lights` will have 4 elements, each being a list of integers.
    #- The loop variable `_` will be 3 after the loop finishes because it increments from 0 to 3.
    #- Each of the 4 lists in `traffic_lights` corresponds to the input provided in each of the 4 iterations.
    #
    #### Final Output State
    #
    #After all 4 iterations of the loop, `traffic_lights` will contain 4 lists, each created from the input provided in each iteration. Therefore, the final output state is:
    #
    #Output State: `traffic_lights` is `[[], [], [], []]` if no input was provided in any of the 4 iterations. However, in practice, since the problem states that the loop executes and appends lists, we can generalize the final state as containing 4 lists of integers, regardless of their content.
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
        
    #State of the program after the  for loop has been executed: `accident_possible` is True, `i` is 3, `j` is 2, `l` is 1, `s` is 1, `r` is 1, `p` is 1.
    if accident_possible :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`accident_possible` is True, `i` is 3, `j` is 2, `l` is 1, `s` is 1, `r` is 1, `p` is 1, and either 'YES' is printed or the values remain unchanged based on the condition of `accident_possible`.
#Overall this is what the function does:The function `func` accepts no direct parameters but processes input consisting of four lines, each containing four integers representing the state of the traffic lights (l, s, r, p) for each of the four road parts in a counter-clockwise order. The possible values for each light are 0 for red and 1 for green. After processing the input, the function checks whether an accident is possible based on the current traffic light states. An accident is considered possible if any of the following conditions are met:
1. Any of the lights (l, s, r, p) are red while another light is green.
2. A green light (p) is followed by two other green lights (l and s or s and r or r and l).

If an accident is possible, the function prints 'YES'; otherwise, it prints 'NO'. The final state of the program includes the value of `accident_possible`, which is either True or False, and the loop variables `i` and `j` that are set during the last iteration of the inner loop.

