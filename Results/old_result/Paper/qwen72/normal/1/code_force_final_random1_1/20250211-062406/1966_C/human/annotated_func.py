#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2·10^5, representing the number of piles, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func():
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, len(arr)):
            dp = arr[i] - (arr[i + 1] if i < n else 0) > 1 or not dp
        
        print('Alice' if dp else 'Alice')
        
        tc -= 1
        
    #State: After the loop has executed all its iterations, `tc` will be 0, indicating that all test cases have been processed. For each test case, the value of `dp` will be `False` if there exists any pair of consecutive elements in `arr` (excluding the last element which is `0`) such that their difference is less than or equal to 1. Otherwise, `dp` will be `True`. The variable `n` will be the length of `arr` minus 1, and `arr` will be a sorted list of unique integers in descending order, followed by a `0`. The value of `i` will be `len(arr) - 1` for each iteration, but it will not persist outside the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` and a list of `n` integers representing the number of stones in each pile. For each test case, the function determines whether the game can be won by Alice under certain conditions and prints "Alice" for each test case. The function processes up to 10,000 test cases, and for each test case, it ensures that the list of stone counts is unique and sorted in descending order before performing the check. The final state of the program after processing all test cases is that `tc` is 0, indicating all test cases have been processed.

