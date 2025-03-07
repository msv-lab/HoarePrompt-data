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
            counter = 0
            for x in c:
                if x not in a[counter] and x not in b[counter]:
                    no = False
                    print('YES')
                    break
                counter += 1
        
        if no:
            print('NO')
        
    #State: `tests` must be greater than 0, `i` is equal to `tests` - 1, `slength` is an input integer for each iteration, `a` is an input string for each iteration, `b` is an input string for each iteration, `c` is an input string for each iteration, `no` is False for each iteration, and `counter` equals the length of the corresponding string `c` for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two input strings \(a\) and \(b\), and one string \(c\). For each test case, it checks if \(c\) contains any character that does not appear in either \(a\) or \(b\). If \(c\) matches either \(a\) or \(b\), or if every character in \(c\) is found in both \(a\) and \(b\), the function prints 'NO'. Otherwise, it prints 'YES'. The function reads the number of test cases, the length of the strings, and the strings themselves for each test case.

