#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, n is an integer where 4 <= n <= 10^9, x is an integer where 2 <= x <= min(n, 2 * 10^5), y is an integer and y = 0, and the second line consists of x distinct integers from 1 to n.
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
        
    #State: `t` is an integer where \(1 \leq t \leq 10^4\), `n` is an input integer where \(4 \leq n \leq 10^9\), `x` is an input integer where \(2 \leq x \leq \min(n, 2 \times 10^5)\), `y` is an input integer, `_` is `T`, `T` must be greater than 0, `list0` is a sorted list of integers derived from the input, `i` is `x - 2`, and `num` is `n - list0[-1]`. If `num` is 1, `count` is the number of times the difference between consecutive elements in `list0` (from index 0 to `x-2`) is exactly 1 plus 1. Otherwise, `count` remains the number of times the difference between consecutive elements in `list0` (from index 0 to `x-2`) is exactly 1.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it takes three integers `n`, `x`, and `y`, and a list of `x` distinct integers. It then calculates the number of gaps of size 1 between consecutive elements in the sorted list, plus the number of gaps of size 1 between the last element and `n`. The function prints the result for each test case. After processing all test cases, the function completes, and the state of the program includes the original values of `t`, `n`, `x`, and `y`, and the processed results have been printed to the standard output.

