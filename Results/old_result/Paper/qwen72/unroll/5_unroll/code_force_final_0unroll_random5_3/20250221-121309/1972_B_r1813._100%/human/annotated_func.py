#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 100) representing the number of test cases, and a list of tuples, each containing an integer n (1 ≤ n ≤ 100) and a string s of length n consisting of "U" and "D" characters, representing the number of coins and their initial states, respectively.
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
        
    #State: The value of `t` remains unchanged. The value of `index` is `1 + 2 * t`. The loop has processed all `t` test cases, and for each test case, it has printed 'YES' if the count of 'U' characters in the string `s` is odd, and 'NO' otherwise.
#Overall this is what the function does:The function `func_1` reads input from `sys.stdin`, processes `t` test cases, where `t` is an integer (1 ≤ t ≤ 100). For each test case, it takes an integer `n` (1 ≤ n ≤ 100) and a string `s` of length `n` consisting of "U" and "D" characters. The function then prints 'YES' if the count of 'U' characters in `s` is odd, and 'NO' otherwise. After processing all test cases, the value of `t` remains unchanged, and the value of `index` is `1 + 2 * t`. The function does not return any value.

