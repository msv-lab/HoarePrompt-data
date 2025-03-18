#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 3 · 10^5) representing the length of array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of array a. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `n` is an integer (1 ≤ `n` ≤ 3 · 10^5) representing the length of array `a`; `a` is a list of `n` integers where each `a_i` is the original `a_i` plus `i + 1` (i.e., `a_1` becomes `a_1 + 1`, `a_2` becomes `a_2 + 2`, ..., `a_n` becomes `a_n + n`).
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
        
    #State: `n` is an integer (1 ≤ `n` ≤ 3 · 10^5); `a` is a list of unique integers sorted in descending order; `counter` is a Counter object with each element's count decremented by 1; `cur` is 0; `cnt` is 0; `ans` is a list of `n` elements, including all elements from `a` and additional elements inserted in descending order to reach the length `n`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `n` is an integer (1 ≤ `n` ≤ 3 · 10^5); `a` is a list of unique integers sorted in descending order; `counter` is a Counter object with each element's count decremented by 1; `cur` is 0; `cnt` is 0; `ans` is a list of `n` elements, including all elements from `a` and additional elements inserted in descending order to reach the length `n`.
    print(*ans)
    #This is printed: [elements of ans separated by spaces] (where ans is a list of n elements constructed from the list a and additional elements in descending order to reach the length n)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` integers `a`. It modifies each element `a_i` by adding `i + 1` to it. Then, it constructs a new list `ans` of `n` elements by including all unique modified elements in descending order and filling any remaining slots with additional elements in descending order to reach the length `n`. Finally, it prints the elements of `ans` separated by spaces.

