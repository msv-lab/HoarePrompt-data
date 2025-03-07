#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. The sum of n over all test cases does not exceed 10^7.
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
        
    #State: The final output state consists of `t` blocks, each starting with the length of the `ans` list followed by the elements of the `ans` list, computed for each test case as described.
#Overall this is what the function does:The function processes `t` test cases, each defined by integers `n` and `k`. For each test case, it calculates and prints a list of integers starting with the length of the list, followed by specific values derived from `k`. The values include `k - 2^i`, `k + 1`, `k + 1 + 2^i`, and `2^j` for `j` not equal to `i`, where `i` is the largest integer such that `2^(i+1)` is less than or equal to `k`.

