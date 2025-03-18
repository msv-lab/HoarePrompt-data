#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, the first line contains an integer n (2 ≤ n ≤ 10) representing the size of the grid. The next n lines each contain n characters, which are either '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid, and the size of the triangle or square is greater than 1 (i.e., the shape cannot consist of exactly one '1').
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
        
    #State: `a` is an integer such that 1 ≤ a ≤ 100, `i` is equal to `a - 1`, and `k` is a list containing the counts of '1's from all strings `b` that contained '1' during the `a` iterations. If `k[0]` is equal to `k[1]`, then the condition `k[0] == k[1]` holds true and `k` is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an `n x n` grid of '0's and '1's. For each test case, it counts the number of '1's in each row that contains at least one '1'. If the counts of '1's in the first two rows that contain '1's are equal, it prints the list of these counts.

