#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each of the t test cases, n is an integer such that 1 ≤ n ≤ 50.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            print('YES')
            pattern = []
            for i in range(n // 2):
                pattern.append('AB'[i % 2])
                pattern.append('AB'[i % 2 ^ 1])
            print(''.join(pattern))
        
    #State: The loop will have executed `t` times, where `t` is the initial integer input by the user such that 1 ≤ t ≤ 50. For each of the `t` test cases, an integer `n` is input. If `n` is odd, the output is 'NO'. If `n` is even, the output is 'YES' followed by a string of length `n` consisting of alternating 'A' and 'B' characters, starting with 'A'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. If `n` is odd, it prints 'NO'. If `n` is even, it prints 'YES' followed by a string of length `n` consisting of alternating 'A' and 'B' characters, starting with 'A'.

