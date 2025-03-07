#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, n is an integer such that 2 <= n <= 10, and the grid is a list of n strings, each of length n, containing only '0' or '1'. Each grid contains exactly one triangle or one square that includes all the '1's, and the shape's size is greater than 1.
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
        
    #State: The loop iterates `a` times. During each iteration, it reads `t` lines of input, each line being a string of length `n` containing only '0' or '1'. For each line that contains at least one '1', it counts the number of '1's and appends this count to the list `k`. If the first two counts in `k` are equal, it prints 'SQUARE'. Otherwise, it prints 'TRIANGLE'. The variables `t`, `n`, and `grid` remain unchanged, and `a` is decremented by the number of iterations completed.
#Overall this is what the function does:The function reads an integer `a` from the input, then for each of the `a` test cases, it reads an integer `t` and a grid of `t` strings, each of length `n`. It processes each grid to count the number of '1's in each row that contains at least one '1'. If the first two rows with '1's have the same count of '1's, it prints 'SQUARE'; otherwise, it prints 'TRIANGLE'. The function does not return any value and does not modify the input parameters `t`, `n`, or `grid`.

