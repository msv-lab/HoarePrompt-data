#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 1 <= n, k <= 2 * 10^5, and a is a list of n integers where -10^9 <= a_i <= 10^9. The sum of the values of n and k for all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, the code computes and prints the value `(2
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`, and a list `a` of `n` integers. For each test case, it calculates and prints a specific value based on the elements of the list and the integer `k`, using the formula `(2^k * maxi - maxi + sum(a)) % 1000000007`, where `maxi` is the maximum value obtained from a particular computation involving the list elements.

