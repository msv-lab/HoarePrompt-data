#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of n integers where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. The sum of n over all test cases does not exceed 3⋅10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4, n is an input integer such that 1 ≤ n ≤ 3⋅10^5, `a` is a list of integers where each element a[i] is increased by (i + 1) for all i in the range of n.
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
        
    #State: `counter` is a Counter object with updated counts for each integer in `a`. `t` remains unchanged. `n` remains unchanged. `a` remains unchanged. `cnt` is 0. `ans` is a list containing all integers from `a[0]` to the smallest integer in `a` minus one, repeated according to the conditions inside the loop.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: `counter` is a Counter object with updated counts for each integer in `a`. `t` remains unchanged. `n` remains unchanged. `a` remains unchanged. `cnt` is 0. `ans` is an empty list.
    print(*ans)
    #This is printed: []
#Overall this is what the function does:The function processes a list of integers `a` for each test case. It first increments each element in `a` by its index plus one. Then, it creates a sorted list of unique elements from `a`, calculates the difference between consecutive elements, and constructs a new list `ans` based on these differences and the counts of each element. Finally, it appends additional elements to `ans` to ensure it contains all integers from the smallest element in `a` down to one, and prints the resulting list `ans`.

