#State of the program right berfore the function call: The function should accept two parameters: a positive integer n (1 ≤ n ≤ 100) representing the number of coins, and a string s of length n containing only "U" and "D" representing the initial state of the coins. The function should be called multiple times for different test cases, with the number of test cases t (1 ≤ t ≤ 100) provided.
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
        
    #State: The loop has completed all iterations. The variable `index` is now `1 + 2 * t`, where `t` is the number of test cases. The variables `n`, `s`, and `count_u` are not retained after the loop, as they are redefined in each iteration. The variable `data` remains unchanged.
#Overall this is what the function does:The function `func_1` reads input from standard input, processes multiple test cases, and prints 'YES' or 'NO' for each test case based on the initial state of the coins. Each test case consists of a positive integer `n` (1 ≤ n ≤ 100) and a string `s` of length `n` containing only "U" and "D". The function prints 'YES' if the number of "U" characters in `s` is odd, and 'NO' if it is even. After processing all test cases, the function does not return any value, and the variable `index` is `1 + 2 * t`, where `t` is the number of test cases. The input data remains unchanged.

