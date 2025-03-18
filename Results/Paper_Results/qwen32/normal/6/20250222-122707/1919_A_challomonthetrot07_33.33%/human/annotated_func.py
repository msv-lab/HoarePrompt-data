#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it receives two integers a and b (1 ≤ a, b ≤ 10^9) representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        
        if a == b:
            print('Bob')
        elif a == 1:
            print('Alice')
        elif b == 1:
            print('Bob')
        elif a % 2 == 1:
            print('Bob')
        elif a % 2 == 0 and b % 2 == 1:
            print('Alice')
        elif a > b:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop has executed `T` times, with `i` equal to `T`. The values of `a` and `b` reflect the last test case processed. The variable `T` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers representing the number of coins Alice and Bob have. It determines the winner based on specific conditions and prints either "Alice", "Bob", or implicitly "Bob" in cases not explicitly covered by the conditions.

