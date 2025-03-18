#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with an integer n (1 ≤ n ≤ 2⋅10^5) representing the number of piles. This is followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: tc is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of piles and the number of stones in each pile. For each test case, it determines the winner of a game where two players take turns removing stones from the piles, with the rule that a player can only remove stones from a pile if it has more stones than the next pile, and the player who cannot make a move loses. The function outputs 'Alice' if Alice wins the game and 'Bob' if Bob wins.

