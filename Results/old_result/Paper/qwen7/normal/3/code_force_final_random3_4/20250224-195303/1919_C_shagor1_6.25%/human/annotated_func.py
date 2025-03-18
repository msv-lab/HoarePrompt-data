#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        *inp, = map(int, input().split())
        
        x = y = n + 1
        
        ans = 0
        
        for a in inp:
            if a <= x:
                x = a
            elif a <= y:
                y = a
            else:
                x == y
                y = a
                ans += 1
        
        print(ans)
        
    #State: After the loop executes all iterations, `x` will be the minimum value in the list `inp`, `y` will be the second minimum value in the list `inp`, and `ans` will be the count of elements in `inp` that are greater than both `x` and `y`.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer n and a list of n integers. For each test case, it finds the minimum and second minimum values in the list and counts how many elements in the list are greater than both these values. The function prints the count for each test case.

