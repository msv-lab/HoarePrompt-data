#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 3 · 10^5), which is the length of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9), which are the elements of the array a. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `a` is a list of `n` integers where each element at index `i` is increased by `i + 1`.
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
        
    #State: `a` remains unchanged, `counter` has each count of elements in `a` decremented by 1, `cur` is the sum of the counts of all elements in `a` after decrementing each by 1, `cnt` is `n - len(a)` minus the total number of elements added to `ans` that are not part of the original list `a`, and `ans` contains all elements of `a` in their original order, plus additional elements inserted between them based on the `adv` calculations.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `a` remains unchanged, `counter` has each count of elements in `a` decremented by 1, `cur` is the sum of the counts of all elements in `a` after decrementing each by 1, `cnt` is 0, and `ans` contains all elements of `a` in their original order, plus additional elements inserted between them based on the `adv` calculations, plus `cnt` additional elements, each being the last element of `ans` at the time of the iteration minus 1.
    print(*ans)
    #This is printed: elements of `a` in their original order, plus additional elements inserted based on `adv` calculations
#Overall this is what the function does:The function processes an array of integers by incrementing each element by its 1-based index, then constructs a new list by inserting additional elements between the sorted unique elements of the modified array based on specific rules, and finally prints the resulting list.

