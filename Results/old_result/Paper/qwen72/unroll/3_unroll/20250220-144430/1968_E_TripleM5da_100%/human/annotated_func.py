#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases, where each test case is defined by an integer `n` (2 ≤ n ≤ 10^3). The function should internally manage the input and output for these test cases, selecting `n` cells in an `n x n` grid to maximize the size of the set \(\mathcal{H}\) of distinct Manhattan distances between any pair of cells.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: The loop has finished executing all iterations. For each test case defined by an integer `n`, the function has printed the coordinates (1, 1), (1, 2), and then (i, i) for i ranging from 3 to n. The variable `i` in the loop head is now equal to the number of test cases, and the variable `n` in the loop body is unchanged for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input, where each test case is defined by an integer `n` (2 ≤ n ≤ 10^3). For each test case, it prints the coordinates (1, 1), (1, 2), and then (i, i) for i ranging from 3 to n. The function does not return any value; it only prints the selected coordinates for each test case. After the function concludes, the input test cases have been processed, and the coordinates for each test case have been printed to the standard output.

