#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100) representing the number of test cases. Each test case consists of two lines: the first line contains an integer n (1 ≤ n ≤ 100) representing the number of coins, and the second line contains a string s of length n consisting only of "U" and "D", where "U" represents a coin facing up and "D" represents a coin facing down.
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
        
    #State: `data` is a list of strings where the first element `t` is `0`, `index` is `2 * t + 1` which is `1`, no further `n` or `s` are processed, and all test cases have been evaluated.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of coins and their orientations ("U" for up, "D" for down). For each test case, it determines if the number of coins facing up is odd, and prints "YES" if it is, otherwise "NO".

