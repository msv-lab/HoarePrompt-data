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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' responses based on the conditions checked within the loop for each iteration. For each test case (`i` in `range(tests)`), the program checks if character `c` is in strings `a` or `b`. If `c` is found in either `a` or `b`, it prints 'NO'. Otherwise, it checks if each character in `c` is present in the corresponding part of `a` and `b`. If any character in `c` is not found in both `a` and `b`, it prints 'YES', otherwise it prints 'NO'. The output state will be a list of 'YES' and 'NO' for each test case.
#Overall this is what the function does:Functionality: The function processes multiple test cases, each involving three strings \(a\), \(b\), and \(c\), where \(a\) and \(b\) are each of length \(n\) (with \(1 \leq n \leq 20\)), and \(c\) is also of length \(n\). For each test case, the function checks if \(c\) contains any character not present in either \(a\) or \(b\). If \(c\) contains any such character, it outputs 'NO'. Otherwise, it checks if each character in \(c\) is present in the corresponding positions in \(a\) and \(b\). If any character in \(c\) is not found in both \(a\) and \(b\), it outputs 'YES'; otherwise, it outputs 'NO'. The function outputs a series of 'YES' and 'NO' responses, one for each test case.

