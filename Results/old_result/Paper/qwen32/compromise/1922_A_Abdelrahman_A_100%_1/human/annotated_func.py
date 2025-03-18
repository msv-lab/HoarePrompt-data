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
            counter = 0
            for x in c:
                if x not in a[counter] and x not in b[counter]:
                    no = False
                    print('YES')
                    break
                counter += 1
        
        if no:
            print('NO')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `tests` is an integer representing the total number of test cases that have been processed, `n` is an integer such that 1 ≤ n ≤ 20, `a`, `b`, and `c` are strings each consisting of exactly `n` lowercase Latin letters from the last iteration, and `slength` is an input integer from the last iteration. The loop has finished executing all `tests` iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it checks if a given string `c` can be formed by characters from corresponding positions in strings `a` and `b`. It prints 'YES' if for every character in `c`, there is a corresponding character in either `a` or `b` at the same position, otherwise it prints 'NO'.

