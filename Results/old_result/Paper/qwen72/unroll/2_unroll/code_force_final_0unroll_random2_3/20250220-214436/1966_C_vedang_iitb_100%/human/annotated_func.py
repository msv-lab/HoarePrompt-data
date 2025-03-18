#State of the program right berfore the function call: The function should take two parameters: `t` (an integer representing the number of test cases, where 1 ≤ t ≤ 10^4) and `test_cases` (a list of tuples, where each tuple contains an integer `n` (1 ≤ n ≤ 2·10^5) and a list of integers `a` (1 ≤ a_i ≤ 10^9) representing the number of piles and the initial number of stones in each pile, respectively). The sum of `n` over all test cases does not exceed 2·10^5.
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
        
    #State: The variable `t` is unchanged, and the list `test_cases` is also unchanged. The loop iterates `t` times, processing each test case and printing either 'Alice' or 'Bob' based on the conditions specified in the loop. The internal variables `n`, `a`, `maxsize`, and `mexsize` are updated and used within each iteration but do not persist outside the loop.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of integers `a` from the input, processes the list to determine a winner ('Alice' or 'Bob') based on the conditions specified in the loop, and prints the result. The function does not return any value; it only prints the results for each test case. The internal variables used for processing each test case do not persist outside the loop, and the function does not modify the input variables `t` or `test_cases`.

