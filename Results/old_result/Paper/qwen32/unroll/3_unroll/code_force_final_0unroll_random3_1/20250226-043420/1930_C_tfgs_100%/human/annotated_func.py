#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the input integer such that 1 ≤ n ≤ 3 · 10^5; `a` is a list of `n` integers where each integer a_i is the sum of the original a_i and i + 1, satisfying 2 ≤ a_i ≤ 10^9 + n.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the input integer such that 1 ≤ n ≤ 3 · 10^5; `a` is a list of unique integers where each integer `a_i` is the sum of the original `a_i` and `i + 1`, satisfying 2 ≤ a_i ≤ 10^9 + n, sorted in descending order; `counter` is a Counter object representing the frequency of each element in the original `a`; `cur` is the remaining count of elements in `counter` that have not been fully used; `cnt` is the remaining count of elements that could have been inserted between the elements of `a`; `ans` is the final sequence of numbers.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `ans` is a list that includes its initial elements followed by `cnt` additional elements, each element being one less than the previous one.
    print(*ans)
    #This is printed: The initial elements of the list `ans` followed by `cnt` additional elements, each element being one less than the previous one.
#Overall this is what the function does:The function processes a list of integers by adding an incrementing value to each element, then constructs a new list that includes unique elements from the modified list and additional elements to fill gaps between the unique elements in descending order. The final list is printed.

