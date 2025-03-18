#State of the program right berfore the function call: The function `func` is expected to take input from the standard input, where the first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case consists of two lines: the first line contains an integer n (1 ≤ n ≤ 2 · 10^5) representing the length of the lost string, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the trace of the string. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: The loop has finished executing all iterations, and the output state is as follows:
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` and a list of `n` integers representing a trace. For each test case, the function constructs a string by mapping each integer in the trace to a character based on its position in the alphabet (starting from 'a'). The function then prints the constructed string for each test case. After processing all test cases, the function completes and no further output is generated.

