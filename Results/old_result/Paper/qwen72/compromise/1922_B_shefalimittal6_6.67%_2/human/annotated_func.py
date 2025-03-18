#State of the program right berfore the function call: The function `func` is expected to take input parameters, but they are not defined in the provided function signature. Based on the problem description, the function should take two parameters: an integer `t` representing the number of test cases, and for each test case, two lines of input: an integer `n` (1 ≤ n ≤ 3 · 10^5) and a list of integers `a` (0 ≤ a_i ≤ n) of length `n`. The sum of `n` over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has completed all iterations, and the final state is as follows:
#Overall this is what the function does:The function `func` accepts an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of integers `a` of length `n`. The function calculates the number of valid triplets of indices (i, j, k) such that i < j < k and a[i] = a[j] = a[k], and the number of valid pairs of indices (i, j) such that i < j and a[i] = a[j], multiplied by the count of all other distinct elements in the list. The result for each test case is printed to the console. After processing all test cases, the function completes and the program returns to its calling context.

