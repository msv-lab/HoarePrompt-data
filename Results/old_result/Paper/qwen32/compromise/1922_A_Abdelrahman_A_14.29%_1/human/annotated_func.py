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
        
    #State: `tests` is 0, `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 20, and `a`, `b`, and `c` are strings each consisting of exactly `n` lowercase Latin letters. The loop has finished executing all `tests` iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three strings `a`, `b`, and `c` of the same length `n`. For each test case, it determines if string `c` can be formed using characters from either `a` or `b` or if it contains at least one character not present in both `a` and `b`. It prints 'YES' if such a character exists, otherwise it prints 'NO'.

