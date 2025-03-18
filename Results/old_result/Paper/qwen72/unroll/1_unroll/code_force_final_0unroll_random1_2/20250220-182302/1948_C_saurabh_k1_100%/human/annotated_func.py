#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an even integer such that 2 ≤ n ≤ 2 · 10^5, and the sum of n over all test cases does not exceed 2 · 10^5. The second and third lines of each test case are strings of length n, containing only the characters '<' and '>', representing the arrows in the first and second rows of the grid, respectively.
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
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n`, `a`, and `b` from input. After processing, it prints 'No' if any of the conditions in the inner loop are met, otherwise it prints 'Yes'. The variables `t`, `n`, `a`, and `b` are not retained between iterations, so their final values are not defined. The sum of `n` over all test cases does not exceed 2 · 10^5, and the loop completes without altering the initial constraints on `t` and `n`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an even integer `n` and two strings `a` and `b` of length `n`, containing only the characters '<' and '>'. It checks if there is any position `i` (where `i` is odd) such that either `a[i]` and `b[i + 1]` are both '<' or `a[i]` and `b[i - 1]` are both '<'. If such a position is found, it prints 'No' and moves to the next test case. If no such position is found, it prints 'Yes'. The function does not retain any state between test cases, and the variables `t`, `n`, `a`, and `b` are reinitialized for each test case. The function completes without altering the initial constraints on `t` and `n`.

