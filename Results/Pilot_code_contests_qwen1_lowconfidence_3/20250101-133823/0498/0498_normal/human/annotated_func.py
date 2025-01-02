#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100 000. The input consists of n lines, where each line contains two integers x and y such that 0 ≤ x, y ≤ 100 000, representing points in the set. It is guaranteed that all points are distinct and if some point (x, y) is present, then all points (x', y'), such that 0 ≤ x' ≤ x and 0 ≤ y' ≤ y, are also present. The last line of the input contains n integers wi such that -100 000 ≤ wi ≤ 100 000, representing the required special values for the points.
def func_1():
    mem, mem2, out = Counter(w), defaultdict(list), []
    for (x, y) in a:
        mem2[y - x].append([x, y])
        
    #State of the program after the  for loop has been executed: `total` is an integer such that \(1 \leq n \leq 100,000\), `mem` is a Counter object counting the occurrences of elements in the list `w`, `mem2` is a defaultdict of lists where for every pair \((x, y)\) in `a`, \([x, y]\) is appended to `mem2[y - x]` exactly once, `out` is an empty list, `a` is a non-empty list containing at least one pair \((x, y)\)
    for (i, j) in mem.items():
        if len(mem2[i]) != j:
            print('NO')
            exit()
        
        mem2[i].sort(reverse=True)
        
    #State of the program after the  for loop has been executed: `total` is an integer such that \(1 \leq total \leq 100,000\), `mem` must contain at least one key-value pair, `mem2` is a defaultdict of lists where for every key `i` in `mem`, `mem2[i]` is sorted in descending order, `out` is an empty list, `a` is a non-empty list containing at least one pair \((x, y)\).
    for i in range(n):
        x, y = mem2[w[i]][-1]
        
        labels[x][y] = i + 1
        
        if i and labels[x + 1][y] < labels[x][y] or labels[x][y + 1] < labels[x][y]:
            print('NO')
            exit()
        
        out.append(' '.join(map(str, mem2[w[i]].pop())))
        
    #State of the program after the  for loop has been executed: `out` is a list of string representations of elements removed from `mem2[w[i]]` for each iteration, `mem2[w[i]]` is empty, `labels[x][y]` is populated based on the removed elements, and if the loop completes without exiting, no condition `labels[x + 1][y] < labels[x][y]` or `labels[x][y + 1] < labels[x][y]` is violated.
    print('YES')
    print('\n'.join(out))
#Overall this is what the function does:The function processes a series of points \((x, y)\) and their corresponding weights \(w_i\). It checks if the points form a valid grid where each cell \((x, y)\) is assigned a unique label based on the weights of the points that cover it. If the points and weights satisfy certain conditions, it outputs "YES" followed by the labels of the points. Otherwise, it outputs "NO". The function ensures that the labels are consistent with the given weights and the grid structure. If any inconsistency is found, it exits early with "NO".

