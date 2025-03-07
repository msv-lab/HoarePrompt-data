#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: Output State: The output state will consist of 't' lines, each containing either 'Yes' or 'No'. Each line corresponds to the result of the condition for each iteration of the loop. If at least one of the integers 'a' or 'b' is even, the output will be 'Yes', otherwise it will be 'No'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it checks if at least one of the integers \(a\) or \(b\) is even. If so, it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, it outputs a total of \(t\) lines, where \(t\) is the number of test cases provided.

