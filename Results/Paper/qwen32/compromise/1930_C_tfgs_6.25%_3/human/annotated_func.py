#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 3 · 10^5) representing the length of the array a, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The function will be called multiple times (1 ≤ t ≤ 10^4) with different test cases, and the sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Each element `a[i]` in the array `a` is incremented by `i + 1` for `i` ranging from `0` to `n-1`.
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
        
    #State: `a` remains unchanged; `counter` is a `Counter` object with all values decremented to 0; `cnt` is 0; `ans` is a list containing all elements from `a` in the same order, with additional elements inserted between them based on the difference between consecutive elements in `a` and the remaining count `cnt`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `a` remains unchanged; `counter` is a `Counter` object with all values decremented to 0; `cnt` is 0; `ans` is a list containing all elements from `a` in the same order, with additional elements inserted between them based on the difference between consecutive elements in `a` and the initial count `cnt`, and an additional `cnt` elements, each being the last element of `ans` minus 1, sequentially.
    print(*ans)
    #This is printed: a1 a2 a3 ... an (where a1, a2, a3, ..., an are the elements of the list `a`)
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers from the input. It modifies each element of the list by adding its 1-based index to it. Then, it constructs a new list by inserting additional elements between the sorted unique values of the modified list, based on the differences between consecutive elements and a count of duplicates. Finally, it prints the resulting list.

