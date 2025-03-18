#State of the program right berfore the function call: The function `func_1` does not take any parameters directly, but it is expected to read input from standard input. The input consists of multiple test cases. The first line of the input contains a single integer `t` (1 ≤ t ≤ 100), representing the number of test cases. For each test case, the first line contains an integer `n` (1 ≤ n ≤ 100), representing the number of coins. The second line contains a string `s` of length `n`, consisting only of the characters "U" and "D", where "U" represents a coin facing up and "D" represents a coin facing down.
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
        
    #State: t is 2, data is ['2', '5', 'UUNNU', '3', 'UUU'], index is 5.
#Overall this is what the function does:The function `func_1` reads multiple test cases from standard input. Each test case consists of an integer `n` and a string `s` of length `n` containing 'U' and 'D'. For each test case, it prints 'YES' if the count of 'U' in the string is odd, otherwise it prints 'NO'.

