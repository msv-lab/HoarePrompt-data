#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20. a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' based on the conditions specified in the loop. For each test case (`i` in `range(tests)`), it checks if the third string `c` contains any character that is not present in either of the strings `a` or `b`. If `c` contains any such character, it prints 'NO'. Otherwise, it checks if `c` matches exactly with either `a` or `b`, and if so, it prints 'NO'. If none of these conditions are met, it prints 'YES'. The final output state will be a list of 'YES' and 'NO' corresponding to each test case.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer t (number of test cases), an integer n (length of strings), and three strings a, b, and c (each of length n). For each test case, it checks if the string c contains any character not present in either a or b. If c contains such a character, it prints 'NO'. If c does not contain any such character, it further checks if c matches exactly with either a or b. If c matches exactly with either a or b, it prints 'NO'. If none of the above conditions are met, it prints 'YES'. The function outputs a series of 'YES' and 'NO' corresponding to each test case.

