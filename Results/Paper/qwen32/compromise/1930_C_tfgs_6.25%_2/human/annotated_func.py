#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 3 · 10^5) representing the length of array a, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of array a. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `n` is greater than 0, `a` is a list of `n` integers where the `i`-th element is increased by `i + 1` for all `i` from `0` to `n-1`.
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
        
    #State: `n` is greater than 0, `a` is a list of `n` integers where the `i`-th element is `n - i`, `counter` is a `Counter` object where each unique element in `a` has a count of 0, `cnt` is 0, and `ans` is a sorted list of integers from `n-1` down to `0`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `n` is greater than 0, `a` is a list of `n` integers where the `i`-th element is `n - i`, `counter` is a `Counter` object where each unique element in `a` has a count of 0, `cnt` is 0, and `ans` is a sorted list of integers from `n-1` down to `0` followed by `-1, -2, ..., -cnt`.
    print(*ans)
    #This is printed: n-1, n-2, ..., 1, 0
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers, modifies the list by adding an incrementing value to each element, and then constructs a new list `ans` that contains a sequence of integers from the highest unique modified value down to 0, filling in any gaps with consecutive decreasing integers. The final list `ans` is printed.

