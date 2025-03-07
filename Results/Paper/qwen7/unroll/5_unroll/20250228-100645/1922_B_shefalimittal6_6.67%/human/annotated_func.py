#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n. The sum of all n over all test cases does not exceed 3 ⋅ 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        num_of_lens = {}
        
        nums = list(map(int, input().split()))
        
        for x in nums:
            num_of_lens[x] = num_of_lens.get(x, 0) + 1
        
        res = 0
        
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += math.comb(cnt, 3)
            if cnt >= 2:
                total_sum = sum(i for i in num_of_lens.values() if i != cnt)
                res += math.comb(cnt, 2) * total_sum
        
        print(res)
        
    #State: A series of integers representing the value of `res` for each iteration of the loop. Each value of `res` is calculated based on the input values of `n` and the list of integers `nums` for that particular iteration.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t` indicating the number of subsequent test cases, a positive integer `n`, and a list `a` of non-negative integers. For each test case, it calculates a result based on the frequency of integers in the list `a`. Specifically, it counts the number of ways to choose 3 or 2 integers from each frequency group and sums these values to produce the final result for each test case. The function then prints the result for each test case.

