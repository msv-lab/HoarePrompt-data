#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) for a test case, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The variable `t` remains unchanged, and the loop has printed the value of `res` for each of the `t` test cases. The variables `n`, `num_of_lens`, `nums`, `res`, `cnt`, `total_sum`, and `x` are reset for each iteration of the loop, and their final values after the loop completes are undefined (as they are local to each iteration).
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then calculates the number of valid triplets of indices (i, j, k) such that the elements at these indices are the same or two of them are the same and the third is different. The function prints the result for each test case. The function does not return any value; it only prints the results. After the function concludes, the variable `t` remains unchanged, and the loop has printed the value of `res` for each of the `t` test cases. The variables `n`, `num_of_lens`, `nums`, `res`, `cnt`, `total_sum`, and `x` are reset for each iteration of the loop, and their final values after the loop completes are undefined.

