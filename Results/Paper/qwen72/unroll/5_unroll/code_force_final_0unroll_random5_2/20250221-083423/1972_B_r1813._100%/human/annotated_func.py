#State of the program right berfore the function call: The function should take two parameters: an integer `n` (1 ≤ n ≤ 100) representing the number of coins, and a string `s` of length `n` containing only "U" and "D", representing the initial state of the coins.
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
        
    #State: The `t` variable remains unchanged, and `index` is now `t * 2 + 1`. The `n` and `s` variables are set to the last values read from the `data` list. The `count_u` variable is set to the count of 'U' in the last `s` string. The loop has printed 'YES' if the count of 'U' in each `s` string was odd, and 'NO' if it was even.
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and for each test case, it checks if the number of 'U' characters in a given string is odd. If the number is odd, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. After the function concludes, the `t` variable remains unchanged, and `index` is set to `t * 2 + 1`. The `n` and `s` variables are set to the last values read from the input, and `count_u` is set to the count of 'U' in the last `s` string.

