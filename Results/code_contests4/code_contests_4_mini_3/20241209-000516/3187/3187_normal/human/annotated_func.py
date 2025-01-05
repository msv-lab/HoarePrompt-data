#State of the program right berfore the function call: The function does not take any input parameters. It operates under the constraints of 1 ≤ n ≤ 100 for the number of colors and 0 ≤ m ≤ min(1000, (n(n-1))/(2)) for the number of harmonizing pairs. The pairs of colors that harmonize are provided as input in the form of m lines following the initial input. Each color is numbered from 1 to n, and the total number of rooks must not exceed 5000, with the coordinates of the rooks being in the range of 1 ≤ x, y ≤ 10^9.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m = rints()
    edges, ans = [rints() for _ in range(m)], [[] for _ in range(n)]
    for i in range(1, n + 1):
        ans[i - 1].append([i, i])
        
    #State of the program after the  for loop has been executed: `ans` is a list containing `n` lists, each containing pairs `[i, i]` for `i` from 1 to `n`.
    for (i, j) in enumerate(edges):
        ans[j[0] - 1].append([i + n + 1, j[0]])
        
        ans[j[1] - 1].append([i + n + 1, j[1]])
        
    #State of the program after the  for loop has been executed: `ans` is a list where each sublist at index `j[0] - 1` and `j[1] - 1` contains pairs of the form `[i + n + 1, j[k]]` for each edge `(j[0], j[1])` in `edges`, with `i` ranging from 0 to `m - 1`, where `m` is the number of edges.
    for i in range(n):
        print(len(ans[i]))
        
        for j in ans[i]:
            print(*j)
        
    #State of the program after the  for loop has been executed: `ans` is a list with at least `n` sublists, `i` is `n - 1` after the last iteration, and all elements in each sublist `ans[k]` for `k` in range `n` have been printed.
#Overall this is what the function does:The function does not take any parameters and processes a given number of colors and harmonizing pairs, printing the number of pairs associated with each color and the pairs themselves. It constructs an adjacency-like list where each color has its own list of pairs, including self-pairs and harmonizing pairs, and outputs this structure. However, it does not handle any edge cases or errors related to input beyond the specified constraints, assuming the input is always valid.

