#State of the program right berfore the function call: The function receives multiple test cases. For each test case, it is given an integer n (1 ≤ n ≤ 100) representing the number of coins, and a string s of length n consisting only of "U" and "D", where "U" indicates a coin is facing up and "D" indicates a coin is facing down.
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
        
    #State: `data` is unchanged, `t` is unchanged, `index` is `1 + 2 * t`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string `s` of length `n` containing 'U' and 'D'. For each test case, it checks if the number of 'U's in the string is odd. If it is, the function prints 'YES'; otherwise, it prints 'NO'.

