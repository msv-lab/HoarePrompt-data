#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers where 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 * 10^5), and y = 0; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `T` is 0, `n`, `x`, and `y` are assigned values from the input split by spaces, `y` is no longer 0, the second line of each test case contains `x` distinct integers from 1 to `n`, representing the vertices Bessie has chosen, `list0` is a sorted list of integers read from the input, `count` is the total number of times the difference between consecutive elements in `list0` is exactly 1 plus the number of times `num` (which is `n - list0[-1]`) is 1, `_` is `T - 1` (initially 0 and incremented by 1 with each iteration until it equals `T`), and the loop has executed `T` times.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `x`, and `y`, and a list of `x` distinct integers. It reads the number of test cases `T` and for each test case, it reads `n`, `x`, and `y`, followed by a list of `x` integers. The function then sorts this list and calculates the number of gaps of size 1 between consecutive elements in the list, including the gap between the last element and `n`. It prints the sum of these gaps plus `x - 2` for each test case. After processing all test cases, the function completes without returning any value.

