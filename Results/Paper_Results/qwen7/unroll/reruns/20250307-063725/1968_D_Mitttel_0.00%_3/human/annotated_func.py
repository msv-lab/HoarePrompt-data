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
#Overall this is what the function does:The function accepts parameters n, k, PB, PS, p, and a. It calculates scores for PB and PS based on the lists p and a. If Bodya's score is higher, it returns 'Bodya'. If Sasha's score is higher, it returns 'Sasha'. If both scores are equal, it returns 'Draw'.

#State of the program right berfore the function call: start_pos is an integer representing the starting position (either P_B or P_S), n is the length of the permutation and is an integer, k is the duration of the game and is an integer, p is a list of integers representing the permutation, and a is a list of integers representing the array a.
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
        
    #State: Output State: The output state will be a dictionary with the key 'score' and its value being the sum of elements in the array `a` at positions specified by the permutation `p` up to `k` steps, and a 'cycle_start' indicating the start of a cycle if one is detected during the loop.
    #
    #Explanation: During each iteration of the loop, the code updates the `score` by adding the element from `a` at the position indicated by `current_pos - 1`. It also keeps track of the `current_pos` using the permutation list `p` and increments the `steps` counter. If the `current_pos` has been visited before within the same loop (indicating a cycle), the loop breaks and returns the `score`. If the loop completes without finding a cycle and `steps` equals `k`, it returns the accumulated `score`. The `visited` dictionary records the step at which each position was first visited to detect cycles.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: Output State: `cycle_length` is the difference between `steps` and `cycle_start`, where `cycle_start` is not -1 indicating a cycle was detected; `cycle_score` is the sum of elements in the array `a` from `cycle_pos - 1 - cycle_length` to `cycle_pos - 1`; `cycle_pos` is equal to `p[cycle_pos - 1]`.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: full_cycles is full_cycles, remaining_steps is 0, cycle_length is cycle_length, cycle_score is cycle_score, cycle_pos is cycle_pos, score is score + full_cycles * cycle_score + sum(a[current_pos - 1] for _ in range(remainder_steps)), remainder_steps is 0
    #State: The output state is a dictionary with the key 'score' and its value being the sum of elements in the array `a` at positions specified by the permutation `p` up to `k` steps, and a 'cycle_start' indicating the start of a cycle if one is detected during the loop. If a cycle is detected, the `score` is updated by adding the sum of elements in `a` at the positions indicated by the cycle until the cycle ends. If no cycle is detected and the loop completes with `steps` equaling `k`, the `score` is the accumulated sum up to that point.
    return score
    #The program returns the score which is the sum of elements in the array `a` at positions specified by the permutation `p` up to `k` steps, and a 'cycle_start' indicating the start of a cycle if one is detected during the loop. If a cycle is detected, the `score` is updated by adding the sum of elements in `a` at the positions indicated by the cycle until the cycle ends. If no cycle is detected and the loop completes with `steps` equaling `k`, the `score` is the accumulated sum up to that point.
#Overall this is what the function does:The function calculates the score based on the permutation `p` and the array `a` up to `k` steps starting from `start_pos`. If a cycle is detected in the permutation during the process, it adjusts the score accordingly. The function returns the final score and, if a cycle is detected, the start position of the cycle. If no cycle is detected and the loop completes with `steps` equaling `k`, the returned score is the accumulated sum up to that point.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases; n is a positive integer such that 1 ≤ n ≤ 2 × 10^5; k is a positive integer such that 1 ≤ k ≤ 10^9; PB and PS are positive integers such that 1 ≤ PB, PS ≤ n; p is a list of n integers representing the permutation; a is a list of n integers representing the array a.
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
        
    #State: Output State: `index` is 4 + 4 * t, `t` is an integer obtained from `int(data[0])`, `results` is a list containing `t` elements, each element being the result of `func_1(n, k, PB, PS, p, a)` for the corresponding iteration.
    for result in results:
        print(result)
        
    #State: Output State: `index` is 4 + 4 * t, `t` is an integer obtained from `int(data[0])`, `results` is a list containing `t` elements, each element being the printed result of `func_1(n, k, PB, PS, p, a)` for the corresponding iteration.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads values for \( n \), \( k \), \( PB \), \( PS \), and two lists \( p \) and \( a \) of length \( n \). It then calls another function `func_1` with these parameters to compute a result. After processing all test cases, it prints the results for each test case.

