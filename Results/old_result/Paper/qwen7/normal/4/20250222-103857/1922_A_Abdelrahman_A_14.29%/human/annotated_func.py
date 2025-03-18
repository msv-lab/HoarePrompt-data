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
            for x in c:
                if x not in a and x not in b:
                    print('YES')
                    no = False
                    break
        
        if no:
            print('NO')
        
    #State: After all iterations of the loop have finished, the value of `tests` will be the total number of inputs processed, `no` will be True, `i` will equal `tests`, `slength` will be the sum of all `slength` values input during the iterations, `a` will be the concatenation of all `a` strings input during the iterations, `b` will be the concatenation of all `b` strings input during the iterations, and `c` will be the concatenation of all `c` strings input during the iterations.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three strings \(a\), \(b\), and \(c\) of equal length \(n\) (where \(1 \leq n \leq 20\)). It checks if \(c\) contains any character not present in either \(a\) or \(b\). If \(c\) matches either \(a\) or \(b\), it prints 'NO'. Otherwise, if \(c\) contains only characters present in \(a\) and \(b\), it prints 'YES'. After processing all test cases, it prints 'NO' for each remaining test case.

