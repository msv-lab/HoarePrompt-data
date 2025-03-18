#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'Alice' or 'Bob', depending on the input values for `a` and `b` in each iteration of the loop. Specifically, the output will be determined by the conditions inside the loop as follows:
    #
    #- If `a` equals `b`, it prints 'Bob'.
    #- If `a` equals 1, it prints 'Alice'.
    #- If `b` equals 1, it prints 'Bob'.
    #- If `a` is odd, it prints 'Bob'.
    #- If `a` is even and `b` is odd, it prints 'Alice'.
    #- If `a` is greater than `b`, it prints 'Bob'.
    #- Otherwise, it prints 'Alice'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( T \) and pairs of positive integers \( a \) and \( b \). For each test case, it prints either 'Alice' or 'Bob' based on specific conditions involving \( a \) and \( b \). The possible outputs are determined as follows: if \( a \) equals \( b \), it prints 'Bob'; if \( a \) equals 1, it prints 'Alice'; if \( b \) equals 1, it prints 'Bob'; if \( a \) is odd, it prints 'Bob'; if \( a \) is even and \( b \) is odd, it prints 'Alice'; if \( a \) is greater than \( b \), it prints 'Bob'; otherwise, it prints 'Alice'.

