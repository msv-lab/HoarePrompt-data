#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' responses based on the conditions checked within the nested loops. For each test case (`i` in `range(tests)`), it checks if the string `c` contains any character that is not present in either `a` or `b`. If `c` matches `a` or `b`, it immediately prints 'NO'. Otherwise, it iterates through each character of `c` and checks if it exists in the corresponding positions of `a` and `b`. If a character in `c` is not found in both `a` and `b` at the same position, it prints 'YES' and breaks out of the loop. If no such character is found throughout the loop, it prints 'NO'.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three strings \(a\), \(b\), and \(c\) of equal length \(n\) (where \(1 \leq n \leq 20\)). It then checks if \(c\) contains any character that is not present in either \(a\) or \(b\). If \(c\) matches \(a\) or \(b\), it prints 'NO'. Otherwise, it iterates through each character of \(c\) and checks if it exists in the corresponding positions of \(a\) and \(b\). If a character in \(c\) is not found in both \(a\) and \(b\) at the same position, it prints 'YES' and stops further checks. If no such character is found, it prints 'NO'. The function does not return any value but prints the result for each test case.

