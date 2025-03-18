#State of the program right berfore the function call: The function is expected to handle multiple test cases. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings of length n consisting of lowercase Latin letters.
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
        
    #State: The loop will have executed `tests` number of times, each time processing a new set of inputs `slength`, `a`, `b`, and `c`. For each test case, if `c` is equal to either `a` or `b`, or if any character in `c` is not found in the corresponding positions of `a` and `b`, the output will be 'YES'. Otherwise, the output will be 'NO'. The variables `a`, `b`, `c`, and `no` will be reset for each iteration, and `counter` will be used to track the position in the strings during each test case. After all iterations, `tests` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `tests` from the input, indicating the number of test cases to process. For each test case, it reads three inputs: an integer `slength`, and two strings `a` and `b` of length `slength`. It then reads another string `c` of the same length. The function checks if `c` is equal to either `a` or `b`. If so, it prints 'NO'. Otherwise, it checks if any character in `c` is not present in the corresponding positions of `a` and `b`. If such a character is found, it prints 'YES'. If no such character is found, it prints 'NO'. The function does not return any value. After processing all test cases, the variable `tests` remains unchanged, and the function concludes.

