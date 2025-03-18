#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4, each test case consists of an integer n such that 1 ≤ n ≤ 2 · 10^5, and a list of n integers a where 0 ≤ a_i < n. The sum of n across all test cases does not exceed 2 · 10^5.
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
        
    #State: `tc` is equal to the total number of test cases `t`, `N` is the length of the list for the last test case, `a` is the list of integers for the last test case, `cnt` is a defaultdict with counts of elements in `a` for the last test case, `t` is either 0 or 1, and `i` is either the index where the loop broke or `N-1` if the loop did not break early.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n` and a list of `n` integers `a`, where each element `a_i` is between 0 and `n-1`. It then determines and prints the smallest index `i` such that either the count of `i` in the list `a` is 1 or the count of `i` is 0, or if there are at least two unique elements with a count of 1.

