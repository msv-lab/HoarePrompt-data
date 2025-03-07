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
        
    #State: The output consists of 'YES' or 'NO' printed based on whether the count of 'U' characters in each substring of `data` starting from `data[index]` and having length `n` is odd. The total number of lines printed is equal to `t`.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \) (1 ≤ \( t \) ≤ 100), and for each test case, a positive integer \( n \) (1 ≤ \( n \) ≤ 100) and a string \( s \) of length \( n \) consisting of "U" and "D". It checks if the count of "U" characters in \( s \) is odd and prints "YES" if true, otherwise "NO". The function outputs the result for each test case, totaling \( t \) lines of output.

