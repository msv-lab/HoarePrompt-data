#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and the integers a_1, a_2, ..., a_n are in the range 1 to n, with each integer from 1 to n appearing at most twice. The sum of all n across all test cases does not exceed 2 ⋅ 10^5.
def func():
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = [0] * (n + 1)
        
        for x in a:
            cnt[x] += 1
        
        ans = 0
        
        for x in cnt:
            ans += max(0, x - 1)
        
        print(ans)
        
    #State: `ans` will be the total count of reductions for each unique element in `a`, where each reduction is calculated as `max(0, x - 1)` for every element `x` in `cnt`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer \( n \) and a list of integers \( a \). It counts the occurrences of each integer in the list \( a \) and calculates the total number of reductions needed such that each integer appears at most once. The function prints the total count of these reductions for each test case.

