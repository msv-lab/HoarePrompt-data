#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: Output State: The output state will consist of 't' lines, each containing either 'Yes' or 'No'. For each iteration of the loop, if either 'a' or 'b' is even, it prints 'Yes', otherwise it prints 'No'. Since the values of 'a' and 'b' are provided by user input during each iteration, the exact content of 'Yes' or 'No' for each line cannot be determined without knowing the specific inputs for each 'a' and 'b'.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` indicating the number of pairs `(a, b)` to process. For each pair `(a, b)`, it checks if either `a` or `b` is an even number. If at least one of them is even, it prints 'Yes'; otherwise, it prints 'No'. After processing all pairs for each test case, it outputs `t` lines of 'Yes' or 'No' based on the condition check.

