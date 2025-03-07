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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' responses based on the conditions checked within the loop for each iteration. For each test case (`i` in `range(tests)`), the program checks if the string `c` contains any character that is not present in either string `a` or `b`. If `c` contains a character from `a` or `b`, it prints 'NO'. Otherwise, if `c` contains only characters present in both `a` and `b`, it prints 'YES'. This process is repeated for each test case provided by the input integer `tests`.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer t (number of test cases), an integer n (length of strings), and three strings a, b, and c (each of length n). For each test case, it checks if string c contains any character not present in either string a or b. If c contains any such character, it outputs 'NO'; otherwise, it outputs 'YES'. After processing all test cases, the function does not return any value but prints the results for each test case.

