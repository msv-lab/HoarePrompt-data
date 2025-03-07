#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n is an integer such that 1 <= n <= 100, and s is a string of length n containing only the characters "U" and "D".
def func_1():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        s = data[index]
        
        index += 1
        
        num_up_coins = s.count('U')
        
        if num_up_coins % 2 == 1:
            results.append('YES')
        else:
            results.append('NO')
        
    #State: `t` is the same as `int(data[0])`, `n` is the value from the last test case, `s` is the string from the last test case, `index` is `1 + 2*t`, `results` is a list of 'YES' or 'NO' based on the number of 'U' characters in each test case string.
    for result in results:
        print(result)
        
    #State: `t` is the same as `int(data[0])`, `n` is the value from the last test case, `s` is the string from the last test case, `index` is `1 + 2*t`, `results` is a list of 'YES' or 'NO' based on the number of 'U' characters in each test case string. The elements of `results` have been printed.
#Overall this is what the function does:The function reads multiple test cases from standard input. Each test case consists of an integer `n` and a string `s` of length `n` containing only the characters "U" and "D". For each test case, it determines if the number of "U" characters in the string is odd. If it is, the function prints "YES"; otherwise, it prints "NO".

