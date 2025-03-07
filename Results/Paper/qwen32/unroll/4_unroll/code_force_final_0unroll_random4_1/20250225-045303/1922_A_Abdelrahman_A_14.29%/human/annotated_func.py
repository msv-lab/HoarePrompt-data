#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: `tests` is an integer input value such that 1 <= `tests` <= 1000; `t` is an integer such that 1 <= `t` <= 1000; `slength`, `a`, `b`, and `c` are the values from the last test case, with `slength` being the length of `a`, `b`, and `c`, and `no` is a boolean reflecting the final state of the flag from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three strings `a`, `b`, and `c` of equal length. For each test case, it determines if there is at least one character in `c` that is not present in either `a` or `b`. If such a character exists, it prints 'YES'; otherwise, it prints 'NO'.

