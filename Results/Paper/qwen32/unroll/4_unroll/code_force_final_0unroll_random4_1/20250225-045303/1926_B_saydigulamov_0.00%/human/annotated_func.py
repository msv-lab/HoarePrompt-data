#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 2 <= n <= 10, and the grid is an n x n list of strings where each string consists of n characters, each character being either '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid, and the size of the triangle or square is greater than 1.
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
        
    #State: `t` is an integer such that 1 <= t <= 100; `n` is an integer such that 2 <= n <= 10; `grid` is an n x n list of strings where each string consists of n characters, each character being either '0' or '1', and the grid contains exactly one triangle or exactly one square that contains all the '1's in the grid, and the size of the triangle or square is greater than 1; `a` is an input integer. The loop has finished executing all `a` iterations without any further changes to `t`, `n`, or `grid`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and an `n x n` grid of strings consisting of '0's and '1's. It then counts the number of '1's in each row that contains at least one '1'. If the counts of '1's in the first two rows are equal, it prints the list of counts. The function does not return any specific value; it only prints output for certain test cases.

