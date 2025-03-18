#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4, each test case consists of an integer n such that 1 ≤ n ≤ 2 · 10^5, and a list of n integers a where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: Each test case has printed its respective output value, and no changes are made to the global state variables outside the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers `a`. For each test case, it determines and prints the smallest index `i` such that either there are at least two elements in the list that appear exactly once, or the element `i` does not appear in the list.

