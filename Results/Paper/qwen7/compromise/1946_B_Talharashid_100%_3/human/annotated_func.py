#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 ⋅ 10^5, and the sum of the values of n and k for all test cases does not exceed 2 ⋅ 10^5. a is a list of n integers where each integer a_i satisfies -10^9 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: After the loop executes all iterations, `maxi` will hold the maximum value between the sum of contiguous subarray elements in the list `l` that meet the specified conditions and any individual element in `l` that is less than 0 and whose absolute value is greater than or equal to `c`. The value of `maxi` will be multiplied by \(2^k\) and then adjusted by subtracting `maxi` and adding the sum of all elements in `l`. Finally, the result will be taken modulo \(1000000007\). The variable `c` will be reset to 0 after each test case, and `i` will increment with each iteration of the loop, effectively serving as the index for processing each test case. The variables `n` and `k` will retain their values from the last test case processed, and `l` will be an empty list for the next test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers `n` and `k`, and a list `l` of `n` integers. For each test case, it calculates the maximum value between the sum of contiguous subarray elements in `l` that meet specific conditions and any individual element in `l` that is less than 0 and whose absolute value is greater than or equal to `c`. This maximum value is then multiplied by \(2^k\), adjusted by subtracting `maxi` and adding the sum of all elements in `l`, and finally taken modulo \(1000000007\). The function returns this computed value after processing all test cases.

