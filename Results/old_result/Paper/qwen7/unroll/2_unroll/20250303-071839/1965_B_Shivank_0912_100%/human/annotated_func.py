#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers satisfying 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
def func():
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: Output State: t test cases are processed. For each test case, the value of `k` is decomposed into a list of powers of 2, including the largest power of 2 less than or equal to `k`, the next power of 2 greater than `k`, and the next power of 2 after that. Additionally, all powers of 2 from 1 up to but not exceeding the largest power of 2 less than `k` are included in the list. The length of this list and the list itself are printed for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes two integers `n` and `k` as inputs and generates a list containing specific powers of 2 related to `k`. The list includes the largest power of 2 less than or equal to `k`, the next power of 2 greater than `k`, and all powers of 2 from 1 up to but not exceeding the largest power of 2 less than `k`. It then prints the length of this list followed by the list itself for each test case.

