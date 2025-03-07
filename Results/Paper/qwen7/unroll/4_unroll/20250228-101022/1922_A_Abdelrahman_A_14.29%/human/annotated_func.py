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
            for x in c:
                if x not in a and x not in b:
                    print('YES')
                    no = False
                    break
        
        if no:
            print('NO')
        
    #State: Output State: The output state will consist of 'YES' or 'NO' printed for each iteration based on the conditions specified in the loop. For each test case, if character `c` is found in either `a` or `b`, it prints 'NO'. Otherwise, it checks if every character in `c` is present in either `a` or `b`. If any character in `c` is not found in both `a` and `b`, it prints 'YES'; otherwise, it prints 'NO'. This process repeats for each of the `tests` inputs.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three strings `a`, `b`, and `c`, each consisting of exactly `n` lowercase Latin letters, where `n` is between 1 and 20. It then checks if the string `c` contains any character that is not present in either `a` or `b`. If `c` contains such a character, it prints 'YES'. Otherwise, if `c` is entirely composed of characters found in either `a` or `b`, it prints 'NO'. This process is repeated for each of the `t` test cases provided, where `t` is between 1 and 1000. After processing all test cases, the function does not return any value but prints the results for each test case.

