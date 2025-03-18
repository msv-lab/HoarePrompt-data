#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0; the sum of x over all test cases does not exceed 2⋅10^5; the first line of each test case contains three integers n, x, and y; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: Output State: `t` is 0, `__name__` is `__main__`, `n` is the first integer from the input, `x` is the second integer from the input, `y` is the third integer from the input, `arr` is a list of integers where each element is the integer from the input corresponding to its index.
        #
        #After all the iterations of the loop, `t` will be reduced to 0 since it starts as an input integer between 1 and \(10^4\) and is decremented by 1 in each iteration until it reaches 0. The values of `n`, `x`, `y`, and `arr` remain unchanged from their last updated state after the last iteration of the loop.
    #State: `t` is 0, `__name__` is `__main__`, `n` is the first integer from the input, `x` is the second integer from the input, `y` is the third integer from the input, and `arr` is a list of integers where each element is the integer from the input corresponding to its index.
#Overall this is what the function does:The function processes multiple test cases, each containing three integers \(n\), \(x\), and \(y\), followed by \(x\) distinct integers from 1 to \(n\). For each test case, it prints the value \(x - 2\). After processing all test cases, it ensures that the counter \(t\) is reduced to 0. The function does not return any value but outputs the results for each test case.

