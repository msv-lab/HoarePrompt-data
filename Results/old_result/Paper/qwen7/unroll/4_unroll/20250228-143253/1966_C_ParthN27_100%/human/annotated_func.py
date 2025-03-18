#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the initial number of stones in each pile. It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: Alice or Bob will be printed based on the input test cases. For each test case, if there exists at least one pair of consecutive elements in the sorted unique list of stone piles (with an added 0 at the beginning) such that their difference is greater than 1, the game starts with Alice's turn and she wins ('Alice' is printed). Otherwise, if no such pair exists, Bob wins ('Bob' is printed). The exact output depends on the input values for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) (number of test cases), an integer \( n \) (number of piles), and a list of \( n \) integers representing the number of stones in each pile. For each test case, it determines whether Alice or Bob wins a game based on the sorted unique list of stone piles. If there exists at least one pair of consecutive elements in the sorted list (with an added 0 at the beginning) such that their difference is greater than 1, Alice wins. Otherwise, Bob wins. The function prints 'Alice' or 'Bob' for each test case based on this condition.

