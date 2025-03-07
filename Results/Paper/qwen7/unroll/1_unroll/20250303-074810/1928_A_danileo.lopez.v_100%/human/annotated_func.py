#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            if a % 2 == 0:
                a1, a2 = a // 2, a // 2
                if a1 != b:
                    print('Yes')
                    continue
            if b % 2 == 0:
                b1, b2 = b // 2, b // 2
                if b1 != a:
                    print('Yes')
                    continue
            print('No')
        else:
            print('No')
        
    #State: Output State: The output will consist of 'Yes' or 'No' for each iteration based on the conditions provided in the loop. Specifically, if either `a` or `b` is even, and the halved value of the even number does not match the other number, 'Yes' will be printed; otherwise, 'No' will be printed. If neither `a` nor `b` is even, 'No' will always be printed. The exact sequence of 'Yes' and 'No' depends on the input values for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers \(a\) and \(b\). It checks whether either \(a\) or \(b\) is even. If \(a\) is even, it checks if half of \(a\) equals \(b\); if \(b\) is even, it checks if half of \(b\) equals \(a\). If either condition is met, it prints 'Yes'; otherwise, it prints 'No'. This process is repeated for each test case specified by the positive integer \(t\). The function does not return any value but prints 'Yes' or 'No' for each test case.

