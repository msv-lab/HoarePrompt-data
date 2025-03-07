#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 10) representing the size of the n x n grid. This is followed by n lines, each containing n characters that are either '0' or '1'. The grid contains exactly one shape, which is either a triangle or a square, and this shape is composed of all the '1's in the grid. The size of the shape (k) is greater than 1, meaning the shape cannot consist of a single '1'.
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
        
    #State: `a` remains the initial input value, and `i` is equal to `a`. The list `k` is recalculated in each iteration but is only printed if `k[0]` equals `k[1]`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an n x n grid of '0's and '1's. For each grid, it checks the number of '1's in the first two rows and prints the list of counts if they are equal. The function does not return any specific value; it only prints output under certain conditions.

