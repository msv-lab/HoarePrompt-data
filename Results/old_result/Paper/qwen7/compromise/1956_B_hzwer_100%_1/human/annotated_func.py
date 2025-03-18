#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the list a contains n integers such that 1 ≤ a_i ≤ n and each integer from 1 through n appears in the list at most 2 times.
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
        
    #State: Output State: `cnt` is [2], `ans` is 3.
    #
    #Explanation: After all iterations of the loop have finished, the list `cnt` contains only one element, which is 2. This indicates that there was exactly one number in the list `a` that appeared exactly twice. The variable `ans` is the sum of `max(0, x - 1)` for all elements `x` in `cnt` after all iterations, which totals to 3. This means that for every number in `a` that appeared more than once, `ans` incremented by the number of times it appeared minus one. Since the only remaining value in `cnt` is 2, it implies that there was one number that appeared twice, contributing 1 to `ans` (since `max(0, 2 - 1) = 1`). The loop stops because `cnt` now has only one element, and no further iterations are possible.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` followed by a list of `n` integers. It counts the occurrences of each integer in the list and calculates the total number of integers that appear more than once, subtracting one from their count. The function then prints the sum of these values for each test case.

