#State of the program right berfore the function call: Each test case consists of two distinct non-negative integers x and y such that 0 ≤ x, y ≤ 10^9 and x ≠ y. The number of test cases t satisfies 1 ≤ t ≤ 10^4.
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
        
    #State: the sequence of printed values for each test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two distinct non-negative integers, and prints a specific value based on the relationship between the two integers. For each test case, it calculates the absolute difference between the two integers and applies different logic to determine the output value, which is then printed.

