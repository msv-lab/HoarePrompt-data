#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: All variables outside the loop (like `tests`, `slength`, `a`, `b`) remain unchanged from their final values after the third iteration. Inside the loop, `i` will be equal to `tests - 1`, `no` will be a boolean value depending on the inputs provided, `counter` will be equal to the length of `c`, and `c` will be the last input string provided. The loop will have completed all its iterations based on the initial value of `tests`.
    #
    #In more detail:
    #- `i` will be set to `tests - 1` because the loop runs from `0` to `tests - 1`.
    #- `no` will be `True` if for every character in `c`, there exists at least one position in `a` or `b` where the character does not appear, otherwise it will be `False`.
    #- `counter` will be equal to the length of `c` since the loop increments `counter` for each character in `c`.
    #- `c` will be the last input string provided by the user.
    #- The values of `slength`, `a`, `b`, and any other variables defined before the loop will remain as they were after the third iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it checks if a given string `c` can be formed by characters that do not simultaneously appear in both strings `a` and `b`. If for every character in `c`, there is at least one position in either `a` or `b` where the character does not appear, the function prints 'YES'. Otherwise, it prints 'NO'. After processing all test cases, the function does not return any value but prints 'YES' or 'NO' for each test case.

