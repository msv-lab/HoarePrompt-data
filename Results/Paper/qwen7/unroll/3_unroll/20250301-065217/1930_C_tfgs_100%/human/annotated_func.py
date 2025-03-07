#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4, n is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5, `a` is a list of integers where each element a[i] (for 0 ≤ i < n) is increased by (i + 1) after the loop executes all the iterations.
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
        
    #State: counter is a Counter object that counts the occurrences of each integer in the updated list `a`, `a` is a sorted list of unique integers where each element a[i] (for 0 ≤ i < n) is increased by (i + 1), `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5, `cur` is the sum of `counter[a[i]]` for all elements in `a`, `cnt` is 0, `ans` is a list containing all elements of `a` followed by additional elements generated based on the differences between consecutive elements in `a`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: `counter` remains unchanged, `a` remains unchanged, `t` remains unchanged, `n` remains unchanged, `cur` remains unchanged, `cnt` is the number of times the loop iterates, `ans` is a list containing all elements of `a` followed by `cnt` additional elements, each of which is one less than the previous element in `ans`.
    print(*ans)
    #This is printed: what is printed is a list of elements where all elements of `a` are followed by `cnt` additional elements, each of which is one less than the previous element in `ans`
#Overall this is what the function does:The function processes a list of integers `a` for each test case. It first modifies each element in `a` by adding its index position plus one. Then, it creates a frequency counter for the modified list, removes duplicates, sorts the list in descending order, and calculates the difference between consecutive elements. Based on these differences, it generates additional elements to form the final output list `ans`. Finally, it prints the list `ans`, which consists of all elements from the modified list `a` followed by additional elements that are one less than the previous element until a certain count `cnt` is reached.

