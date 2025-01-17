#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i <= n for all 0 <= i < n.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    positions = []
    for i in range(n):
        positions.append((i + 1, i + 1))
        
    #State of the program after the  for loop has been executed: `n` must be greater than or equal to 0; `positions` is a list containing n tuples, each tuple being `(i + 1, i + 1)` where `i` ranges from 0 to `n - 1`.
    visit = [-1] * n
    for i in range(n):
        found = False
        
        for j in range(n):
            if i != j:
                dist = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] -
                    positions[j][1])
                if dist == a[i]:
                    visit[i] = j + 1
                    found = True
                    break
        
        if not found:
            print('NO')
            return
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `positions` is a list of `n` tuples, each initially containing `(i + 1, i + 1)` where `i` ranges from 0 to `n - 1`, `visit` is a list of length `n` where each element is `-1`, and for each `i` in `range(n)`, `visit[i]` is set to `j + 1` if a valid `j` (where `i != j`) is found such that the Manhattan distance between `positions[i]` and `positions[j]` is equal to `a[i]`, otherwise `visit[i]` remains `-1`.
    print('YES')
    for pos in positions:
        print(pos[0], pos[1])
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `positions` is a list of `n` tuples, each initially containing `(i + 1, i + 1)`, and `visit` is a list of length `n` where each element is not `-1`; the output of the print statement is a sequence of tuples `(x, y)` where each tuple represents a position in `positions`. For each `i` in `range(n)`, there exists a `j` (where `i != j`) such that the Manhattan distance between `positions[i]` and `positions[j]` is equal to `a[i]`.
    print(' '.join(map(str, visit)))
#Overall this is what the function does:The function processes a list of integers `a` of size `n` and checks if it is possible to assign coordinates to `n` positions such that the Manhattan distance between each position `i` and another position `j` equals `a[i]` if `i` is not equal to `j`. If such an assignment is possible, it prints "YES" followed by the coordinates of the positions and the indices of the positions that satisfy the distance conditions. Otherwise, it prints "NO". The function does not accept any parameters and does not return any value.

