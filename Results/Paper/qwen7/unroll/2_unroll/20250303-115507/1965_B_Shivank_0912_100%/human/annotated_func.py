#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers satisfying 2 <= n <= 10^6 and 1 <= k <= n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
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
        
    #State: Output State: t test cases are processed. For each test case, the output consists of the length of the list `ans` followed by the elements of `ans`. The list `ans` contains specific integers derived from the values of `n` and `k` for each test case. Specifically, `ans` includes `k - (1 << i)`, `k + 1`, `k + 1 + (1 << i)`, and all powers of 2 up to 2^19 (since the loop runs for 20 iterations but skips the index `i`). The values printed for each test case depend on the inputs `n` and `k`, but the structure of the output remains consistent across all test cases.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \( n \) and \( k \). It then calculates a list of integers based on these values and prints the length of this list followed by its elements. The list includes specific values derived from \( k \) and all powers of 2 up to \( 2^{19} \), excluding one particular power of 2. After processing all test cases, it outputs the results for each case, ensuring the output structure is consistent.

