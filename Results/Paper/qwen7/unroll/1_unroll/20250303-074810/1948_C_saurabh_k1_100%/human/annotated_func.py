#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even; the input consists of t test cases, each test case includes the dimensions of a 2x n grid with arrows pointing either left (<) or right (>).
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: Output State: `t` test cases, each test case outputs 'Yes' if no invalid configurations (where two consecutive left-pointing arrows face each other directly) are found in the 2x `n` grid, otherwise outputs 'No'.
#Overall this is what the function does:The function processes `t` test cases, where each test case includes an integer `n` (2 ≤ n ≤ 2⋅10^5 and n is even) and a 2xn grid with arrows pointing either left (<) or right (>). For each test case, it checks if there are any invalid configurations (where two consecutive left-pointing arrows face each other directly) in the grid. If such configurations are found, it prints 'No'; otherwise, it prints 'Yes'.

