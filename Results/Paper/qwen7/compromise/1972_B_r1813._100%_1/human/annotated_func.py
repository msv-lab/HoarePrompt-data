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
        
    #State: Output State: t is an integer representing the number of iterations in the loop, n is a positive integer such that 1 ≤ n ≤ 100 for each iteration, s is a string of length n containing only "U" and "D" for each iteration, index is 1 + 2 * t, and the output consists of 'YES' or 'NO' printed for each iteration based on whether the count of 'U' in s is odd or even.
#Overall this is what the function does:The function processes multiple test cases where each case includes an integer `t` representing the number of iterations, followed by `t` pairs of integers `n` and strings `s`. For each pair, it counts the number of 'U' characters in the string `s`. If the count of 'U' is odd, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function outputs a series of 'YES' or 'NO' values corresponding to each case.

