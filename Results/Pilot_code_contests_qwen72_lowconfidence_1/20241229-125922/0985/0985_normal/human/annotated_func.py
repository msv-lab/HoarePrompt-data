#State of the program right berfore the function call: H and W are integers such that 1 ≤ H, W ≤ 500; a_{ij} is an integer such that 0 ≤ a_{ij} ≤ 9 for all 1 ≤ i ≤ H and 1 ≤ j ≤ W.
def func_1():
    H, W = map(int, raw_input().split())
    a = []
    result = []
    for i in range(H):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `H` is an integer such that 1 ≤ H ≤ 500, `W` is an integer such that 1 ≤ W ≤ 500, `a` is a list containing `H` lists of integers, each list having `W` integers, `result` is an empty list, `i` is `H - 1`
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 0:
                continue
            elif j + 1 < W:
                result.append([i + 1, j + 1, i + 1, j + 2])
                a[i][j] = a[i][j] - 1
                a[i][j + 1] = a[i][j + 1] + 1
            elif j + 1 == W and i + 1 < H:
                result.append([i + 1, j + 1, i + 2, j + 1])
                a[i][j] = a[i][j] - 1
                a[i + 1][j] = a[i + 1][j] + 1
        
    #State of the program after the  for loop has been executed: `H` is an integer such that 1 ≤ H ≤ 500, `W` is an integer such that 1 ≤ W ≤ 500, `a` is a list containing `H` lists of integers, each list having `W` integers, where all elements in `a` are even. `result` is a list containing operations that were performed to adjust the elements of `a` to ensure all elements are even. Each operation in `result` is a list of four integers representing the indices of the elements that were adjusted. If the loop does not execute (i.e., if `H` is 0 or `W` is 0), `result` remains an empty list.
    print(len(result))
    for i in range(len(result)):
        for j in range(len(result[i])):
            if j == len(result[i]) - 1:
                print(result[i][j])
            else:
                print(result[i][j]),
        
    #State of the program after the  for loop has been executed: `H` is an integer such that 1 ≤ H ≤ 500, `W` is an integer such that 1 ≤ W ≤ 500, `a` is a list containing `H` lists of integers, each list having `W` integers, where all elements in `a` are even, `result` is a list with a length of 0, and no elements in `result` have been printed.
#Overall this is what the function does:The function `func_1` reads a 2D array (matrix) of dimensions H x W from user input, where H and W are integers such that 1 ≤ H, W ≤ 500, and each element \(a_{ij}\) is an integer such that 0 ≤ \(a_{ij}\) ≤ 9. It processes the matrix to ensure all elements are even by performing the following operations: If an element is odd, it either increments the adjacent element to the right or below (if possible) and decrements itself to make it even. The function then prints the number of operations performed and the details of each operation. The final state of the program is that the matrix `a` contains only even numbers, and the operations performed are printed to the console. If the matrix is empty (i.e., H or W is 0), no operations are performed, and the function prints 0.

