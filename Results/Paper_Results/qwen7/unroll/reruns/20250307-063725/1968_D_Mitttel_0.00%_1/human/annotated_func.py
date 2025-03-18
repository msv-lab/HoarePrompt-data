#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 × 10^5, k is an integer such that 1 ≤ k ≤ 10^9, PB and PS are integers such that 1 ≤ PB, PS ≤ n, and p is a list of n integers representing the permutation, and a is a list of n integers where each element is in the range 1 to 10^9.
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
#Overall this is what the function does:The function accepts parameters n, k, PB, PS, p, and a. It calculates scores for two individuals, Bodya and Sasha, based on their respective positions (PB and PS) in the permutation list p and the corresponding values in the list a. If Bodya's score is higher, the function returns 'Bodya'. If Sasha's score is higher, the function returns 'Sasha'. If both scores are equal, the function returns 'Draw'.

#State of the program right berfore the function call: start_pos is an integer such that 1 <= start_pos <= n, k is a positive integer, n is a positive integer such that 1 <= n <= 2*10^5, a is a list of integers where 1 <= a_i <= 10^9, and p is a permutation of integers from 1 to n.
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
        
    #State: Output State: The final value of `score` will be the sum of elements in the list `a` from the positions specified by the permutation `p` for `k` steps, or until a cycle is detected. If a cycle is detected, the `score` will be the sum of elements from the start of the cycle to the point where the cycle starts, plus the sum of elements for the remaining steps within the cycle.
    #
    #Explanation: The loop iterates up to `k` times, updating the `current_pos` based on the permutation `p` and accumulating the score by adding the value at `a[current_pos - 1]` to `score`. If the `current_pos` has been visited before (indicating a cycle), the loop breaks and the current `score` is returned. Otherwise, it continues to update the `visited` dictionary and increment the `steps` counter.
    if (cycle_start != -1) :
        cycle_length = steps - cycle_start
        cycle_score = 0
        cycle_pos = current_pos
        for _ in range(cycle_length):
            cycle_score += a[cycle_pos - 1]
            
            cycle_pos = p[cycle_pos - 1]
            
        #State: Output State: `cycle_score` is the sum of elements from `cycle_pos - cycle_length` to `cycle_pos - 1`, `cycle_length` is the same as the number of iterations in the loop, `current_pos` remains unchanged and is equal to `cycle_pos`, `cycle_pos` is updated to the position after completing all iterations in the loop, and `visited` dictionary includes all positions visited during the loop iterations. The `steps` counter is incremented by `cycle_length`.
        remaining_steps = k - steps
        full_cycles = remaining_steps // cycle_length
        remainder_steps = remaining_steps % cycle_length
        score += full_cycles * cycle_score
        for _ in range(remainder_steps):
            score += a[current_pos - 1]
            
            current_pos = p[current_pos - 1]
            
        #State: Output State: `remaining_steps` is updated to `remaining_steps % cycle_length`, `cycle_score` remains unchanged, `cycle_length` remains unchanged, `current_pos` is updated to `cycle_pos`, `cycle_pos` is updated to the position after completing all iterations in the loop, `visited` dictionary includes all positions visited during the loop iterations, and `score` is increased by `full_cycles * cycle_score`.
    #State: The final value of `score` is the sum of elements in the list `a` from the positions specified by the permutation `p` for `k` steps, or until a cycle is detected. If a cycle is detected, the `score` is the sum of elements from the start of the cycle to the point where the cycle starts, plus the sum of elements for the remaining steps within the cycle. If a cycle is not detected, `score` is updated by adding the sum of elements for each step according to the permutation `p`.
    return score
    #The program returns the score which is the sum of elements in the list 'a' from the positions specified by the permutation 'p' for 'k' steps, or until a cycle is detected. If a cycle is detected, the score is the sum of elements from the start of the cycle to the point where the cycle starts, plus the sum of elements for the remaining steps within the cycle. If a cycle is not detected, the score is updated by adding the sum of elements for each step according to the permutation 'p'.
#Overall this is what the function does:The function `calculate_score` accepts a starting position `start_pos` and computes a score by summing elements in the list `a` based on the permutation `p` for `k` steps. If a cycle is detected in the permutation sequence, the score includes the sum of elements from the start of the cycle to the point where the cycle starts, plus the sum of elements for the remaining steps within the cycle. If no cycle is detected, the score is the cumulative sum of elements for each step according to the permutation `p`. The function returns the final computed score.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases; n and k are positive integers such that 1 ≤ n ≤ 2 × 10^5 and 1 ≤ k ≤ 10^9; PB and PS are positive integers such that 1 ≤ PB, PS ≤ n; p is a list of n integers representing the permutation, where each integer is a distinct value from 1 to n; a is a list of n integers representing the array a, where each integer is a positive integer not exceeding 10^9.
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
        
    #State: Output State: `index` is 4 + 4 * t; `t` is `data[0]`; `results` is a list containing `t` elements where each element is the result of `func_1(n, k, PB, PS, p, a)` for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: index
#Overall this is what the function does:The function reads input data from standard input, processes it in multiple iterations based on the number of test cases, and calls another function `func_1` for each iteration to compute a result. It then stores these results in a list and prints each result. The function does not return any value.

