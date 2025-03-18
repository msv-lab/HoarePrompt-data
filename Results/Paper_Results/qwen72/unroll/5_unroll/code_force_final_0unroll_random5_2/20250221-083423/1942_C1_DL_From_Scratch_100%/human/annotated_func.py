#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 4 <= n <= 10^9, x is an integer such that 2 <= x <= min(n, 2 * 10^5), y is an integer and y = 0, and the second line consists of x distinct integers from 1 to n representing the vertices Bessie has chosen.
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
        
        num = list0[0] + n - list0[-1] - 1
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: t remains an integer such that 1 <= t <= 10^4, n is an integer such that 4 <= n <= 10^9, x is an integer such that 2 <= x <= min(n, 2 * 10^5), y is an integer and y = 0, T is an input integer, and the second line consists of x distinct integers from 1 to n representing the vertices Bessie has chosen. The loop prints the number of gaps of size 1 between the sorted vertices for each iteration, plus x - 2.
#Overall this is what the function does:The function `func` reads an integer `T` from input, which represents the number of test cases. For each test case, it reads three integers `n`, `x`, and `y` from input, and a list of `x` distinct integers representing vertices chosen by Bessie. It then calculates and prints the number of gaps of size 1 between the sorted vertices, plus `x - 2`. The function does not return any value. After the function concludes, `t` remains an integer such that 1 <= t <= 10^4, `n` is an integer such that 4 <= n <= 10^9, `x` is an integer such that 2 <= x <= min(n, 2 * 10^5), `y` is an integer and y = 0, and the input list of vertices is processed for each test case.

