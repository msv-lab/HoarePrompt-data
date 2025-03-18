#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4; `i` is `t-1` (indicating the last iteration of the loop); `n` is the input integer for the last test case; `l` is the list of integers obtained from the input for the last test case; `e` is a set of unique integers from the list `l` for the last test case; `m` is the length of the list `l` for the last test case. If 1 is in the list `l`, then `e` includes the integer 1 and `m` is at least 1. Otherwise, 1 is not in the list `l`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of piles and the number of stones in each pile. For each test case, it determines and prints the winner of a game based on whether the number 1 is present in the list of stones. If 1 is present, Bob wins; otherwise, Alice wins.

