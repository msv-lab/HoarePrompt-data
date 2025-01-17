#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and s is a binary string of length n consisting of only characters '0' and '1'. Additionally, the sum of n² over all test cases does not exceed 10⁴.
def func_1():
    input = sys.stdin.read
    data = input().split()
    index = 0
    num_cases = int(data[index])
    index += 1
    results = []
    for _ in range(num_cases):
        n = int(data[index])
        
        index += 1
        
        s = data[index]
        
        index += 1
        
        dp = [0] * (n + 1)
        
        result = 0
        
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                dp[i] = n - i + dp[i + 1]
            else:
                dp[i] = dp[i + 1]
        
        result = sum(dp[:n])
        
        results.append(result)
        
    #State of the program after the  for loop has been executed: `index` is `num_cases + 1`, `results` is a list containing the sum of the first `n` elements of `dp` for each case, `data` is a list of strings, `s` is the last string processed, `dp` is a list of length `n + 1` where each element is calculated based on the presence of '1's in the string `s` from index `-1` to `n-1`, `n` is the number of cases processed, `result` is the sum of the first `n` elements of `dp` for the last case.
    for res in results:
        print(res)
        
    #State of the program after the  for loop has been executed: `results` is a non-empty list, `index` is `num_cases + 1`, `data` is a list of strings, `s` is the last string processed, `dp` is a list of length `n + 1` where each element is calculated based on the presence of '1's in the string `s` from index `-1` to `n-1`, `n` is the number of cases processed, `result` is the sum of the first `n` elements of `dp` for the last case, `res` contains the value of each element in the `results` list, the loop prints each element in `results`.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of an integer `n` and a binary string `s` of length `n`. For each test case, it calculates a dynamic programming array `dp` where `dp[i]` represents the sum of indices from `i` to `n-1` that are marked as '1' in the string `s`. The function then sums up the first `n` elements of `dp` and appends this sum to the `results` list. After processing all test cases, it prints each element in the `results` list. The function handles edge cases such as empty input strings or test cases where `n` is 1. If `n` is 1, `dp` is initialized with a single element `0`, and the result is directly set to 0 since there are no indices to sum.

