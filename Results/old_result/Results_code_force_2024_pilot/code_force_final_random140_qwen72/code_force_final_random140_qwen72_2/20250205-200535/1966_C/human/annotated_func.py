#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of an integer n where 1 ≤ n ≤ 2·10^5, representing the number of piles, followed by a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        ans = 1
        
        s = [0] + s
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans = 1 - ans
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: After all iterations, `t` is an integer where 1 ≤ t ≤ 10^4, `_` is a placeholder variable, `n` is the length of `s`, `arr` is a list of integers from the input, `s` is a list containing 0 followed by the unique elements from `arr`, `i` is `n - 1`, `ans` is 1 if the number of iterations is odd or if the loop breaks due to a difference greater than 1, and 0 if the number of iterations is even. For each test case, if `n` is 2, `ans` is 1, and the output is 'Alice'. If `n` is greater than 2, the output is 'Alice' if `ans` is 1, otherwise 'Bob'.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by an integer `n` and a list of `n` integers representing the number of stones in each pile. For each test case, it determines and prints the winner of a game between Alice and Bob based on the following rules: If the list of unique stone counts (including 0) has exactly two elements, Alice wins. Otherwise, the function iterates through the sorted unique stone counts and toggles a flag (`ans`) based on whether the difference between consecutive elements is 1. If the final value of `ans` is 1, Alice wins; otherwise, Bob wins. The function does not return any values but prints the winner ('Alice' or 'Bob') for each test case.

