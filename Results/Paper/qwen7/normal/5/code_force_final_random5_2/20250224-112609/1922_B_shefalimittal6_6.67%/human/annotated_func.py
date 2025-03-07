#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and the list a contains n non-negative integers such that 0 ≤ a_i ≤ n. The sum of all n values over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: After the loop executes all the iterations, `num_of_lens` will be an empty dictionary, as it gets reset for each iteration of the outer loop. The variable `res` will contain the sum of all combinatorial calculations performed over all integers in the `num_of_lens.values()` from all iterations of the loop, where for each `cnt` in `num_of_lens.values()` that is greater than or equal to 3, we add `math.comb(cnt, 3)` to `res`, and for each `cnt` that is greater than or equal to 2, we add `math.comb(cnt, 2) * total_sum` to `res`, with `total_sum` being the sum of all values in `num_of_lens.values()` except the current `cnt`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) indicating the number of subsequent test cases, followed by a positive integer \( n \) and a list of \( n \) non-negative integers. For each test case, it calculates a result based on the frequency of each integer in the list. Specifically, it counts the number of ways to choose 3 or more identical integers and pairs of identical integers, and sums these combinations to produce the final result for each test case. This process is repeated for each test case, and the results for all test cases are printed.

