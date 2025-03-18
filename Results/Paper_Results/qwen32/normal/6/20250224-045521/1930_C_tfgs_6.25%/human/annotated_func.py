#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 3 · 10^5) representing the length of array a, and a list a of n integers (1 ≤ a_i ≤ 10^9) representing the elements of array a. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `n` is an integer (1 ≤ `n` ≤ 3 · 10^5); `a` is a list of `n` integers where each element `a[i]` is updated to `a[i] + i + 1`.
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
        
    #State: `n` is an integer (1 ≤ `n` ≤ 3 · 10^5); `a` is a list of unique integers sorted in descending order; `counter` is a Counter object with decremented counts for the elements used in `ans`; `cnt` is `n - len(ans)`; `ans` is a list containing all elements of `a` and all additional integers inserted between consecutive elements in `a` up to the constraints of `cnt` and the counts in the `counter`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `n` is an integer (1 ≤ `n` ≤ 3 · 10^5); `a` is a list of unique integers sorted in descending order; `counter` is a Counter object with decremented counts for the elements used in `ans`; `cnt` is `0`; `ans` is a list containing all elements of `a` and all additional integers inserted between consecutive elements in `a` up to the constraints of `cnt` and the counts in the `counter`, with additional elements appended such that the length of `ans` is `n`.
    print(*ans)
    #This is printed: Elements of `ans` (where `ans` is a list containing all elements of `a` and additional integers inserted or appended to meet the length requirement of `n`)
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers, modifies each element of `a` by adding its 1-based index, then constructs a new list `ans` that includes all unique elements of the modified `a` in descending order, along with additional integers inserted between these elements to ensure the total length of `ans` is `n`. The final list `ans` is printed.

