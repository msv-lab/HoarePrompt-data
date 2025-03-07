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
        
    #State: After all iterations, `i` is equal to `a`, indicating that the loop has completed all iterations. The variable `_` is 0, indicating that the inner loop has completed all iterations for each test case. The list `k` contains the counts of '1' characters from each input string `b` where '1' was present, in the order the inputs were received. The variables `t`, `n`, `a`, and the grid remain unchanged as they are not modified within the loop. The variable `b` is the last input string provided during the final iteration. If the first element of `k` is equal to the second element of `k`, the condition holds true, and "SQUARE" is printed. Otherwise, "TRIANGLE" is printed.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a grid of size n (where 2 ≤ n ≤ 10) represented by '0's and '1's. For each test case, it determines whether the shape formed by '1's in the grid is a square or a triangle. It prints "SQUARE" if the count of '1's in the first two rows is the same, indicating a square, and "TRIANGLE" otherwise. The function does not return any value; it only prints the shape type for each test case. The original values of `t`, `n`, and the grid remain unchanged.

