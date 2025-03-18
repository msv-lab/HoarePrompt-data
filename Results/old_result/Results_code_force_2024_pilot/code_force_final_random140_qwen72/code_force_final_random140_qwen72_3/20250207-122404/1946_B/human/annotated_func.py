#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n, k ≤ 2 · 10^5, representing the length of the array a and the number of operations, respectively. a is a list of n integers where -10^9 ≤ a_i ≤ 10^9, representing the array a. The sum of the values of n and k over all test cases does not exceed 2 · 10^5.
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
        
        print((2 ** k * maxi - maxi + sum(l)) % 1000000007)
        
    #State: After the loop executes all the iterations, `i` is `t-1`, `n` and `k` are integers with values input by the user for the last test case, `l` is a list of integers input by the user for the last test case, `maxi` is the maximum value between the current `c` and the previous `maxi` for the last test case, and `c` is the sum of the positive elements in the list `l` since the last negative number encountered, or 0 if no positive elements were added since the last reset.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case is defined by two integers `n` and `k`, and a list of integers `a`. The function calculates and prints a result for each test case based on the following logic: it finds the maximum sum of contiguous positive elements in the list `a` (resetting the sum when encountering a negative element), and then computes a final value using this maximum sum, the total sum of the list, and the value of `k`. The result for each test case is printed modulo 1000000007. After processing all test cases, the function completes without returning any value.

