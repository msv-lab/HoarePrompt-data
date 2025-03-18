#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: Output State: The output consists of 't' lines, each containing either 'Yes' or 'No'. For each iteration, if either 'a' or 'b' is even, the output is 'Yes', otherwise it is 'No'. Given the initial state where 't' is a positive integer between 1 and 10^4, the output will depend on the values of 'a' and 'b' provided for each of the 't' iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(a\) and \(b\). It reads the number of test cases \(t\) first, then for each test case, it checks if either \(a\) or \(b\) is even. If either is even, it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, it outputs 'Yes' or 'No' for each case based on the condition.

