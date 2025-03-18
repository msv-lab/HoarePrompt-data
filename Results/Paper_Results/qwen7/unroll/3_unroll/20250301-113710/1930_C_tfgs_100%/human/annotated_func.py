#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case consists of an integer n such that 1 ≤ n ≤ 3⋅10^5, and a list of n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3⋅10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, n is an input integer, and the list a is a list of integers where each element a[i] is increased by (i + 1) for every iteration i in the range of n.
    #
    #In more detail: After the loop executes all the iterations, each element a[i] in the list a will be incremented by (i + 1), where i ranges from 0 to n-1.
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
        
    #State: `ans` is a list containing elements from `a` with gaps filled based on the differences between consecutive elements and the value of `cnt` and `cur`. `counter` is updated to reflect the remaining counts of each element in `a`. `t`, `n`, `cnt`, and `cur` are unchanged.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: `ans` is a list containing `cnt` consecutive elements where each element is 1 less than the previous element (starting from the last element of the initial `ans`). `counter` is updated to reflect the remaining counts of each element in `a`. `t`, `n`, `cnt`, and `cur` are unchanged.
    print(*ans)
    #This is printed: 3 2 1
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer `n` and a list of `n` integers. It first increments each element in the list by its index plus one. Then, it creates a list `ans` by sorting the unique elements of the modified list in descending order, filling in gaps between consecutive elements based on certain conditions, and appending `cnt` consecutive decreasing elements to the end of `ans`. Finally, it prints the resulting list `ans`.

