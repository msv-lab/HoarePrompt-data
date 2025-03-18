#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 · 10^5 and `n` must be greater than 0, `a` is a list of `n` integers where each integer `a_i` is such that 1 ≤ a_i ≤ 10^9, `i` is `n-1`, `a[0]` is increased by 1, `a[1]` is increased by 2, ..., `a[n-1]` is increased by `n`.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 · 10^5 and `n` must be greater than 0, `a` is a list of unique integers where each integer `a_i` was originally in the range 1 ≤ a_i ≤ 10^9 and has been increased by `i + 1` (where `i` ranges from 0 to `n-1`), and `a` is now sorted in descending order, `i` is `len(a) - 1`, `counter` is a Counter object that counts the occurrences of each integer in the updated and now unique list `a`, but the count of each element in `a` is decreased by 1, `cnt` is 0, `ans` is a list containing all elements of `a` in their original order, and additional elements that fill the gaps between consecutive elements of `a` such that the total number of elements in `ans` is `n`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 · 10^5 and `n` must be greater than 0, `a` is a list of unique integers where each integer `a_i` was originally in the range 1 ≤ a_i ≤ 10^9 and has been increased by `i + 1` (where `i` ranges from 0 to `n-1`), and `a` is now sorted in descending order, `i` is `len(a) - 1`, `counter` is a Counter object that counts the occurrences of each integer in the updated and now unique list `a`, but the count of each element in `a` is decreased by 1, `cnt` is 0, `ans` is a list containing all elements of `a` in their original order, and additional elements that fill the gaps between consecutive elements of `a` such that the total number of elements in `ans` is `n + cnt`. The last element of `ans` is `ans[-1] - cnt`.
    print(*ans)
    #This is printed: 11 10 9 8 7
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `a` of `n` integers from the user. It then modifies each element in `a` by adding its index plus one to it. After this, it processes `a` to create a new list `ans` that contains all unique elements from `a` in descending order, along with additional integers that fill the gaps between consecutive elements in `a` to ensure the length of `ans` is `n`. Finally, it prints the elements of `ans` in a space-separated format. The function does not return any value.

