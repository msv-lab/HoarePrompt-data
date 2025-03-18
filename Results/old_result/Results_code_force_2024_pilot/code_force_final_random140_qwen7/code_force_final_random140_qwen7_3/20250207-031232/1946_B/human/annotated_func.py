#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 ⋅ 10^5, and the sum of the values of n and k for all test cases does not exceed 2 ⋅ 10^5. The array a is a list of n integers where -10^9 ≤ a_i ≤ 10^9 for each element a_i in the array.
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
        
    #State: Output State: The final output state after the loop executes all its iterations will have `maxi` as the maximum value between the cumulative sum of non-negative elements in the array `l` and the maximum value of `c` (which is the sum of elements until a negative element is encountered with an absolute value greater than or equal to `c`) for each iteration. The variable `c` will hold the sum of all non-negative elements in the array `l` after processing all elements. The loop processes each test case independently, so the final `maxi` for each test case will be printed as `(2 ** k * maxi - maxi + sum(l)) % 1000000007`. This calculation is performed for each test case, and the result is printed after all iterations of the loop are completed.
    #
    #In simpler terms, after all iterations, `maxi` will be the highest value obtained from either the sum of non-negative elements or the special condition involving negative elements, and `c` will be the total sum of all non-negative elements in the array `l`. The final output for each test case will be calculated using the formula provided and printed modulo \(1000000007\).
#Overall this is what the function does:The function processes multiple test cases, each consisting of positive integers n and k, and an array of n integers. For each test case, it calculates a specific value based on the array elements and prints the result for each test case. The final output for each test case is computed using the formula \(2^k \times \text{maxi} - \text{maxi} + \sum(\text{array})\) modulo \(1000000007\), where \(\text{maxi}\) is the maximum value obtained from either the cumulative sum of non-negative elements in the array or a special condition involving negative elements, and \(\sum(\text{array})\) is the total sum of all elements in the array.

