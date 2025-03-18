#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 100) representing the number of test cases, and a list of tuples, each containing an integer n (1 ≤ n ≤ 100) and a string s of length n with characters "U" and "D" only.
def func_1():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n = int(data[index])
        
        s = data[index + 1]
        
        index += 2
        
        count_u = s.count('U')
        
        if count_u % 2 == 1:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: The loop has completed all its iterations. `index` is now equal to `2 * t + 1`. The values of `t` and `data` remain unchanged. For each iteration, the loop has read an integer `n` and a string `s` from `data`, incremented `index` by 2, counted the occurrences of 'U' in `s`, and printed 'YES' if the count is odd or 'NO' if the count is even.
#Overall this is what the function does:The function reads from standard input a series of test cases, where each test case consists of an integer `n` and a string `s` of length `n` containing only the characters "U" and "D". For each test case, it counts the occurrences of "U" in the string `s`. If the count is odd, it prints 'YES'; if the count is even, it prints 'NO'. After processing all test cases, the function does not return any value. The state of the program after the function concludes includes the completion of all iterations, with the `index` variable equal to `2 * t + 1`, and the `t` and `data` variables remaining unchanged.

