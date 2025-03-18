#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' responses based on the conditions checked within the loop for each iteration. For each test case (`i` in `range(tests)`), the program checks if character `c` is in strings `a` and `b`. If `c` is found in either `a` or `b`, it prints 'NO' and sets `no` to `False`. Otherwise, it checks if every character in `c` is present in either `a` or `b`. If any character in `c` is not found in either `a` or `b`, it prints 'YES' and sets `no` to `False`. If `no` remains `True` after these checks, it prints 'NO'. This process repeats for each test case, and the final output will be a sequence of 'YES' or 'NO' for each test case.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer t (1 ≤ t ≤ 1000), an integer n (1 ≤ n ≤ 20), and three strings a, b, and c, each consisting of exactly n lowercase Latin letters. For each test case, it checks if the string c contains any characters that are not present in either string a or b. If c contains any such characters, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function outputs a sequence of 'YES' or 'NO' responses corresponding to each test case.

