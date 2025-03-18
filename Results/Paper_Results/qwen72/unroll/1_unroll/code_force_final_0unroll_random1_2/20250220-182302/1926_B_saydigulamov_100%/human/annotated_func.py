#State of the program right berfore the function call: The function `func` is expected to be called within a context that provides the input as described, but the function definition itself does not explicitly take any parameters. The input context should include a single integer t (1 ≤ t ≤ 100) indicating the number of test cases, followed by t test cases, each starting with an integer n (2 ≤ n ≤ 10) representing the size of the grid, and then n lines of n characters each, where each character is either '0' or '1'. The grid contains exactly one triangle or one square that includes all '1's, and the shape size is greater than 1.
def func():
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print('SQUARE')
        else:
            print('TRIANGLE')
        
    #State: The loop will print 'SQUARE' or 'TRIANGLE' for each test case based on the input grid, and the variable `a` will be decremented by the number of iterations it has completed. The variable `k` will be reset to an empty list at the beginning of each iteration. The input grid and other variables outside the loop will remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases, each containing a grid of '0's and '1's. It reads the number of test cases `t` from the input, and for each test case, it reads the grid size `n` and the grid itself. The function then counts the number of '1's in each row of the grid. If the first two rows have the same number of '1's, it prints 'SQUARE'; otherwise, it prints 'TRIANGLE'. After processing all test cases, the function terminates, and the input grid and other variables outside the function remain unchanged.

