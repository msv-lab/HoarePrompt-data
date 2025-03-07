#State of the program right berfore the function call: The function `func` is incomplete and does not match the problem description. The correct function definition should be `def max_sum_after_operations(t, n, k, a):` where `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4), `n` and `k` are integers representing the length of the array `a` and the number of operations, respectively (1 ≤ n, k ≤ 2 · 10^5), and `a` is a list of integers (−10^9 ≤ a_i ≤ 10^9). The sum of the values of `n` and `k` for all test cases does not exceed 2 · 10^5.
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
        
    #State: `int(input())` is 0, `i` is `int(input()) - 1`, `n` and `k` are the integers from the input split by a space for the last test case, `l` is a list of integers from the input split by a space for the last test case, `c` is the sum of the non-negative elements in `l` that are contiguous and not immediately followed by a negative element whose absolute value is greater than or equal to `c`, and `maxi` is the maximum value between the previous `maxi` and the current `c` for the last test case.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it reads the length of an array `n` and the number of operations `k`, followed by the array `a` itself. It then calculates the maximum sum of contiguous non-negative elements in the array, considering the reset condition when a negative element with an absolute value greater than or equal to the current sum is encountered. Finally, it prints the result of the formula `(2

