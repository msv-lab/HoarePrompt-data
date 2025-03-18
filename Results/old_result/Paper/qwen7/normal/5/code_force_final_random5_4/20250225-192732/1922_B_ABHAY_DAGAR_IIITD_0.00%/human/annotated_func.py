#State of the program right berfore the function call: test_cases is a list of tuples. Each tuple contains two elements: an integer n representing the number of sticks, and a list of integers a where each a_i represents the exponent used to calculate the length of the i-th stick as 2^{a_i}.
def func_1(test_cases):
    results = []
    for _ in range(test_cases):
        n = int(input())
        
        num_list = list(map(int, input().split()))
        
        num_of_lens = {}
        
        for x in num_list:
            if x in num_of_lens:
                num_of_lens[x] += 1
            else:
                num_of_lens[x] = 1
        
        res = 0
        
        total_count = 0
        
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += cnt * (cnt - 1) * (cnt - 2) // 6
            if cnt >= 2:
                res += cnt * (cnt - 1) // 2 * total_count
            total_count += cnt
        
        results.append(res)
        
    #State: After all iterations of the loop have finished, `total_count` will be the sum of all values from `num_of_lens.values()` for every iteration. The variable `res` will contain the cumulative result of applying the formulas for each value in `num_of_lens` that meets the conditions across all iterations. The list `results` will contain the value of `res` after each iteration of the loop.
    for result in results:
        print(result)
        
    #State: `results` is a list containing all the elements from each iteration of the loop, `total_count` is the sum of all values from `num_of_lens.values()` for every iteration, `res` is the cumulative result of applying the formulas for each value in `num_of_lens` that meets the conditions across all iterations, and `result` is the last element in the list `results` after the loop has executed all its iterations.
#Overall this is what the function does:The function accepts a list of tuples `test_cases`, where each tuple contains an integer `n` and a list of integers `a`. For each tuple, it calculates the number of ways to choose three sticks such that the product of their lengths is a perfect cube and the number of ways to choose two sticks such that the product of their lengths is a perfect square. It then sums these counts across all tuples and appends the result to a list. Finally, it prints each result in the list.

