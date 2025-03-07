#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9 and x != y.
def func():
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: `x` and `y` are distinct non-negative integers such that 0 <= x, y <= 10^9 and x != y, `i` is the number of iterations specified by the user input, `n` and `m` are input integers greater than 0, `k` is the absolute difference between `n` and `m`. If `k` is a power of 2, the program retains the initial state of the variables. Otherwise, if `n` is 0 and `m` is even or odd, the program retains the initial state of the variables. If neither of these conditions is met, `l` is the binary representation of `k` without the '0b' prefix, `p` is the length of the binary representation of `k`, and `q` is 2 raised to the power of (p - 1).
#Overall this is what the function does:The function `func` reads an integer `i` from user input, which specifies the number of iterations to perform. For each iteration, it reads two integers `n` and `m` from user input, calculates the absolute difference `k` between `n` and `m`, and prints a value based on the following conditions: If `k` is a power of 2, it prints `k`. If `n` is 0 and `m` is odd, it prints 1. If `n` is 0 and `m` is even, it prints 2. Otherwise, it calculates the highest power of 2 less than `k` and prints the difference between `k` and that power of 2. The function does not return any value; it only prints the results to the console.

