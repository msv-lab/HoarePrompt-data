#State of the program right berfore the function call: The function `func` is expected to take input through a standard input mechanism (like reading from stdin) and not through function parameters. The input consists of multiple test cases. The first integer `t` (1 ≤ t ≤ 10^4) represents the number of test cases. For each test case, the first integer `n` (1 ≤ n ≤ 2·10^5) represents the number of piles, and the next line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5.
def func():
    t = int(input())
    for tc in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        maxsize = max(a)
        
        a.sort()
        
        mexsize = 1
        
        for sz in a:
            if sz == mexsize:
                mexsize = mexsize + 1
        
        if mexsize > maxsize:
            print('Alice' if mexsize % 2 == 0 else 'Bob')
        else:
            print('Alice' if mexsize % 2 == 1 else 'Bob')
        
    #State: The loop has finished executing all `t` iterations, and for each test case, the output is either 'Alice' or 'Bob' based on the conditions specified in the loop. The variables `t`, `n`, and `a` are no longer in their initial states, but the final state of `t` is 0 (since the loop has completed its iterations), and the values of `n` and `a` are undefined after the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case consists of an integer `n` representing the number of piles, followed by `n` integers representing the number of stones in each pile. For each test case, it determines and prints the winner ('Alice' or 'Bob') based on the following rules: If the smallest non-negative integer not present in the sorted list of pile sizes (MEX) is greater than the maximum pile size, the winner is 'Alice' if MEX is even, and 'Bob' if MEX is odd. If MEX is not greater than the maximum pile size, the winner is 'Alice' if MEX is odd, and 'Bob' if MEX is even. After processing all test cases, the function completes, and the variables `t`, `n`, and `a` are no longer in their initial states.

