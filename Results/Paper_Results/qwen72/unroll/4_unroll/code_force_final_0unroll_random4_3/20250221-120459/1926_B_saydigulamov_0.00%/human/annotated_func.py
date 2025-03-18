#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, n is an integer such that 2 <= n <= 10, and the grid is a list of n strings, each string consisting of n characters that are either '0' or '1'. The grid contains exactly one triangle or one square, and the shape's size is greater than 1.
def func():
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print(k)
        
    #State: t remains an integer such that 1 <= t <= 100, n remains an integer such that 2 <= n <= 10, grid remains a list of n strings, each string consisting of n characters that are either '0' or '1', a remains the same input integer. The list k is populated with the counts of '1's in each input string b, but only if '1' is present in b. If the first two counts in k are equal, k is printed.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `a` from the input, and for each value from 0 to `a-1`, it reads a series of strings (each representing a row of a grid) until it finds a row containing at least one '1'. It then counts the number of '1's in each such row and stores these counts in a list `k`. If the first two counts in `k` are equal, the list `k` is printed. The function does not modify the initial state of the program (i.e., `t`, `n`, and `grid` remain unchanged).

