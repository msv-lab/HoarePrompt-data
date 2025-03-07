#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, a and b are integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: t test cases have been processed, and for each test case, either 'Bob' or 'Alice' has been printed based on whether the absolute difference between a and b is even or odd, respectively. The values of t, a, and b from the initial state are no longer relevant as they have been used and are not retained after the loop completes.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `a` and `b`. For each test case, it prints 'Bob' if the absolute difference between `a` and `b` is even, and 'Alice' if the absolute difference is odd.

