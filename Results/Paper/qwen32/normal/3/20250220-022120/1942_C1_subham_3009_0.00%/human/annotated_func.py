#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and y is 0. Additionally, the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen. The sum of x over all test cases does not exceed 2 · 10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: `t` is 0, `n`, `x`, and `y` are the last set of integers from the input, `arr` is a list of integers representing the vertices Bessie has chosen in the last iteration.
    #State: `t` is an integer such that 1 ≤ `t` ≤ 10^4. For each test case, `n` is an integer such that 4 ≤ `n` ≤ 10^9, `x` is an integer such that 2 ≤ `x` ≤ min(`n`, 2 · 10^5), and `y` is 0. Additionally, the second line of each test case contains `x` distinct integers from 1 to `n`, representing the vertices Bessie has chosen. The sum of `x` over all test cases does not exceed 2 · 10^5. If the program is executed as the main module, `t` is set to 0, `n`, `x`, and `y` are the last set of integers from the input, and `arr` is a list of integers representing the vertices Bessie has chosen in the last iteration. Otherwise, no changes are made to the variables.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it reads integers `n`, `x`, and `y` (with `y` always being 0), followed by a list of `x` distinct integers from 1 to `n`. It then outputs `x - 2` for each test case.

