#State of the program right berfore the function call: The function `func` is intended to solve a problem involving a regular polygon with `n` sides, where `n` is an integer such that 4 ≤ n ≤ 10^9, and Bessie has chosen `x` vertices, where `x` is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and `y` is fixed at 0. The vertices chosen by Bessie are represented by a list of `x` distinct integers ranging from 1 to `n`. The function is expected to handle multiple test cases, where the number of test cases `t` is an integer such that 1 ≤ t ≤ 10^4.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: The value of `t` is 0, and the loop has printed `x - 2` for each test case.
    #State: *If `t` is 0, the loop has printed `x - 2` for each test case. Otherwise, the function is intended to solve a problem involving a regular polygon with `n` sides, where `n` is an integer such that 4 ≤ n ≤ 10^9, and Bessie has chosen `x` vertices, where `x` is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and `y` is fixed at 0. The vertices chosen by Bessie are represented by a list of `x` distinct integers ranging from 1 to `n`. The function is expected to handle multiple test cases, where the number of test cases `t` is an integer such that 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three integers `n`, `x`, and `y`, and a list of `x` integers. It then prints `x - 2` for each test case. After processing all test cases, the value of `t` is 0, and the function has completed its execution. The function does not return any value.

