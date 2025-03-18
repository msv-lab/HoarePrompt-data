#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2⋅10^5, k is an integer such that 1 ≤ k ≤ 10^9, PB and PS are integers such that 1 ≤ PB, PS ≤ n, and p is a list of n integers representing a permutation, and a is a list of n integers where 1 ≤ a_i ≤ 10^9.
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
#Overall this is what the function does:The function accepts parameters n, k, PB, PS, p, and a. It calculates scores for 'Bodya' and 'Sasha' based on the elements at indices PB and PS in the list p. If 'Bodya's score is higher, it returns 'Bodya'. If 'Sasha's score is higher, it returns 'Sasha'. If both scores are equal, it returns 'Draw'.

#State of the program right berfore the function call: start_pos is an integer representing the starting position (either P_B or P_S), n is an integer representing the length of the permutation, k is an integer representing the duration of the game, p is a list of integers representing the permutation, and a is a list of integers representing the array a.
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
        
    #State: The output state will be determined by the final value of `score`.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: Output State: `cycle_length` is `steps - cycle_start`, `cycle_start` is not equal to -1, `cycle_score` is the sum of elements in the array `a` from index `cycle_pos - 1 - cycle_length` to `cycle_pos - 1` with the indices wrapped around according to the array `p`, `cycle_pos` is `current_pos`.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: full_cycles is remaining_steps // cycle_length, cycle_length is steps - cycle_start, cycle_score is the sum of elements in the array a from index (cycle_pos - 1 - cycle_length) to (cycle_pos - 1) with the indices wrapped around according to the array p, cycle_pos is current_pos, remaining_steps is k - steps, remainder_steps is remaining_steps % cycle_length, score is score + full_cycles * cycle_score + sum of elements in the array a from index (current_pos - 1 - remainder_steps) to (current_pos - 1) with the indices wrapped around according to the array p.
    #State: Postcondition: `score` is the final value determined by the following rules:
    #- If `cycle_start` is not equal to -1, `full_cycles` is the number of complete cycles remaining, `cycle_length` is the length of the cycle, `cycle_score` is the sum of elements in the array `a` from index `(cycle_pos - 1 - cycle_length)` to `(cycle_pos - 1)` with indices wrapped around according to the array `p`, `cycle_pos` is the current position, `remaining_steps` is `k - steps`, `remainder_steps` is the remainder when `remaining_steps` is divided by `cycle_length`. The `score` is updated to `score + full_cycles * cycle_score +` the sum of elements in the array `a` from index `(current_pos - 1 - remainder_steps)` to `(current_pos - 1)` with indices wrapped around according to the array `p`.
    #- If `cycle_start` is equal to -1, no changes are made to `score`.
    return score
    #The program returns the final value of `score` as calculated by the given rules.
#Overall this is what the function does:The function accepts a starting position (`start_pos`) and calculates the score based on a series of steps and a permutation. If a cycle is detected during the steps, it accounts for the full cycles and the remainder steps within the cycle to compute the final score. The function returns the final calculated score.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases; n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9; PB and PS are positive integers such that 1 ≤ PB, PS ≤ n; p is a list of n integers representing the permutation; a is a list of n integers representing the array a.
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
        
    #State: `data` is a list of strings, `index` is 8 (since it starts from 2 and increments by 4 for each iteration), `t` is an integer from the list at position 0, `n`, `k`, `PB`, `PS`, `p`, and `a` are integers or lists of integers determined during each iteration, `results` is a list containing the results of calling `func_1` for each iteration.
    for result in results:
        print(result)
        
    #State: data is a list of strings, index is 8, t is an integer from the list at position 0, n, k, PB, PS, p, and a are integers or lists of integers determined during each iteration, results is a list containing the results of calling func_1 for each iteration, and no changes were made to the print statement inside the loop, so the loop simply prints each result in the results list without affecting any variables outside the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads values for \( n \), \( k \), \( PB \), \( PS \), a permutation list \( p \), and an array \( a \). It then calls another function `func_1` with these values and stores the result. After processing all test cases, it prints the results of `func_1` for each test case.

