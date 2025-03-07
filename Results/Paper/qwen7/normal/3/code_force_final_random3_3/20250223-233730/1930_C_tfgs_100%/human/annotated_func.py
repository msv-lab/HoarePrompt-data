#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `i` is 3, `n` must be greater than or equal to 3, `a` is a list of integers obtained from splitting the input string by spaces, each element `a[j]` (where \(0 \leq j < n\)) is increased by \(j + 1\) for every iteration \(j\) from 0 to \(n-1\).
    #
    #This means that after the loop completes all its iterations, each element `a[j]` in the list `a` will have been incremented by the sum of all integers from 1 to `j + 1`. In mathematical terms, the value of `a[j]` will be `a[j] + (j + 1)`, where `j` ranges from 0 to `n-1`.
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
        
    #State: `cur` is 0, `cnt` is 0, `ans` contains `n` elements each calculated as `a[i - 1] - (adv - 1 - j) - 1` for `j` in the range of `adv`, and `counter` is an empty dictionary.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: `cur` is 0, `cnt` must be equal to 3, `ans` now has `n` elements where the last element is `ans[0] - 2` and all other elements remain the same, `counter` is an empty dictionary.
    #
    #Explanation: After the loop executes all 3 iterations, `cnt` will be 3. The loop body decrements the last element of `ans` in each iteration. Since the loop runs 3 times, the last element of `ans` will be decremented by 3 from its initial value, resulting in `ans[0] - 2`. All other elements in `ans` remain unchanged as they are not affected by the loop.
    print(*ans)
    #This is printed: x y1 y2 ... yn-1 x-2
#Overall this is what the function does:The function processes a list of integers `a` received as input, modifies it by incrementing each element by its index plus one, and then generates a new list `ans` based on certain conditions. Finally, it prints the elements of `ans`. The function does not accept any direct parameters but operates on data derived from standard input.

