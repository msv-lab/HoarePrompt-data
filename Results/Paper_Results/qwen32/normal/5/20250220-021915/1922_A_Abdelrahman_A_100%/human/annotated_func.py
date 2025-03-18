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
            counter = 0
            for x in c:
                if x not in a[counter] and x not in b[counter]:
                    no = False
                    print('YES')
                    break
                counter += 1
        
        if no:
            print('NO')
        
    #State: The loop has executed `tests` number of times. For each iteration, `slength`, `a`, `b`, and `c` are read as inputs. The variable `no` is used to determine if `c` is neither equal to `a` nor `b` and if every character in `c` is found in either `a` or `b` at the corresponding position. If these conditions are met, `no` remains `True`, and 'NO' is printed. Otherwise, 'YES' is printed. After all iterations, the loop terminates, and the program ends.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks if a given string `c` is neither equal to strings `a` nor `b` and if each character in `c` is found in either `a` or `b` at the corresponding position. It prints 'NO' if these conditions are met for all characters in `c`, otherwise, it prints 'YES'.

