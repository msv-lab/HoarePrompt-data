#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case contains an integer n (2 ≤ n ≤ 2 \cdot 10^5) which is even, followed by two strings of length n consisting of '<' and '>' characters representing the arrows in the first and second rows of the grid, respectively. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: The loop has processed all `t` test cases. For each test case, it has determined whether the second last character of the string `b` is `'<'`. If it is, it prints `'No'`; otherwise, it prints `'Yes'`. The variables `t`, `n`, `a`, and `b` are no longer in their initial state as they have been updated through each iteration, but `t` has been decremented to 0, indicating all test cases have been processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an even integer `n` and two strings of length `n` containing '<' and '>' characters. For each test case, it checks if the second last character of the second string is '<'. If it is, the function outputs 'No'; otherwise, it outputs 'Yes'.

