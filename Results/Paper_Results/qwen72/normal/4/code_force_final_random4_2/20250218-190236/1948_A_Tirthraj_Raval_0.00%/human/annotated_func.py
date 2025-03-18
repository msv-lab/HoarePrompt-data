#State of the program right berfore the function call: The function should accept a single integer n where 1 ≤ n ≤ 50, and return a string of uppercase Latin letters of length at most 200 with exactly n special characters, or "NO" if no such string exists.
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
        
    #State: `t` is 0, and for each iteration, if the input `n` was odd, the output was 'NO'. If `n` was even, the output was 'YES' followed by a string of alternating 'A' and 'B' characters, with the total length of the string being `n`.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `n` from the input. If `n` is odd, the function prints 'NO'. If `n` is even, the function prints 'YES' followed by a string of alternating 'A' and 'B' characters, with the total length of the string being `n`. After processing all test cases, the function concludes, and the state of the program is such that `t` is 0, and the output for each test case is either 'NO' or 'YES' followed by the specified string.

