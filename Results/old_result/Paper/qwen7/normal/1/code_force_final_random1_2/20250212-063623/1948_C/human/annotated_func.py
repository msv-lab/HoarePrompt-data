#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; the first line of each test case contains a string of length n consisting of characters "<" and/or ">"; the second line of each test case contains a string of length n consisting of characters "<" and/or ">".
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: Output State: The loop completes all iterations and prints 'yes'.
    #
    #In natural language, the output state after the loop executes all its iterations is: **If the loop completes without breaking (i.e., none of the specified conditions are met for any `i`), the output will be 'yes'.**
#Overall this is what the function does:The function processes a series of test cases, each containing two strings of equal even length consisting of "<" and ">". For each test case, it checks if there exists an index `i` (where `i` is odd) such that either `a[i] == b[i+1] == '<'` or `a[i] == b[i-1] == '<'`. If such an index is found, it prints "No" and stops processing further. If no such index is found after checking all possible indices, it prints "Yes".

