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
        
    #State: Output State: t test cases are processed. For each test case, the output consists of the length of the list `ans` followed by the elements of `ans`. The list `ans` contains specific values based on the input `k` for each test case. Specifically, `ans` includes `k - (1 << i)`, `k + 1`, `k + 1 + (1 << i)`, and powers of 2 up to 2^19 (since the loop runs 20 times). Here, `i` is determined such that `1 << i + 1` is the largest power of 2 less than or equal to `k`.
#Overall this is what the function does:The function processes a series of test cases, each defined by a positive integer `t` (the number of test cases), and for each test case, two integers `n` and `k`. It calculates and outputs a list `ans` containing specific values derived from `k`. The list includes `k - (1 << i)`, `k + 1`, `k + 1 + (1 << i)`, and powers of 2 up to 2^19. Here, `i` is determined such that `1 << i + 1` is the largest power of 2 less than or equal to `k`. For each test case, it prints the length of the list `ans` followed by its elements.

