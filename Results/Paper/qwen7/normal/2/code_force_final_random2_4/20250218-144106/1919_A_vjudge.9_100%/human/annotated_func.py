#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: `t` must be equal to the total number of iterations the loop has executed, `i` is `t-1`, `a` and `b` are input integers assigned the values of two integers input by the user separated by a space during the last iteration of the loop. If the absolute difference between `a` and `b` is even, the loop prints 'Bob'. If the absolute difference between `a` and `b` is odd, the loop prints 'Alice'. The values of `a` and `b` from the last iteration are retained as they are.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) (1 ≤ \( t \) ≤ 1000) followed by \( t \) pairs of positive integers \( a \) and \( b \) (1 ≤ \( a, b \) ≤ 10^9). For each pair, it checks if the absolute difference between \( a \) and \( b \) is even or odd. If the difference is even, it prints 'Bob'; if odd, it prints 'Alice'. After processing all test cases, the function does not return any value but prints the results for each case.

