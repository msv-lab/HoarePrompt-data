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
        
    #State: Output State: The output consists of 'Yes' or 'No' for each iteration based on the conditions provided in the loop. Specifically, if either `a` or `b` is even, and the divided value does not match the other number, it prints 'Yes'. Otherwise, it prints 'No'. The exact sequence of 'Yes' and 'No' depends on the input values for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(a\) and \(b\). For each pair, it checks if either \(a\) or \(b\) is even. If so, it further checks if half of the even number matches the other number. If the condition is met, it prints 'Yes'; otherwise, it prints 'No'. If both numbers are odd, it always prints 'No'. After processing all test cases, the function concludes with the printed outputs.

