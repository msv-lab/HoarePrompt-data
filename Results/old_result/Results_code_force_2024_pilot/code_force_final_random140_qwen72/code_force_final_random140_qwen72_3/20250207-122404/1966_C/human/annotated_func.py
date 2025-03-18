#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2·10^5, representing the number of piles, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: After all iterations of the loop, `t` is 0, `_` is `t` (initial value of `t`), `n` is the length of `s` for the last test case, `arr` is the list of integers from the last test case, `s` is a list containing 0 followed by all unique elements of the last `arr`, `i` is `n-1` if `n` is 2, otherwise `i` is `n-2`. `ans` is 1 if the loop broke due to the condition `s[i] - s[i - 1] > 1` being true at some point during the iterations of the last test case, or 0 if the loop did not break due to this condition.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by an integer `n` and a list of `n` integers representing the number of stones in each pile. For each test case, it determines and prints whether "Alice" or "Bob" wins based on the unique values in the list of stones. If the list contains only one unique value, "Alice" wins. Otherwise, it iterates through the sorted unique values and toggles a win state based on the difference between consecutive values. If the difference is greater than 1 at any point, the loop breaks, and the current win state is used to determine the winner. The function does not return any values; it only prints the results for each test case. After processing all test cases, the function concludes without modifying any global state.

