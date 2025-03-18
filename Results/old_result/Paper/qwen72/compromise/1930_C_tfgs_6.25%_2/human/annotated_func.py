#State of the program right berfore the function call: t is an integer such that 1 \leq t \leq 10^4, n is an integer such that 1 \leq n \leq 3 \cdot 10^5, and a is a list of n integers where each a_i satisfies 1 \leq a_i \leq 10^9. The sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 · 10^5, `a` is a list of n integers where each a_i satisfies 1 ≤ a_i ≤ 10^9, and after the loop, each `a[i]` is increased by `i + 1` for all 0 ≤ i < n.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 3 · 10^5, `a` is a list of unique integers sorted in descending order, `counter` is a Counter object that contains the frequency of each integer in the original list `a` but all values in `counter` are now 0, `cnt` is 0, `ans` is a list containing all elements from `a` and additional elements such that the total length of `ans` is `n`, and these additional elements are the largest possible integers that can be inserted between the elements of `a` without violating the uniqueness and descending order.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 3 · 10^5, `a` is a list of unique integers sorted in descending order, `counter` is a Counter object that contains the frequency of each integer in the original list `a` but all values in `counter` are now 0, `cnt` is 0, `ans` is a list containing all elements from `a` and additional elements such that the total length of `ans` is `n + cnt`, and the last `cnt` elements of `ans` are each one less than the previous element, starting from the last element of the initial `ans` list.
    print(*ans)
    #This is printed: 5 4 3 2 1
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `a` of `n` integers from the user. It modifies each element of `a` by adding `i + 1` to `a[i]` for all `0 ≤ i < n`. Then, it generates a new list `ans` that contains all unique elements from the modified `a` in descending order, along with additional integers that are the largest possible values that can be inserted between these unique elements without violating the uniqueness and descending order. If there are still remaining positions to fill, it appends the largest possible integers that are one less than the previous element, ensuring the final length of `ans` is `n`. The function prints the elements of `ans` in a single line separated by spaces.

