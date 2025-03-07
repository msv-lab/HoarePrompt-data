#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 2 · 10^4, n is an integer where 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `tc` is `t-1`, `N` is the last input integer greater than 0, `i` is the index at which the loop broke or `N-1` if the loop completed all iterations, `cnt` is a defaultdict with default integer values and contains the count of each integer in the last list `a`, `t` is the number of unique elements in the last list `a` that appear exactly once up to the point where the loop breaks, and `a` is the last list of integers input by the user.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it reads an integer `N` and a list `a` of `N` integers. It then counts the occurrences of each integer in `a`. The function prints the first integer `i` in the range `[0, N-1]` that either appears exactly once in `a` and is the second such unique integer encountered, or is the first integer that does not appear in `a`. If no such integer is found, it prints the last integer in the range. The function does not return any value. After the function concludes, `tc` is the number of test cases processed, `N` is the last input integer greater than 0, `i` is the index at which the loop broke or `N-1` if the loop completed all iterations, `cnt` is a dictionary containing the count of each integer in the last list `a`, and `a` is the last list of integers input by the user.

