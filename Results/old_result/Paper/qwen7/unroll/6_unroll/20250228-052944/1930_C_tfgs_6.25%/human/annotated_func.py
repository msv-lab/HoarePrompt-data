#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, a is a list of integers where each element a[i] is initially a[i] + (i + 1) for 0 ≤ i < n, n is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5.
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
        
    #State: Output State: `counter` is a Counter object with updated counts for each element in the list `a`, `t` remains an integer such that 1 ≤ t ≤ 10^4, `a` is a sorted list of integers in descending order, `cnt` is reduced by the sum of `adv` values calculated during the loop, and `ans` is a list containing a sequence of integers generated based on the differences between consecutive elements in `a` and the remaining count of each element.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: `counter` is a Counter object with updated counts for each element in the list `a`, `t` remains an integer such that 1 ≤ t ≤ 10^4, `a` is a sorted list of integers in descending order, `cnt` is reduced by the sum of `adv` values calculated during the loop, and `ans` is a list where each element is reduced by 1 for each iteration of the loop, starting from the last element of `ans`.
    print(*ans)
    #This is printed: [n-1, n-2, ..., 1, 0]
#Overall this is what the function does:The function processes a list of integers `a` for each test case, where `n` is the length of the list. It first increments each element in the list by its index plus one. Then, it creates a sorted list of unique elements from the modified list in descending order. Based on the count of each unique element, it generates a new list `ans` where each element is adjusted according to the differences between consecutive unique elements and the remaining count of each element. Finally, it appends additional elements to `ans` to ensure the list contains `n` elements, each decremented by 1 from the previous element, and prints the resulting list.

