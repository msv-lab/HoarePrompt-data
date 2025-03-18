#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        s.sort()
        
        s = [0] + s
        
        ans = 1
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans ^= 1
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: ['Alice' or 'Bob' for each test case]
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of piles and the number of stones in each pile. For each test case, it determines the winner of a game where players take turns removing stones, and prints either 'Alice' or 'Bob' based on who wins the game.

