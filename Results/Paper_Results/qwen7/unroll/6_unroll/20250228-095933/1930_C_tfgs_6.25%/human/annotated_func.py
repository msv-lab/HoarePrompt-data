#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `a` is a list of integers where each element `a[i]` (for 0 ≤ i < n) is increased by `i + 1`, and `n` is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5.
    #
    #In more detail, after the loop executes all the iterations, each element `a[i]` in the list `a` will be updated to `a[i] + i + 1`. The value of `t` and `n` remain unchanged.
    counter = Counter(a)
    a = list(set(a))
    a.sort(reverse=True)
    cnt = n - len(a)
    ans = []
    for i in range(len(a)):
        if i > 0:
            adv = min(a[i - 1] - a[i] - 1, cnt, counter[a[i - 1]])
            for j in range(adv):
                ans.append(a[i - 1] - j - 1)
            cnt -= adv
            counter[a[i - 1]] -= adv
        
        ans.append(a[i])
        
        counter[a[i]] -= 1
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `a` is a list of unique integers sorted in descending order, `n` is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5, `cnt` is 0, `ans` is a list containing all integers from `a[0]` to the smallest integer in `a` inclusive, repeated according to the conditions in the loop.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `a` is a list of unique integers sorted in descending order, `n` is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5, `cnt` is 0, `ans` is a list containing all integers from `a[0]` to the smallest integer in `a` inclusive, repeated 0 times (i.e., `ans` is an empty list).
    print(*ans)
    #This is printed: []
#Overall this is what the function does:The function processes a list of integers `a` of length `n` by first incrementing each element by its index plus one. It then creates a new list `ans` containing all integers from the maximum value in `a` down to the minimum value, ensuring each integer is included according to certain conditions. If there are remaining counts needed to meet these conditions, it appends the last integer in `ans` repeatedly until `cnt` reaches zero. Finally, it prints the resulting list `ans`.

