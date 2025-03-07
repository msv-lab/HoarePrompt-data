#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an input integer such that 1 ≤ n ≤ 3 · 10^5; `a` is a list of `n` integers where each integer `a_i` is the original `a_i` plus `i + 1`.
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
        
    #State: `t` is unchanged; `n` is unchanged; `a` is unchanged; `counter` has adjusted counts based on the elements added to `ans`; `cnt` is reduced by the number of elements added to `ans` beyond `len(a)`; `ans` contains all elements from `a` plus additional elements inserted between consecutive elements of `a` based on the conditions specified.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `t` is unchanged; `n` is unchanged; `a` is unchanged; `counter` is unchanged; `cnt` is unchanged; `ans` contains all elements from `a` plus `cnt` additional elements, each being one less than the previous element.
    print(*ans)
    #This is printed: all elements of `a` followed by `cnt` additional elements, each being one less than the previous element (where the additional elements start from `a[-1] - 1` and decrement by 1 for each subsequent element)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `a` of `n` integers. It modifies the list by adding the index plus one to each element, then constructs a new list `ans` that includes all unique elements from the modified list `a` in descending order, with additional elements inserted between consecutive elements of `a` based on specific conditions. Finally, it prints the elements of `ans`.

