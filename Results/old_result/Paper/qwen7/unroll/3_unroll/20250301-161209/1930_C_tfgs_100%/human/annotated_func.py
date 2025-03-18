#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5, `a` is a list of integers where each element `a[i]` is increased by `i + 1` for all `i` in the range of `n`.
    counter = Counter(a)
    cur = 0
    a = list(set(a))
    a.sort(reverse=True)
    cnt = n - len(a)
    ans = []
    for i in range(len(a)):
        if i > 0:
            adv = min(a[i - 1] - a[i] - 1, cnt, cur)
            for j in range(adv):
                ans.append(a[i - 1] - j - 1)
            cnt -= adv
            cur -= adv
        
        ans.append(a[i])
        
        counter[a[i]] -= 1
        
        cur += counter[a[i]]
        
    #State: cur is 0, cnt is 0, ans is a list containing elements derived from the differences between consecutive elements in the list `a` up to `n` elements in total, and counter is a Counter object with decremented counts of each element in `a`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: cur is 0, cnt is 0, ans is a list containing elements derived from the differences between consecutive elements in the list `a` up to `n` elements in total, with each element decremented by the number of iterations in the loop, and counter is a Counter object with decremented counts of each element in `a`.
    print(*ans)
    #This is printed: [difference1 - cnt, difference2 - cnt, ..., differencen - cnt]
#Overall this is what the function does:The function processes a list of integers `a` for each test case. It first increments each element in the list by its index plus one. Then, it creates a list `ans` containing the differences between consecutive elements in the sorted unique list of `a`, up to a length of `n`. It adjusts the values in `ans` based on the count of each element in the original list `a`. Finally, it prints the adjusted list `ans`.

