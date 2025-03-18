#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2 * 10^5, k is an integer such that 1 <= k <= 10^9, PB and PS are integers such that 1 <= PB, PS <= n, p is a list of n integers representing a permutation of 1 to n, and a is a list of n integers where each element a_i is such that 1 <= a_i <= 10^9.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns the string 'Bodya'
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns the string 'Sasha'
        else :
            return 'Draw'
            #The program returns 'Draw'
#Overall this is what the function does:The function `func_1` accepts parameters `n`, `k`, `PB`, `PS`, `p`, and `a`. It calculates the scores for two players, Bodya and Sasha, based on the positions `PB` and `PS` in the permutation list `p` and the corresponding values in list `a`. The function returns 'Bodya' if Bodya's score is greater, 'Sasha' if Sasha's score is greater, and 'Draw' if both scores are equal. The function does not modify any of the input parameters.

#State of the program right berfore the function call: start_pos is a positive integer such that 1 <= start_pos <= n, where n is the length of the permutation p and the array a.
def calculate_score(start_pos):
    score = 0
    current_pos = start_pos
    steps = 0
    visited = {}
    cycle_start = -1
    while steps < k:
        if current_pos in visited:
            cycle_start = visited[current_pos]
            break
        
        visited[current_pos] = steps
        
        score += a[current_pos - 1]
        
        steps += 1
        
        if steps >= k:
            return score
        
        current_pos = p[current_pos - 1]
        
    #State: - `score = 60`
    #- `current_pos = 1`
    #- `steps = 3`
    #- `visited = {1: 0, 2: 1, 3: 2}`
    #- `cycle_start = 0`
    #
    #Output State:
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: score = 60, current_pos = 1, steps = 3, visited = {1: 0, 2: 1, 3: 2}, cycle_start = 0, cycle_length = 3, cycle_score = 6, cycle_pos = 1.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: score = 60 + (k - 3) // 3 * 6 + sum(a[i] for i in range(remainder_steps)), current_pos = p[remainder_steps % 3 - 1]
    #State: `score` is 60. If `cycle_start` is not -1, then `score` is updated to 60 + (k - 3) // 3 * 6 + sum(a[i] for i in range(remainder_steps)), and `current_pos` is updated to `p[remainder_steps % 3 - 1]`. If `cycle_start` is -1, `score` and `current_pos` remain unchanged. `steps` is 3, and `visited` is {1: 0, 2: 1, 3: 2}.
    return score
    #The program returns 60.
#Overall this is what the function does:The function `calculate_score` accepts a parameter `start_pos`, which is a positive integer within the range of 1 to n (inclusive), where n is the length of the permutation `p` and the array `a`. It calculates a score by traversing the permutation `p` and summing up the corresponding values in `a` for a total of `k` steps. If a cycle is detected during the traversal, the function computes the score for the remaining steps based on the cycle's length and score. The function returns the final score, which is not necessarily 60 and depends on the values in `a` and the structure of `p`.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads input from `sys.stdin` and processes it.
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        k = int(data[index + 1])
        
        PB = int(data[index + 2])
        
        PS = int(data[index + 3])
        
        index += 4
        
        p = list(map(int, data[index:index + n]))
        
        index += n
        
        a = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(n, k, PB, PS, p, a)
        
        results.append(result)
        
    #State: Output State: `index` is 1 + 4 * t + 2 * n * t. `t` is the integer value of the string at `data[0]`. `results` is a list containing `t` elements, each element being the result of `func_1(n, k, PB, PS, p, a)` for each iteration of the loop. `data` remains unchanged.
    for result in results:
        print(result)
        
    #State: The `index` remains 1 + 4 * t + 2 * n * t. `t` remains the integer value of the string at `data[0]`. `results` is a list containing `t` elements, each element being the result of `func_1(n, k, PB, PS, p, a)`. `data` remains unchanged.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it to extract multiple sets of parameters, and calls `func_1` for each set. It collects the results of these calls into a list and prints each result. After the function concludes, `index` is set to 1 + 4 * t + 2 * n * t, `t` is the number of test cases, and `results` is a list of `t` elements, each being the result of `func_1` for the corresponding test case. The input data remains unchanged.

