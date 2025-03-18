#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
def func():
    tests = int(input())
    for i in range(tests):
        slength = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        no = True
        
        if c == a or c == b:
            no = False
            print('NO')
        else:
            for x in c:
                if x not in a and x not in b:
                    print('YES')
                    no = False
                    break
        
        if no:
            print('NO')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 20, `a`, `b`, and `c` are strings each consisting of exactly n lowercase Latin letters, `tests` is an input integer, and the loop has executed `tests` times. After each iteration, if `c` is equal to either `a` or `b`, the output is 'NO'. Otherwise, if `c` contains at least one character not present in either `a` or `b`, the output is 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three strings of equal length. For each test case, it determines if the third string contains at least one character not present in either of the first two strings. If such a character exists, it outputs 'YES'; otherwise, it outputs 'NO'.

