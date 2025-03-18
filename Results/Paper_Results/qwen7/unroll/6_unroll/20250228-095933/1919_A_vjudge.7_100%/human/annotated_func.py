#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: The output state consists of `test` lines, each line containing either 'Bob' or 'Alice' based on whether the sum of two integers (a and b) entered by the user is even or odd, respectively.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` followed by `t` pairs of positive integers `a` and `b`. For each pair, it checks if their sum is even or odd and prints 'Bob' if the sum is even, otherwise it prints 'Alice'. After processing all test cases, it outputs a total of `t` lines, each containing either 'Bob' or 'Alice'.

