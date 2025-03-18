#State of the program right berfore the function call: The input consists of several test cases. Each test case starts with two integers n and k (1 ≤ n, k ≤ 2 · 10^5) representing the length of the array and the number of operations, respectively. This is followed by a line containing n integers a_1, a_2, ..., a_n (-10^9 ≤ a_i ≤ 10^9) which are the elements of the array. The sum of n and k across all test cases does not exceed 2 · 10^5.
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
        
    #State: `i` is the total number of test cases, `n` and `k` are the values from the last test case, `l` is the list from the last test case, `c` is the sum of the last contiguous subsequence of non-negative numbers in the last test case, and `maxi` is the maximum cumulative sum of the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` representing the length of an array, an integer `k` representing the number of operations, and an array of `n` integers. For each test case, it calculates a result based on the maximum cumulative sum of non-negative numbers in the array, adjusted by `k` operations, and prints the result modulo 1,000,000,007.

