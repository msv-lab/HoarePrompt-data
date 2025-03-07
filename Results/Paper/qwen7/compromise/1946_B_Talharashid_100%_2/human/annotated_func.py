#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 ⋅ 10^5, and the sum of the values of n and k for all test cases does not exceed 2 ⋅ 10^5. The array a is a list of integers where -10^9 ≤ a_i ≤ 10^9 for each element a_i in the array.
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
        
    #State: Output State: After all iterations of the loop have finished, `maxi` will hold the maximum value of `c` across all test cases, `c` will be 0 (as it is reset to 0 after processing each test case), `i` will be equal to `t` (indicating all test cases have been processed), `n` will be the last `n` value inputted, `k` will be the last `k` value inputted, and `l` will be an empty list since all elements have been processed.
    #
    #This means that `maxi` captures the highest accumulated value of `c` across all test cases, considering the conditions specified in the loop. The variable `c` resets to 0 after each test case, `i` increments with each iteration until it equals `t`, and `n` and `k` retain their last input values from the final test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) (number of test cases), two positive integers \( n \) and \( k \), and an array \( a \) of integers. For each test case, it calculates a value \( c \) based on the elements of array \( a \) under certain conditions and keeps track of the maximum value of \( c \) across all test cases. Finally, it prints the result of the formula \( (2^k \times \text{maxi} - \text{maxi} + \sum_{i=1}^{n} a_i) \mod 1000000007 \), where \( \text{maxi} \) is the maximum value of \( c \) found during the processing of all test cases.

