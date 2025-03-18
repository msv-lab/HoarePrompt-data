#State of the program right berfore the function call: The function should take two parameters: `t` (an integer representing the number of test cases, where 1 ≤ t ≤ 10^4) and `test_cases` (a list of tuples, where each tuple contains an integer `n` (1 ≤ n ≤ 2·10^5) and a list of integers `a` (1 ≤ a_i ≤ 10^9) representing the number of piles and the initial number of stones in each pile, respectively). The sum of `n` over all test cases does not exceed 2·10^5.
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
        
    #State: `tc` is `0`, `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4), `test_cases` is a list of tuples where each tuple contains an integer `n` (1 ≤ n ≤ 2·10^5) and a list of integers `a` (1 ≤ a_i ≤ 10^9), the sum of `n` over all test cases does not exceed 2·10^5, `n` must be greater than or equal to the initial value of `n` for each test case, `arr` is a list of unique integers from the input, sorted in descending order, followed by 0, `dp` is the result of the condition `arr[n-1] - arr[n] > 1 or not dp` evaluated for the last iteration of each test case, `i` is `n-1` for each test case.
#Overall this is what the function does:The function `func` reads input from the user to process multiple test cases. For each test case, it reads the number of piles `n` and a list of integers `a` representing the initial number of stones in each pile. It then determines and prints the winner of a game between Alice and Bob based on the condition that Alice wins if the difference between any two consecutive unique, sorted piles (in descending order) is greater than 1, otherwise Bob wins. The function does not return any value but prints the winner for each test case. After processing all test cases, the function concludes with `tc` being 0.

