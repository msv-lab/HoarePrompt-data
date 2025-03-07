#State of the program right berfore the function call: t is an integer such that 1 \leq t \leq 10^4, n is an integer such that 1 \leq n \leq 3 \cdot 10^5, and a is a list of n integers where 1 \leq a_i \leq 10^9. The sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: t remains an integer such that 1 ≤ t ≤ 10^4, n remains an input integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where each a_i has been updated to a_i + (i + 1). The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` remains an integer such that 1 ≤ t ≤ 10^4, `n` remains an input integer such that 1 ≤ n ≤ 3 · 10^5, `a` is a sorted list of unique integers in descending order where each `a_i` has been updated to `a_i + (i + 1)`, `counter` is a Counter object that contains the frequency of each integer in the original list `a` before the update, the sum of `n` over all test cases does not exceed 3 · 10^5, `cur` is 0, `cnt` is 0, `ans` is a list containing all integers from the original list `a` plus additional integers that fill the gaps between the updated values of `a` such that the length of `ans` is `n`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `t` remains an integer such that 1 ≤ t ≤ 10^4, `n` remains an input integer such that 1 ≤ n ≤ 3 · 10^5, `a` is a sorted list of unique integers in descending order where each `a_i` has been updated to `a_i + (i + 1)`, `counter` is a Counter object that contains the frequency of each integer in the original list `a` before the update, `cur` is 0, `cnt` is 0, `ans` is a list containing all integers from the original list `a` plus additional integers that fill the gaps between the updated values of `a` such that the length of `ans` is `n`.
    print(*ans)
    #This is printed: [a_0 + 1, a_1 + 2, a_2 + 3, ..., a_m + (m + 1), additional integers to fill the gaps] (where the additional integers are the next smallest integers not already in the list to ensure the length of `ans` is `n`)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` integers `a` from the user. It then updates each element `a_i` in the list `a` to `a_i + (i + 1)`. After updating, it generates a new list `ans` that contains all unique updated values from `a` in descending order, along with additional integers to fill any gaps between these values, ensuring the final length of `ans` is `n`. The function prints the elements of `ans` in a single line separated by spaces. The variables `t`, `n`, and `a` are not modified outside of the function's scope, and the function does not return any value.

