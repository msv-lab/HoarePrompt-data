#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists stones where each sublist represents the piles of stones for a test case. Each sublist contains n integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^9 and 1 ≤ n ≤ 2·10^5. The sum of n over all test cases does not exceed 2·10^5.
def func():
    t = int(input())
    for tc in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        maxsize = max(a)
        
        a.sort()
        
        mexsize = 1
        
        for sz in a:
            if sz == mexsize:
                mexsize = mexsize + 1
        
        if mexsize > maxsize:
            print('Alice' if mexsize % 2 == 0 else 'Bob')
        else:
            print('Alice' if mexsize % 2 == 1 else 'Bob')
        
    #State: The loop has finished executing for all test cases. The variable `t` remains unchanged as it represents the number of test cases. The list `stones` remains unchanged as it is not modified within the loop. The loop has printed the result ('Alice' or 'Bob') for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases and then, for each test case, reads a list of integers `a` representing piles of stones. It determines the winner ('Alice' or 'Bob') based on the following rules: If the smallest non-negative integer not present in the sorted list of stones (`mexsize`) is greater than the maximum stone size (`maxsize`), the winner is 'Alice' if `mexsize` is even, and 'Bob' if `mexsize` is odd. Otherwise, the winner is 'Alice' if `mexsize` is odd, and 'Bob' if `mexsize` is even. The function prints the winner for each test case and does not return any value. The input list `stones` is not modified.

