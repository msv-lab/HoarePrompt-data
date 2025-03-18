#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
def func():
    for tc in range(int(input())):
        N = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = defaultdict(int)
        
        for i in range(N):
            cnt[a[i]] += 1
        
        t = 0
        
        for i in range(N):
            if cnt[i] == 1:
                t += 1
            if t >= 2 or cnt[i] == 0:
                print(i)
                break
        
    #State: Output State: `t` is 1, `i` is equal to `N`, and `N` is greater than 0.
    #
    #Explanation: After the loop has executed all its iterations, the value of `i` will be equal to `N` because the loop increments `i` from 0 to `N-1` and then continues until the loop condition is no longer satisfied. Given that the loop has completed all its iterations without breaking early due to `t >= 2` or `cnt[i] == 0`, `t` remains 1 (as it was incremented once when `cnt[2]` was 1, assuming `cnt[2]` was the last element checked before the loop condition was met). The value of `N` remains greater than 0 as it was initially and has not been modified by the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( n \), a list \( a \) of \( n \) non-negative integers, and an integer \( t \) such that \( 1 \leq t \leq 2 \cdot 10^4 \). For each test case, it prints an integer \( i \) that meets specific conditions related to the count of occurrences of each element in the list \( a \). If no such \( i \) exists, it prints nothing. The function does not return any value but outputs the result directly.

