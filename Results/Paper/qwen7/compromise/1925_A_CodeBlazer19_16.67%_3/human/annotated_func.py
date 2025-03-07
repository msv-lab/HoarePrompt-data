#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        s = ''
        
        for j in range(97, k + 97):
            s += chr(j)
        
        if k == 1:
            print(n * s)
        else:
            print((2 - (n == 1)) * s)
        
    #State: The loop has executed all its iterations, meaning `i` ranges from 0 to `t-1`. The variable `j` will end at `97 + t*96`, `k` is at least 102, and `s` is the string consisting of characters from ASCII values 97 to `97 + t*96`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( n \) and \( k \). It then generates a string \( s \) containing \( k \) consecutive lowercase letters starting from 'a'. If \( k \) equals 1, it prints \( n \) times the string \( s \); otherwise, it prints \( (2 - (n == 1)) \) times the string \( s \). After processing all test cases, the function does not return any value.

