#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but it should internally handle multiple test cases. Each test case consists of an integer `n` (2 ≤ n ≤ 10) representing the size of the grid, followed by `n` lines of `n` characters each, where each character is either '0' or '1'. The grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, and the shape's size is greater than 1. The number of test cases `t` is an integer (1 ≤ t ≤ 100).
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
        
    #State: The loop iterates `a` times. For each iteration, it reads an integer `n` and then `n` lines of input to form a grid. If the grid contains a shape (either a triangle or a square) that includes all the '1's and the number of '1's in the first two rows of the shape is the same, it prints the list `k` containing the count of '1's in each row of the shape. The variable `a` remains unchanged after the loop finishes. The variable `k` is reset to an empty list at the start of each iteration.
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case involves reading an integer `n` (2 ≤ n ≤ 10) and then `n` lines of `n` characters each, where each character is either '0' or '1'. The function counts the number of '1's in each row that contains at least one '1'. If the number of '1's in the first two rows is the same, it prints the list `k` containing these counts. The function does not return any value; it only prints the list `k` for qualifying test cases. The variable `a` remains unchanged after the function concludes.

