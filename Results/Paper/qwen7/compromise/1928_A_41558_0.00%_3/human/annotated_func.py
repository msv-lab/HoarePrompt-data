#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b or b / 2 == a:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' printed for each iteration of the loop based on the conditions provided. Specifically, for each pair (a, b) entered, if both a and b are odd, or if a/2 equals b or b/2 equals a, the output will be 'NO', otherwise it will be 'YES'. The total number of outputs will be equal to the value of n.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it checks if both \(a\) and \(b\) are odd, or if \(a/2\) equals \(b\) or \(b/2\) equals \(a\). If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function reads the number of test cases from user input, then iterates through each test case, performing the specified checks and printing the result.

