#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The input also includes a list of x distinct integers from 1 to n representing the vertices Bessie has chosen, and the sum of x over all test cases does not exceed 2⋅10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: Output State: `t` is equal to 0; `n` is the integer value of the first element of the input split, `x` is the integer value of the second element of the input split, `y` is the integer value of the third element of the input split, `arr` is a list of integers obtained from converting the first `x` elements of the input split into integers.
        #
        #This output state occurs because the loop continues to execute as long as `t > 0`. After each iteration, `t` is decremented by 1. Therefore, if the loop executes all its iterations, `t` will eventually reach 0. The values of `n`, `x`, `y`, and `arr` remain unchanged from their last state within the loop, as these values are determined by the input during each iteration and not modified within the loop itself.
    #State: `t` is equal to 0, `n` is the integer value of the first element of the input split, `x` is the integer value of the second element of the input split, `y` is the integer value of the third element of the input split, and `arr` is a list of integers obtained from converting the first `x` elements of the input split into integers.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads integers t, n, x, and y (where t is a positive integer up to 10^4, n is an integer between 4 and 10^9, x is an integer between 2 and the minimum of n or 2⋅10^5, and y is always 0), along with a list of x distinct integers from 1 to n. It then prints x - 2 for each test case. After processing all test cases, it ensures that the variable t is set to 0.

