#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases, where each test case is defined by an integer `n` (2 ≤ n ≤ 10^3). The function should internally manage the input and output for these test cases.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: The loop has completed all its iterations, and `t` is now 0. For each test case, the output includes a sequence of numbers starting from '1 1' to '1 n', followed by a single space.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `n` (2 ≤ n ≤ 10^3) and prints a sequence of lines. Each line in the sequence contains the number '1' followed by a space and then the integer `i` (1 ≤ i ≤ n). After processing all test cases, the function completes and `t` is 0. The function does not return any value.

