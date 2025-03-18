#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2·10^5, representing the number of piles, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func():
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, n):
            dp = arr[i] - arr[i + 1] > 1 or not dp
        
        print('Alice' if dp else 'Bob')
        
        tc -= 1
        
    #State: `tc` is 0, `t` is an integer where 1 ≤ t ≤ 10^4, `n` is the length of `arr` minus 1, `arr` is a list of unique integers from the input, sorted in descending order, followed by 0, `i` is `n - 1`, `dp` is `True` if any difference between consecutive elements in `arr` (excluding the last element which is 0) is greater than 1, otherwise `dp` is `False`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers representing the number of stones in each pile. It then determines and prints whether "Alice" or "Bob" wins based on the condition that any difference between consecutive unique, sorted (in descending order) pile sizes (excluding the last 0) is greater than 1. After processing all test cases, the function terminates with `tc` set to 0, `n` being the length of the processed list minus 1, `arr` being the unique, sorted list of integers followed by 0, and `dp` being `True` if the winning condition is met, otherwise `False`.

