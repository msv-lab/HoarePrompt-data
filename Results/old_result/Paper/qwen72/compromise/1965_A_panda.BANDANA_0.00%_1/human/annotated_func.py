#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains n integers (1 ≤ n ≤ 2·10^5) representing the number of stones in each pile for a test case. Each integer a_i in the inner lists satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop has finished executing all iterations. For each test case, if any pile contains exactly 1 stone, the output is "Bob". Otherwise, the output is "Alice". The variables `t`, `n`, `l`, `e`, and `m` are no longer in scope after the loop completes.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers from the input, representing the number of stones in each pile. The function then checks if any pile contains exactly 1 stone. If so, it prints "Bob" for that test case; otherwise, it prints "Alice". After processing all test cases, the function concludes without returning any value. The variables `t`, `n`, `l`, `e`, and `m` are no longer in scope after the function completes.

