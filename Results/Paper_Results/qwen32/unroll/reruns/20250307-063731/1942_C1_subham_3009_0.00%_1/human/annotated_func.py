#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and y is 0. The sum of x over all test cases does not exceed 2 · 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: The output state consists of `t` lines, each containing `x - 2` for the corresponding test case.
    #State: For each test case, if the program is run as the main module, the output consists of `t` lines, each containing `x - 2` for the corresponding test case. If the program is not run as the main module, there is no output.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads integers `n`, `x`, and `y` (where `y` is always 0), and a list of `x` distinct integers representing vertices. It then outputs `x - 2` for each test case.

