#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3. The loop has printed pairs of integers (1, 1), (1, 2), and for each integer i from 3 to n, it has printed (i, i).
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer between 1 and 50. For each test case, it accepts an integer `n` between 2 and 10^3. It prints the pairs (1, 1), (1, 2), and for each integer `i` from 3 to `n`, it prints the pair (i, i). The function does not return any value.

