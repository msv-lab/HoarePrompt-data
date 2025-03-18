#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `tests` is the number of iterations, `n` is an integer such that 1 ≤ n ≤ 20, `a`, `b`, and `c` are the strings from the last iteration, `slength` is the integer input from the last iteration, and `no` is True if `c` is neither equal to `a` nor `b` and all characters in `c` are in `a` and `b`. Otherwise, `no` is False.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it checks if a third string `c` is either equal to the first string `a` or the second string `b`, or if all characters in `c` are present in either `a` or `b`. For each test case, it prints 'YES' if `c` meets one of these conditions, otherwise it prints 'NO'.

