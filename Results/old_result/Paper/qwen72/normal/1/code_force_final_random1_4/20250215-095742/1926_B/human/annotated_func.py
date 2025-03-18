#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 10, representing the size of the grid. Each grid is represented by n lines of n characters, where each character is either '0' or '1'. The grid contains exactly one triangle or one square that includes all '1's, and the shape's size is greater than 1.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `n` is an integer such that 2 ≤ n ≤ 10, the grid is represented by n lines of n characters, where each character is either '0' or '1', the grid contains exactly one triangle or one square that includes all '1's, and the shape's size is greater than 1, `a` is the initial value of `a` (unchanged), `i` is `a - 1`, `b` is the last input string provided by the user, `k` is a list containing the count of '1's in each input string `b` that contained at least one '1' during all iterations of the loop. If the first two elements of `k` are equal (`k[0] == k[1]`), the program has printed 'SQUARE' for each iteration where this condition was true. Otherwise, the program has printed 'TRIANGLE' for each iteration where this condition was false.
#Overall this is what the function does:The function `func` processes a series of test cases, each involving a grid of '0's and '1's. It reads the number of test cases `t` and for each test case, it reads the size of the grid `n` and the grid itself. The function then counts the number of '1's in each row of the grid that contains at least one '1'. If the count of '1's in the first two rows is the same, it prints 'SQUARE'; otherwise, it prints 'TRIANGLE'. After processing all test cases, the function has printed 'SQUARE' or 'TRIANGLE' for each test case based on the pattern of '1's in the grid.

