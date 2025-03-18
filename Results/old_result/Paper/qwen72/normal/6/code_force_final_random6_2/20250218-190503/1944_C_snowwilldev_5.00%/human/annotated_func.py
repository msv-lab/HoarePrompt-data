#State of the program right berfore the function call: t is an integer such that 1 <= t <= 2 * 10^4, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has completed all iterations, `i` is `N-1`, `t` is the number of times `cnt[i]` was 1 during the loop, and the loop has printed the value of `i` if `t` became greater than or equal to 2 or `cnt[i]` was 0 at any point during the loop.
#Overall this is what the function does:The function `func` reads input for multiple test cases, each consisting of an integer `N` and a list `a` of `N` integers. For each test case, it counts the occurrences of each integer in `a`. It then iterates through the list `a` and prints the first index `i` where the count of `i` is 1 and the count of any previous index was 1, or where the count of `i` is 0. If no such index is found, the function implicitly ends the test case without printing anything. The function does not return any value.

