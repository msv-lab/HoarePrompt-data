#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and y is 0. Additionally, there are x distinct integers in the range from 1 to n representing the vertices Bessie has chosen, and the sum of x over all test cases does not exceed 2 · 10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: - The variable `t` will be 0 after the loop finishes, as it is decremented in each iteration until it reaches zero.
        #- The variables `n`, `x`, and `y` will hold the values from the last iteration of the loop.
        #- The variable `arr` will hold the list of integers from the last iteration of the loop.
        #- The output of the program will be a series of `x - 2` values, one for each iteration.
        #
        #However, the problem asks for the output state in terms of the variables in the loop head and body. Since `t` will be 0 after the loop, and the values of `n`, `x`, and `y` will be from the last iteration, we can describe the final state as follows:
        #
        #Output State:
    #State: `t` is 0 after the loop finishes, and `n`, `x`, and `y` hold the values from the last iteration of the loop. The variable `arr` contains the list of integers from the last iteration of the loop. The output of the program is a series of `x - 2` values, one for each iteration.
#Overall this is what the function does:The function processes `t` test cases, where for each test case it reads integers `n`, `x`, and `y` (with `y` always being 0), followed by `x` distinct integers representing vertices. It outputs `x - 2` for each test case.

