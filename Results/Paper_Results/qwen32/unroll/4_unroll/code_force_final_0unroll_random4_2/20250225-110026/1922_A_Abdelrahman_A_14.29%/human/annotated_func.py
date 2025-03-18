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
        
    #State: After all iterations, the variables `t`, `tests`, `n`, `a`, `b`, and `c` retain their initial values, and no further changes are made to them. The variable `no` is not retained as it is local to each iteration. The program will have printed 'YES' or 'NO' for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks if a given string `c` is identical to either of two other strings `a` or `b`. If `c` is identical to either, it prints 'NO'. Otherwise, it checks if every character in `c` is present in either `a` or `b`. If all characters in `c` are found in `a` or `b`, it prints 'YES'; otherwise, it prints 'NO'.

