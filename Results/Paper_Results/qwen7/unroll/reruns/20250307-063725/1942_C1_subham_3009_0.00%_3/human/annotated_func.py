#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The vertices Bessie has chosen are represented by x distinct integers from 1 to n. The sum of x over all test cases does not exceed 2⋅10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: Output State: The output state will consist of multiple lines, each containing a single integer value which is the result of `x - 2` for each iteration of the loop.
        #
        #Explanation: In each iteration of the loop, the value of `t` is decremented by 1, and then the code reads three integers (`n`, `x`, `y`) from input and an array of integers. It then prints `x - 2`. Since the value of `t` is used as the condition to continue the loop, once `t` becomes 0, the loop stops. Therefore, the number of times the loop runs is equal to the initial value of `t`. For each run, it prints `x - 2`, so the final output state will be a series of these values, one per line.
    #State: The output consists of `t` lines, each containing the value of `x - 2`, where `t` is the initial value of the integer `t`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( t \) (where \( 1 \leq t \leq 10^4 \)). For each test case, it reads three integers \( n \), \( x \), and \( y \) (with \( y \) fixed at 0), and an array of \( x \) distinct integers from 1 to \( n \). The function then prints the value \( x - 2 \) for each test case, resulting in \( t \) lines of output, each containing a single integer.

