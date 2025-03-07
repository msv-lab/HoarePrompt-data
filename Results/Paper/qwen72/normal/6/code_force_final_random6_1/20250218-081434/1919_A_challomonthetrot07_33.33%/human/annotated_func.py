#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a and b are integers such that 1 <= a, b <= 10^9.
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
        
    #State: `T` is greater than or equal to the number of iterations, `i` is `T-1`, and for each iteration, `a` and `b` are the input integers. If `a` is equal to `b`, the relationship between `a` and `b` remains unchanged. If `a` is not equal to `b`, the following conditions apply: If `a` is 1, `a` remains 1. If `a` is not 1, `a` retains its value and parity (odd or even). If `b` is 1, `b` remains 1. If `b` is not 1, `b` retains its value and parity (odd or even). The relationship between `a` and `b` (whether `a` is greater than, less than, or equal to `b`) remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `T` from the input, representing the number of test cases, where `1 <= T <= 1000`. For each test case, it reads two integers `a` and `b` from the input, where `1 <= a, b <= 10^9`. It then determines and prints the winner ('Alice' or 'Bob') based on the following rules: If `a` is equal to `b`, 'Bob' wins. If `a` is 1, 'Alice' wins. If `b` is 1, 'Bob' wins. If `a` is odd, 'Bob' wins. If `a` is even and `b` is odd, 'Alice' wins. If `a` is greater than `b`, 'Bob' wins. Otherwise, 'Alice' wins. After processing all test cases, the function concludes, and the state of the program is unchanged except for the output printed to the console.

