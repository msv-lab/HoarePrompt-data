#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2·10^5, representing the number of piles. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 10^9, representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: After all iterations of the loop, `t` remains an integer where 1 ≤ t ≤ 10^4, `tc` is 0 (since it has been decremented by 1 for each iteration until it reaches 0), `n` is the number of unique integers in `arr` and must be greater than 0 for each test case, `a_1, a_2, ..., a_n` are integers where 1 ≤ a_i ≤ 10^9, `arr` is a list of unique integers from the input, sorted in descending order, followed by a 0 for each test case, `i` is `n-1` for each test case, and `dp` is `True` if any of the differences `arr[j] - arr[j + 1] > 1` for `j` in the range `[1, n-1]` or if the original `dp` was `True` for each test case, otherwise `dp` is `False`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers representing the initial number of stones in each pile. It then processes these inputs to determine the winner of a game between Alice and Bob based on specific rules. The function prints "Alice" if the game can be won by Alice under optimal play conditions, otherwise, it prints "Bob". After processing all test cases, the function terminates with `tc` set to 0, and the state of other variables (`n`, `arr`, `dp`, etc.) being irrelevant as they are local to each test case.

