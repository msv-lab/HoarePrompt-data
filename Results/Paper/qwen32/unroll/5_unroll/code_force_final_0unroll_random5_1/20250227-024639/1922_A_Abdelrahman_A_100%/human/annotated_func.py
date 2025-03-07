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
            counter = 0
            for x in c:
                if x not in a[counter] and x not in b[counter]:
                    no = False
                    print('YES')
                    break
                counter += 1
        
        if no:
            print('NO')
        
    #State: - After all iterations, the only variables that are affected and need to be described in the output state are `tests`, `a`, `b`, and `c` (as these are the only variables that are modified inside the loop).
    #   - The variable `no` is a local variable within each iteration and does not affect the output state across iterations.
    #   - The variable `slength` is read but not stored or used after the current iteration, so it does not affect the output state.
    #
    #Given that the loop modifies `a`, `b`, and `c` in each iteration, the final values of `a`, `b`, and `c` will be the values from the last test case processed. The variable `tests` remains unchanged as it is the number of test cases and is not modified within the loop.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of three strings `a`, `b`, and `c` of equal length. For each test case, it checks if string `c` can be formed by characters from the corresponding positions in strings `a` and `b`. It outputs "YES" if `c` can be formed in this manner, otherwise "NO". The final state of the program includes the processed values of `a`, `b`, and `c` from the last test case.

