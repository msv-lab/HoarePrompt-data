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
        
    #State: After all iterations, the variables `t`, `tests`, `n`, `a`, `b`, and `c` retain their initial values. The loop processes each test case by reading inputs for `slength`, `a`, `b`, and `c`, and prints either 'YES' or 'NO' based on the conditions specified. The variable `no` is a boolean flag used within each iteration to determine if a 'NO' should be printed, but it does not affect the overall state outside the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three strings `a`, `b`, and `c` of equal length `n`. For each test case, it determines if there is at least one character in `c` that is not present in both `a` and `b`. If such a character exists, it prints 'YES'; otherwise, it prints 'NO'. The function does not modify the input values and performs this check independently for each test case.

