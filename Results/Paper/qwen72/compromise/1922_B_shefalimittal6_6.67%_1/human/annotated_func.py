#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains n (1 ≤ n ≤ 3 · 10^5) integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents of the stick lengths. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n` integers from the input, counts the occurrences of each integer, and calculates the number of ways to choose 3 sticks of the same length or 2 sticks of the same length and one stick of a different length. The result for each test case is printed. After all iterations, the loop finishes and the final state is that `t` is unchanged, and the input has been fully processed. The variables `num_of_lens`, `nums`, and `res` are reset for each test case.
#Overall this is what the function does:The function `func` reads input from the user to process `t` test cases, where each test case involves a list of `n` integers representing the exponents of stick lengths. For each test case, it calculates the number of ways to choose 3 sticks of the same length or 2 sticks of the same length and one stick of a different length. The result for each test case is printed to the console. The function does not return any value; instead, it directly outputs the results. After processing all test cases, the function completes, and the input has been fully processed. The variable `t` remains unchanged, and the internal variables are reset for each test case.

