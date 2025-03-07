#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2·10^5, k is an integer such that 1 ≤ k ≤ 10^9, PB and PS are integers such that 1 ≤ PB, PS ≤ n, and p is a list of n integers representing a permutation, and a is a list of n integers where 1 ≤ a[i] ≤ 10^9 for all 0 ≤ i < n.
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
#Overall this is what the function does:The function accepts parameters n, k, PB, PS, p, and a. It calculates scores for PB and PS using the `calculate_score` function. Based on the comparison of these scores, the function returns either 'Bodya', 'Sasha', or 'Draw'.

#State of the program right berfore the function call: start_pos is an integer such that 1 <= start_pos <= n, k is an integer such that 1 <= k <= 10^9, n is an integer such that 1 <= n <= 2 * 10^5, a is a list of integers where 1 <= a_i <= 10^9, and p is a permutation of length n (1 <= p_i <= n).
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
        
    #State: Output State: The loop will either continue executing until `steps` equals `k`, or it will break out of the loop when a cycle is detected. If the loop completes all iterations without breaking, the final state will be as follows:
    #
    #- `score` will be the sum of elements in the list `a` from index `start_pos - 1` to `current_pos - 1` for each step taken within the loop.
    #- `steps` will be equal to `k`.
    #- `current_pos` will be the position after taking `k` steps according to the permutation `p`.
    #- `visited` will be a dictionary containing all positions visited during the loop, with their respective step counts.
    #- `cycle_start` will be `-1` unless a cycle is detected, in which case it will be set to the step count of the starting point of the cycle.
    #
    #If the loop breaks due to detecting a cycle, then:
    #
    #- `cycle_start` will be the step count at which the cycle began.
    #- The function will return the accumulated `score` up to the point where the cycle was detected.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: Output State: The `cycle_score` will be increased by the sum of the values of `a` from each position within the cycle, as determined by the permutation `p`. The `cycle_pos` will be updated to the final position within the cycle after all iterations. All other variables (`cycle_start`, `score`, `steps`, `current_pos`, `visited`, `cycle_length`) will remain unchanged from their last known state after the third iteration.
        #
        #In simpler terms, after the loop completes all its iterations, the total score accumulated within the cycle (as defined by the permutation `p`) will be added to `cycle_score`, and `cycle_pos` will reflect the end position of the cycle.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: All variables remain unchanged except `score` which is increased by the sum of `a[current_pos - 1]` for each iteration from `remainder_steps` down to 1, and `current_pos` is updated to the final value after executing the loop `remainder_steps` times.
    #State: If a cycle is detected, `cycle_start` will be the step count at which the cycle began, and the function will return the accumulated `score` up to the point where the cycle was detected. Otherwise, `score` will be increased by the sum of `a[current_pos - 1]` for each iteration from `remainder_steps` down to 1, and `current_pos` will be updated to the final value after executing the loop `remainder_steps` times, with all other variables remaining unchanged.
    return score
    #The program returns the accumulated score up to the point where the cycle was detected, if a cycle is detected; otherwise, it returns the updated score which is increased by the sum of a[current_pos - 1] for each iteration from remainder_steps down to 1.
#Overall this is what the function does:The function `calculate_score` accepts an integer `start_pos` and calculates a cumulative score based on the list `a` and the permutation `p`. It traverses the list `a` from `start_pos` to `current_pos` according to the permutation `p` for `k` steps. If a cycle is detected during traversal, it calculates the score contributed by the cycle and updates the total score accordingly. The function returns the final accumulated score.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases; n is a positive integer such that 1 ≤ n ≤ 2 * 10^5; k is a positive integer such that 1 ≤ k ≤ 10^9; PB and PS are positive integers such that 1 ≤ PB, PS ≤ n; p is a list of n integers representing the permutation, where each integer is between 1 and n inclusive; a is a list of n integers representing the array a, where each integer is between 1 and 10^9 inclusive.
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
        
    #State: Output State: `index` is `18 + 3 * n + 8 + 2 * n`, `PB` is an integer value from `data[index + 2]`, `k` is an integer value from `data[index + 1]`, `n` is an integer value from `data[1]`, `t` is 1, `results` is a list containing the return value of `func_1(n, k, PB, PS, p, a)` repeated three times, `PS` is now `int(data[index + 3])`, `p` is a list of integers extracted from `data` starting from `index - 3 * n` and having length `n`, `a` is a list of integers obtained by converting the slice of `data` from `index - 3 * n` to `index - 3 * n + 3 * n` into integers.
    #
    #This output state describes the final condition of the variables after the loop has executed all its iterations. The `index` variable will be at the position `18 + 3 * n + 8 + 2 * n` because it increments by 4 each iteration and by `2 * n` in total over 3 iterations. The `results` list will contain the return value of `func_1` three times since the loop appends the same result to the list in each iteration. The `PB`, `k`, `n`, `t`, `PS`, `p`, and `a` variables will reflect their values after the last iteration of the loop.
    for result in results:
        print(result)
        
    #State: The `results` list contains the return value of `func_1(n, k, PB, PS, p, a)` repeated nine times, `result` is the first element in the `results` list.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads specific inputs including integers n, k, PB, PS, and two lists p and a. It then calls another function `func_1` with these inputs and stores the result. After processing all test cases, it prints the results of `func_1` for each test case.

