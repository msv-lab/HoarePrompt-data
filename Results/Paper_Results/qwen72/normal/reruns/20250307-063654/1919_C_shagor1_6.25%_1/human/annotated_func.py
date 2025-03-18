#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 2·10^5) representing the size of the array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the elements of the array a. The total number of test cases t is an integer (1 ≤ t ≤ 10^4), and the sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: _ is equal to `int(input())`, `n` is a positive integer, `inp` is a list of integers provided by the user, `x` is the smallest integer in the list `inp`, `y` is the second smallest integer in the list `inp` (if they exist), and `ans` is the number of integers in the list `inp` that are greater than both `x` and `y`.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers `a`. It then determines the number of integers in `a` that are greater than both the smallest and the second smallest integers in the list. The function prints this count for each test case. The function does not return any value. If the input values do not meet the specified constraints (1 ≤ n ≤ 2·10^5, 1 ≤ a_i ≤ n, and the sum of n over all test cases does not exceed 2·10^5), the behavior of the function is undefined.

