#State of the program right berfore the function call: n is a positive integer, k is a positive integer, PB and PS are integers such that 1 <= PB, PS <= n, p is a list of integers representing a permutation of length n where 1 <= p[i] <= n, and a is a list of integers of length n where 1 <= a[i] <= 10^9.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns the string 'Bodya'.
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns 'Sasha'
        else :
            return 'Draw'
            #The program returns 'Draw'
#Overall this is what the function does:The function `func_1` accepts parameters `n`, `k`, `PB`, `PS`, `p`, and `a`. It calculates the scores for two players, Bodya and Sasha, based on their positions `PB` and `PS` respectively. The function returns 'Bodya' if Bodya's score is greater than Sasha's score, 'Sasha' if Sasha's score is greater than Bodya's score, and 'Draw' if both scores are equal. The function does not modify any of its input parameters.

#State of the program right berfore the function call: start_pos is an integer such that 1 <= start_pos <= n, where n is the length of the permutation p and the array a.
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
        
    #State: - After the loop finishes, `steps` will be equal to `k` or the loop will break if a cycle is detected.
    #   - `score` will be the sum of the values from `a` that were added during the loop.
    #   - `visited` will contain the positions visited and the step at which they were visited.
    #   - `cycle_start` will be set to the step where the cycle was first detected, or it will remain -1 if no cycle is detected.
    #   - `current_pos` will be the last position visited before the loop breaks or completes.
    #
    #Given this, the output state can be described as:
    #
    #Output State:
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: `cycle_score` will be the sum of the values from `a` that were added during the loop, `cycle_pos` will be the position where the cycle ends (which is the same as the starting position of the cycle, `current_pos`), `steps`, `score`, `visited`, and `cycle_start` will remain unchanged, and `cycle_length` will remain the same.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: `score` is updated to `score + full_cycles * cycle_score + sum of the values from `a` that were added during the `remainder_steps` iterations, `current_pos` is the position after `remainder_steps` iterations, `steps` is `steps + remainder_steps`, `remaining_steps` is `0`, `full_cycles` is `remaining_steps // cycle_length`, `remainder_steps` is `remaining_steps % cycle_length`. The values of `visited`, `cycle_start`, and `cycle_length` remain unchanged.
    #State: *`steps` will be equal to `k` or the loop will break if a cycle is detected. `score` will be the sum of the values from `a` that were added during the loop. If a cycle is detected (`cycle_start` is not -1), `score` is updated to `score + full_cycles * cycle_score + sum of the values from `a` that were added during the `remainder_steps` iterations`, `current_pos` is the position after `remainder_steps` iterations, `steps` is `steps + remainder_steps`, and `remaining_steps` is `0`. The values of `visited`, `cycle_start`, and `cycle_length` remain unchanged. If no cycle is detected (`cycle_start` is -1), `score`, `current_pos`, `steps`, `visited`, `cycle_start`, and `cycle_length` retain their values from the loop.
    return score
    #The program returns the final value of `score`. If a cycle is detected (`cycle_start` is not -1), `score` is updated to `score + full_cycles * cycle_score + sum of the values from `a` that were added during the `remainder_steps` iterations`. If no cycle is detected (`cycle_start` is -1), `score` retains its value from the loop.
#Overall this is what the function does:The function `calculate_score` accepts an integer `start_pos` and returns an integer `score`. It calculates the score by summing up elements from the array `a` based on a sequence of positions determined by the permutation `p`, starting from `start_pos`. If a cycle is detected in the permutation, the function adjusts the score to account for the full cycles and any remaining steps. The final state of the program is that `score` reflects the total sum of the values from `a` that were added during the specified number of steps `k`, considering any cycles in the permutation.

#State of the program right berfore the function call: This function does not take any parameters, but it reads input from stdin. The input is expected to be formatted such that the first integer t (1 ≤ t ≤ 10^4) represents the number of test cases. For each test case, the next integers n, k, PB, PS (1 ≤ PB, PS ≤ n ≤ 2·10^5, 1 ≤ k ≤ 10^9) represent the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively. The following n integers represent the permutation p, and the next n integers represent the array a, where 1 ≤ p_i ≤ n and 1 ≤ a_i ≤ 10^9.
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
        
    #State: `index` is 1 + 4 * t + 2 * n * t, `t` is the same as the initial value, `results` is a list containing `t` elements, each element being the result of the function `func_1` for each iteration.
    for result in results:
        print(result)
        
    #State: `index` remains 1 + 4 * t + 2 * n * t, `t` remains the same as the initial value, and `results` is a list containing `t` elements, each element being the result of the function `func_1` for each iteration.
#Overall this is what the function does:The function reads input from stdin, processes multiple test cases, and prints the results. Each test case involves a permutation and an array, along with game parameters. The function determines whether Bodya can win the game for each test case and prints the results in the order of the test cases. After the function concludes, `index` is 1 + 4 * t + 2 * n * t, `t` remains the same as the initial value, and `results` is a list containing `t` elements, each element being the result of the function `func_1` for each iteration.

