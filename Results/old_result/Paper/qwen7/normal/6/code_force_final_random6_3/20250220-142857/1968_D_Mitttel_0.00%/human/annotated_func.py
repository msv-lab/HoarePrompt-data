#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2⋅10^5, k is an integer such that 1 ≤ k ≤ 10^9, PB and PS are integers such that 1 ≤ PB, PS ≤ n, and p is a list of n integers representing the permutation, and a is a list of n integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns 'Bodya'
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns 'Sasha'
        else :
            return 'Draw'
            #The program returns 'Draw'
#Overall this is what the function does:The function accepts parameters n, k, PB, PS, p, and a. It calculates scores for 'Bodya' and 'Sasha' based on the elements at indices PB and PS in the list p. Depending on which score is higher, it returns either 'Bodya', 'Sasha', or 'Draw'.

#State of the program right berfore the function call: start_pos is an integer such that 1 <= start_pos <= n, n and k are positive integers with 1 <= P_B, P_S <= n and 1 <= k <= 10^9, p is a list of n integers representing the permutation, and a is a list of n integers where each element is between 1 and 10^9 inclusive.
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
        
    #State: Output State: `score` is the sum of elements in the list `a` from index `start_pos - 1` to `end_pos - 1` (inclusive), `current_pos` is the position after the last jump, `steps` is equal to `k`, `visited` is a dictionary containing all positions visited during the loop with their corresponding step numbers, and `cycle_start` is -1 if no cycle was detected or the step number where the cycle started if a cycle was detected.
    #
    #This output state assumes that the loop completes all its iterations without detecting a cycle and that `k` is large enough to allow the loop to execute until its termination condition (`steps >= k`). The `score` accumulates the values from the list `a` based on the positions traversed by `current_pos`.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: After the loop executes all its iterations, `cycle_pos` will be updated to the final position determined by repeatedly applying `p[cycle_pos - 1]` for `cycle_length` times. `cycle_score` will be the sum of `a[cycle_pos - 1]` for each iteration plus the original `score`. The `score` itself, `current_pos`, `steps`, and the `visited` dictionary will remain unchanged. The `cycle_length` will also remain as it was initialized.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: Output State: `full_cycles` is `remaining_steps // cycle_length`, `remaining_steps` is `k - steps - remainder_steps`, `cycle_pos` remains unchanged, `cycle_score` remains unchanged, `score` is `score + remainder_steps * a[current_pos - 1]`, `current_pos` is updated to `p[current_pos - 1]` repeated `remainder_steps` times, `steps` remains unchanged, `visited` dictionary remains unchanged.
        #
        #In this final output state, the variable `full_cycles` remains the same as it was calculated before the loop started. The `remaining_steps` is reduced by the number of steps executed within the loop, which is equal to `remainder_steps`. The `score` is incremented by the sum of `a[current_pos - 1]` for each step within the loop, which is `remainder_steps` times. The `current_pos` is updated multiple times according to the rule `current_pos = p[current_pos - 1]` for each iteration of the loop. All other variables (`cycle_pos`, `cycle_score`, `steps`, `visited`) remain unchanged as they were not affected by the loop.
    #State: `score` is the sum of elements in the list `a` from index `start_pos - 1` to `end_pos - 1` (inclusive), `current_pos` is the position after the last jump, `steps` is equal to `k`, `visited` is a dictionary containing all positions visited during the loop with their corresponding step numbers, and `cycle_start` is -1 if no cycle was detected or the step number where the cycle started if a cycle was detected. If a cycle is detected (`cycle_start != -1`), `full_cycles` remains the same, `remaining_steps` is reduced by the number of steps executed within the loop, `score` is incremented by the sum of `a[current_pos - 1]` for each step within the loop, `current_pos` is updated multiple times according to the rule `current_pos = p[current_pos - 1]` for each iteration of the loop, and all other variables (`cycle_pos`, `cycle_score`, `steps`, `visited`) remain unchanged. If no cycle is detected, all variables remain as they were at the start of the loop.
    return score
    #The program returns the sum of elements in the list `a` from index `start_pos - 1` to `end_pos - 1` (inclusive)
#Overall this is what the function does:The function `calculate_score` accepts a parameter `start_pos`, which is an integer indicating the starting position in the lists `a` and `p`. It calculates the sum of elements in the list `a` from the index `start_pos - 1` to the position determined by following the permutation `p` for `k` steps. If a cycle is detected during the process, it accounts for the cycle to compute the final score. The function returns the total score as an integer.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases; n and k are positive integers such that 1 ≤ n ≤ 2 × 10^5 and 1 ≤ k ≤ 10^9; PB and PS are positive integers such that 1 ≤ PB, PS ≤ n; p is a list of n integers representing the permutation; a is a list of n integers representing the array a.
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
        
    #State: Output State: `index` is 17 + 3 * n + 4 + 2 * n + n, `t` is `t - 2`, `results` is a list containing the return values of `func_1(n, k, PB, PS, p, a)` for each iteration, `PB` is an integer from `int(data[index + 2])`, `k` is `int(data[index + 1])`, `PS` is an integer from `int(data[index + 3])`, `p` is a list of integers obtained by mapping each element in `data` from `index` to `index + n` converted to integers, and `a` is a list of integers obtained by mapping each element in `data` from `index` to `index + n` converted to integers.
    #
    #In this final state, after the loop has executed all its iterations, the `index` will have advanced by the total amount required for all iterations, which is 17 + 3 * n + 4 + 2 * n + n. The variable `t` will have been decremented by the number of iterations minus one (since it starts at the number of iterations and decreases by one each time). The `results` list will contain the return values from `func_1` for each iteration of the loop. The values of `PB`, `k`, and `PS` will be updated based on their positions in the `data` list after the last iteration, and `p` and `a` will be lists of integers derived from the `data` list as described.
    for result in results:
        print(result)
        
    #State: The index is 34, t is 0, results is a list containing the return values of func_1(n, k, PB, PS, p, a) for each iteration, PB is an integer from int(data[39]), k is int(data[38]), PS is an integer from int(data[40]), p is a list of integers obtained by mapping each element in data from index 34 to 34 + n converted to integers, and a is a list of integers obtained by mapping each element in data from index 34 to 34 + n converted to integers.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads in values for \( n \), \( k \), \( PB \), \( PS \), a permutation \( p \), and an array \( a \). It then calls another function `func_1` with these parameters to compute a result for each test case. After processing all test cases, it prints the results for each case.

