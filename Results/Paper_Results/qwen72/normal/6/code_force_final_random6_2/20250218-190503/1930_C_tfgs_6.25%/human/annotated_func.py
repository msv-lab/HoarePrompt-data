#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer provided by the user, `a` is a list of `n` integers provided by the user, where 1 ≤ a_i ≤ 10^9. The sum of `n` over all test cases does not exceed 3 · 10^5, `i` is `n-1`, `a[0]` is increased by 1, `a[1]` is increased by 2, ..., `a[n-1]` is increased by `n`.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer provided by the user, `a` is a list of unique integers sorted in descending order, `i` is `len(a) - 1`, `counter` is a Counter object that counts the occurrences of each integer in the updated list `a` (all counts are 0 or negative because each element in `a` has been decremented at least once), `cnt` is 0, `ans` is a list containing all elements of `a` and additional elements that were added to fill the gap between consecutive elements in `a` to ensure the total length of `ans` is `n`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer provided by the user, `a` is a list of unique integers sorted in descending order, `i` is `len(a) - 1`, `counter` is a Counter object that counts the occurrences of each integer in the updated list `a` (all counts are 0 or negative), `cnt` is 0, `ans` is a list containing all elements of `a` and additional elements to ensure the total length of `ans` is `n + cnt` (where `cnt` is the initial value of `cnt`), the last `cnt` elements of `ans` are a sequence of integers decrementing by 1 starting from `ans[-cnt-1] - 1`.
    print(*ans)
    #This is printed: 10 8 6 4 2
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `a` of `n` integers from the user. It then modifies the list `a` by incrementing each element by its index plus one. After this, it removes duplicates from `a`, sorts the list in descending order, and constructs a new list `ans` that contains all unique elements from `a` and additional elements to ensure the total length of `ans` is `n`. The additional elements are chosen to fill the gaps between consecutive elements in the sorted list `a` and are decremented by 1 from the last element of `a` if necessary. Finally, the function prints the elements of `ans` separated by spaces. The function does not return any value.

