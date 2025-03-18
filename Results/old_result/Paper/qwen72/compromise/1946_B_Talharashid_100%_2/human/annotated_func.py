#State of the program right berfore the function call: The function `func` is expected to be called with parameters in the context of a test case, where the first parameter is an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases, followed by `t` pairs of parameters for each test case. Each pair consists of two integers `n` and `k` (1 ≤ n, k ≤ 2 · 10^5) representing the length of the array and the number of operations, respectively, and a list of `n` integers `a` (-10^9 ≤ a_i ≤ 10^9) representing the array. The sum of the values of `n` and `k` for all test cases does not exceed 2 · 10^5.
def func():
    for i in range(int(input())):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        c = 0
        
        maxi = 0
        
        for ele in l:
            if ele < 0 and c <= abs(ele):
                maxi = max(c, maxi)
                c = 0
            else:
                c += ele
                maxi = max(c, maxi)
        
        maxi = max(c, maxi)
        
        print((2 ** k * maxi - maxi + sum(l)) % 1000000007)
        
    #State: The loop has completed all iterations, `i` is `t-1` (where `t` is the total number of test cases), `n` and `k` are the values provided for the last test case, `l` is the list of integers provided for the last test case, `c` is the sum of the non-negative elements in the list `l` up to the last non-negative element before a negative element that resets `c` to 0, or 0 if the last element processed is negative and `c` was reset to 0, `maxi` is the maximum value of `c` encountered during the loop execution, which represents the maximum sum of contiguous non-negative elements in the list `l` before any negative element reset `c` to 0, and the final output for each test case is `(2
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the length of an array `n` and the number of operations `k`, followed by the array `a` of `n` integers. It calculates the maximum sum of contiguous non-negative elements in the array `a` before any negative element resets the sum to 0. The function then computes and prints the result of the expression `(2

