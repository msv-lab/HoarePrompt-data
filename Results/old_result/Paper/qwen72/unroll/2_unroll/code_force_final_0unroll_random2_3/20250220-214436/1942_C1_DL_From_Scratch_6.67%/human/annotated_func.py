#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 4 <= n <= 10^9, x is an integer such that 2 <= x <= min(n, 2 * 10^5), y is an integer and y = 0, and the list of x integers are distinct and within the range 1 to n.
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
        
    #State: T is an integer such that 1 <= T <= 10^4, n, x, y, and list0 remain unchanged for each iteration, but their values are re-assigned in each iteration of the loop. count is 0 at the start of each iteration and is printed as count + x - 2 at the end of each iteration.
#Overall this is what the function does:The function `func` reads an integer `T` from the input, representing the number of test cases. For each test case, it reads three integers `n`, `x`, and `y` (where `y` is always 0 and not used), and a list of `x` distinct integers. The function then calculates and prints the number of gaps of size 1 between the sorted list of integers, plus `x - 2`. The function does not return any value. After the function concludes, `T` is an integer such that 1 <= T <= 10^4, and for each test case, `n`, `x`, `y`, and the list of integers remain unchanged, but their values are re-assigned in each iteration of the loop.

