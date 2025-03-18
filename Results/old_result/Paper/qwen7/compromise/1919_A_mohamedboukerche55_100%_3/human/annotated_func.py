#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
        if (a + b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: The output state will consist of 'Bob' or 'Alice' printed for each iteration based on whether the sum of the first two integers in each input string is even or odd. Specifically, if the sum is even, 'Bob' will be printed; otherwise, 'Alice' will be printed. The exact sequence of 'Bob' and 'Alice' depends on the input provided for each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer `t` followed by `t` pairs of positive integers `a` and `b`. For each pair, it checks if the sum of `a` and `b` is even or odd. If the sum is even, it prints 'Bob'; if the sum is odd, it prints 'Alice'. The function does not return any value but prints the result for each test case.

