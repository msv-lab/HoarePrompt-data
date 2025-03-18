#State of the program right berfore the function call: The function `func` is expected to take input through standard input, where the first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following t test cases consists of two lines: the first line contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The variable `tc` is 0, and the loop has processed all the test cases. The values of `n`, `arr`, and `dp` are not preserved between iterations and are redefined in each iteration of the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case includes the number of piles and the initial number of stones in each pile. For each test case, it determines whether Alice or Bob wins a game based on the piles of stones and prints the winner. The function processes all test cases and exits once all have been processed. The state of the program after the function concludes is that all test cases have been read and processed, and the results for each test case have been printed. The variables `tc`, `n`, `arr`, and `dp` are not preserved between test cases and are redefined for each iteration.

