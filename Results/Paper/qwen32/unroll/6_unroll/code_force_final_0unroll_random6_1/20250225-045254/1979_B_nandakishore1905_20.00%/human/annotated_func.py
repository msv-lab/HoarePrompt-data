#State of the program right berfore the function call: Each test case consists of two distinct non-negative integers x and y such that 0 <= x, y <= 10^9 and x != y. The function will be called multiple times, with the number of test cases t satisfying 1 <= t <= 10^4.
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
        
    #State: a series of printed values, each corresponding to the output of the loop for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two distinct non-negative integers `n` and `m`. For each test case, it calculates a specific value based on the difference between `n` and `m` and prints this value. The printed value is determined by specific conditions related to the difference being a power of two, or whether one of the integers is zero and the other is odd or even.

