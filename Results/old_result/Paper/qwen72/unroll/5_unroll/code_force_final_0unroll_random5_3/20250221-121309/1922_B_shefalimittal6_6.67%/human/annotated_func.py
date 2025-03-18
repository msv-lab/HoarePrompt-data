#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains an integer n (1 ≤ n ≤ 3 · 10^5) followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The variable `t` is decremented to 0, and the variables `n`, `num_of_lens`, `nums`, `res`, `cnt`, and `total_sum` are updated for each test case but their final values are not retained after the loop completes. The output state includes the printed results for each test case, which are the values of `res` calculated during each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then calculates the number of valid triplets that can be formed from these integers, where a valid triplet is defined as a set of three numbers that are either all the same or two are the same and the third is different. The function prints the result for each test case. After processing all test cases, the function does not return any value, but the output includes the printed results for each test case.

