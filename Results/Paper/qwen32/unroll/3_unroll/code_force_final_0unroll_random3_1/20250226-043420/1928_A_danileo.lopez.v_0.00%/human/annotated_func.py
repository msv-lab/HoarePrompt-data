#State of the program right berfore the function call: Each test case consists of two integers a and b (1 ≤ a, b ≤ 10^9) representing the dimensions of Bob's rectangle. There are t (1 ≤ t ≤ 10^4) such test cases.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: After executing the loop for all test cases, the output will consist of 't' lines, each containing either 'Yes' or 'No' depending on whether the dimensions of the rectangle in the corresponding test case have at least one even number. The state of variables 'a' and 'b' will reflect the last test case's dimensions processed by the loop, and 't' will remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers representing the dimensions of a rectangle. For each test case, it checks if at least one of the dimensions is even and prints 'Yes' if true, otherwise 'No'. After processing all test cases, the function outputs 'Yes' or 'No' for each case based on the evenness of the dimensions.

