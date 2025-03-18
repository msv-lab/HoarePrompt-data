#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) indicating the number of test cases. Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9) representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `test` is an integer representing the number of test cases (1 ≤ `test` ≤ 1000), `a` and `b` retain the values from the last iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers representing the number of coins Alice and Bob have. For each test case, it determines and prints the winner based on whether the sum of the coins is even or odd. If the sum is even, Bob wins; if odd, Alice wins.

