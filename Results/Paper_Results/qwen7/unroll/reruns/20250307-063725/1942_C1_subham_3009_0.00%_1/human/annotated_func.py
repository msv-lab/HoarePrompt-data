#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 ⋅ 10^5), and y = 0; the vertices are represented as x distinct integers from 1 to n; the sum of x over all test cases does not exceed 2 ⋅ 10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: The value of `t` is 0, and the loop has printed the value of `x-2` for each test case.
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4. If `t` is 0, the loop has printed the value of `x-2` for each test case. Otherwise, no changes are made to `t`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads integers t, n, x, and y, where t indicates the number of test cases, n and x have specific constraints, and y is always 0. It then reads x distinct integers representing vertices and prints the value of x - 2. After processing all test cases, it ensures that the variable t is set to 0.

