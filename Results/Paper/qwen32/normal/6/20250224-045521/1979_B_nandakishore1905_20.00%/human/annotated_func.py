#State of the program right berfore the function call: Each test case consists of two distinct non-negative integers x and y such that 0 <= x, y <= 10^9 and x != y. The function will be called with multiple test cases, where the first line contains an integer t (1 <= t <= 10^4) indicating the number of test cases, and each of the following t lines contains two integers x and y as described.
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
        
    #State: The sequence of printed values for each test case, where each printed value is determined by the logic described above for the corresponding `n` and `m`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two distinct non-negative integers. For each test case, it calculates a value based on the difference between the two integers and prints this value. The printed value is determined by specific conditions related to the difference being a power of two, the integers being zero, and the parity of the non-zero integer.

