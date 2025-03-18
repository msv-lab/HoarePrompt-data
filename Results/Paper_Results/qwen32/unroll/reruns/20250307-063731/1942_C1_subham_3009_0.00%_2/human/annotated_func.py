#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 * 10^5), and y is 0. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen. The sum of x over all test cases does not exceed 2 * 10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: The output will consist of `t` lines, each containing the value `x - 2` for the corresponding input.
    #State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 * 10^5), and y is 0. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen. The sum of x over all test cases does not exceed 2 * 10^5. If the program is executed as the main module, the output will consist of t lines, each containing the value x - 2 for the corresponding input.
#Overall this is what the function does:The function processes `t` test cases, each consisting of integers `n`, `x`, and `y` (where `y` is always 0), along with a list of `x` distinct integers from 1 to `n`. For each test case, it outputs the value `x - 2`.

