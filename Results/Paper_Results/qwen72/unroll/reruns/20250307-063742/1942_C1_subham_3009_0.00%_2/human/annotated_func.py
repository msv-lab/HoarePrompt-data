#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case consists of a regular polygon with n sides (4 ≤ n ≤ 10^9), x vertices chosen by Bessie (2 ≤ x ≤ min(n, 2 · 10^5)), and y = 0. The vertices chosen by Bessie are distinct integers from 1 to n. The sum of x over all test cases does not exceed 2 · 10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: t = 0.
    #State: *If the program is the main module, `t` is set to 0. Otherwise, `t` remains unchanged and the function does not execute any specific action.
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case involves a regular polygon with `n` sides and `x` distinct vertices chosen by Bessie. The function reads the number of test cases `t` from the input, and for each test case, it reads `n`, `x`, and `y` (where `y` is always 0), followed by a list of `x` vertices. The function then prints `x - 2` for each test case. After processing all test cases, the function sets `t` to 0 if it is the main module. If the function is not the main module, `t` remains unchanged and no specific action is performed.

