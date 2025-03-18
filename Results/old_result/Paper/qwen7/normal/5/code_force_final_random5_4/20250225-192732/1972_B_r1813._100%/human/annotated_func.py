#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D".
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
        
    #State: Output State: `t` is an integer equal to `data[0] - 3`, `count_u` is the number of 'U' in the final string `s`, `n` is now `int(data[index + 4])`, `s` is now `data[index + 3]`, and `index` is increased by 6 for each iteration, ending at `index` being increased by 6 * 3 = 18.
    #
    #In natural language, after the loop has executed all its iterations, `t` will be reduced by 3, reflecting the number of times the loop has run. The value of `count_u` will be the total number of 'U' characters in the final string `s` after all iterations. The variable `n` will be set to `int(data[6])` (since `index` starts at 1 and increases by 6 each time), and `s` will be `data[6]`. The variable `index` will be increased by 18 in total, aligning with the pattern of increasing by 6 for each of the 3 iterations.
#Overall this is what the function does:The function processes multiple test cases from standard input. Each test case consists of a positive integer \( t \) indicating the number of cases to process, followed by a positive integer \( n \) and a string \( s \) of length \( n \) containing only "U" and "D". For each test case, the function counts the number of 'U' characters in the string \( s \). If the count of 'U' characters is odd, the function prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function implicitly reduces the value of \( t \) by 3, reflecting the number of test cases processed.

