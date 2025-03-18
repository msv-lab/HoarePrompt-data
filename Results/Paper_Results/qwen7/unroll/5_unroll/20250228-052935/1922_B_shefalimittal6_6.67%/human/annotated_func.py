#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n for all i where 1 ≤ i ≤ n. The sum of all n over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: The output state will be a series of integers representing the value of `res` after each iteration of the loop, printed for each input integer `t`. Each `res` is calculated based on the frequency of numbers in the input list `nums`, using combinations to count the number of ways to select specific counts of numbers.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a positive integer \( t \) (the number of test cases), followed by a positive integer \( n \) and a list of \( n \) non-negative integers. It then calculates and prints the number of ways to select specific counts of numbers from the list, using combinations. The final output consists of a series of integers, each representing the result for each test case.

