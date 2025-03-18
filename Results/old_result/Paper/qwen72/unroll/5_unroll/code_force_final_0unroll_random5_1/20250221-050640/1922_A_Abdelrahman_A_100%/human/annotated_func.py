#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 20, and a, b, and c are strings of length n consisting of lowercase Latin letters.
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
        
    #State: The values of `t`, `n`, `a`, `b`, and `c` remain unchanged. The loop iterates `tests` times, and for each iteration, it reads `slength`, `a`, `b`, and `c` from user input. The variable `no` is set to `True` at the start of each iteration and may be changed to `False` during the iteration. The loop prints 'NO' if `c` is equal to `a` or `b`, or if any character in `c` is not found in the corresponding positions in `a` or `b`. Otherwise, it prints 'YES' and breaks the loop. After `tests` iterations, the loop completes.
#Overall this is what the function does:The function `func` reads an integer `tests` from user input, which represents the number of test cases. For each test case, it reads an integer `slength`, and three strings `a`, `b`, and `c` of length `slength` from user input. The function checks if `c` is equal to `a` or `b`, or if any character in `c` at a given position is not found in the corresponding positions in `a` or `b`. If any of these conditions are met, it prints 'YES' and breaks out of the inner loop; otherwise, it prints 'NO' at the end of each test case. The function does not return any value and does not modify the input variables `t`, `n`, `a`, `b`, or `c`. After `tests` iterations, the function completes its execution.

