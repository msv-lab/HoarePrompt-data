#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, there are two integers a and b such that 1 <= a, b <= 10^9.
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
        
    #State: The loop has executed `T` times, and for each pair of integers `a` and `b` read from the input, the program has printed the winner ('Alice' or 'Bob') based on the given conditions. The variables `a` and `b` hold the values of the last pair processed, and `i` equals `T`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b` and prints the name of the winner ('Alice' or 'Bob') based on specific conditions.

