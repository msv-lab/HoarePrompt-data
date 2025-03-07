#State of the program right berfore the function call: The function is designed to handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 3 · 10^5) representing the number of sticks, and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) where each a_i represents the exponent of the length of the i-th stick, which is 2^{a_i}. The total number of test cases, t, is an integer (1 ≤ t ≤ 10^4), and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has processed all test cases, and for each test case, it has printed the number of ways to choose three sticks such that no two sticks have the same length, and the number of ways to choose two sticks of the same length and one stick of a different length. The variables `t`, `n`, `num_of_lens`, `nums`, `cnt`, `res`, and `total_sum` are reset or updated for each test case, but the overall state of the program remains ready to handle the next input or terminate if all test cases have been processed.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` and a list of `n` integers representing the exponents of stick lengths. For each test case, it calculates and prints the number of ways to choose three sticks such that no two sticks have the same length, and the number of ways to choose two sticks of the same length and one stick of a different length. After processing all test cases, the function terminates, and the program is ready to handle new input or end.

