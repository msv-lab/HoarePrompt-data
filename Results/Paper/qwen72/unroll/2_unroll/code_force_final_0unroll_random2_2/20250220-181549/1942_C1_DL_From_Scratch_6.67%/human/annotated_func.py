#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 4 <= n <= 10^9, x is an integer such that 2 <= x <= min(n, 2 * 10^5), y is an integer and y = 0, and the list of x integers contains distinct values from 1 to n.
def func():
    T = int(input())
    for _ in range(T):
        n, x, y = map(int, input().split())
        
        list0 = list(map(int, input().split()))
        
        list0 = sorted(list0)
        
        count = 0
        
        for i in range(x - 1):
            num = list0[i + 1] - list0[i] - 1
            if num == 1:
                count += 1
        
        num = n - list0[-1]
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: T is an integer such that 1 <= T <= 10^4, t is an integer such that 1 <= t <= 10^4, n is an integer such that 4 <= n <= 10^9, x is an integer such that 2 <= x <= min(n, 2 * 10^5), y is 0, and the list of x integers contains distinct values from 1 to n. The loop has printed the value of count + x - 2 for each iteration, where count is the number of gaps of size 1 between consecutive elements in the sorted list of x integers, plus x - 2.
#Overall this is what the function does:The function `func` reads an integer `T` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `x`, and `y` from the input, where `n` is the upper bound of a range of integers, `x` is the number of distinct integers in the range from 1 to `n`, and `y` is always 0. It then reads a list of `x` distinct integers from the input, sorts this list, and calculates the number of gaps of size 1 between consecutive elements in the sorted list. The function prints the sum of this count and `x - 2` for each test case. After all test cases are processed, the function has printed the calculated value for each test case, and the state of the program remains as described in the initial state, with the exception that the input has been consumed.

