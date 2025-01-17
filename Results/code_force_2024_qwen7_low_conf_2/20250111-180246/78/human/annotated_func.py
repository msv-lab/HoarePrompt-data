#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of n, m, and k where 2 <= n, m <= 10^9 and 2 <= k <= 2 * 10^5. The coordinates of k fountains are given as pairs of integers (r_i, c_i) such that 1 <= r_i <= n and 1 <= c_i <= m, and all coordinates are distinct and none of them is (n, 1).
def func():
    t = int(input())
    for z in range(t):
        n, m, k = map(int, input().split())
        
        c = []
        
        for i in range(k):
            x, y = map(int, input().split())
            c.append((y, x, i))
        
        c.sort()
        
        f = [(1, 0, 0)]
        
        s = 0
        
        answer = [0] * k
        
        for i in range(k):
            if c[i][1] > f[-1][1]:
                s += (c[i][0] - 1) * (c[i][1] - f[-1][1])
                f.append((c[i][0], c[i][1], c[i][2]))
        
        answer[f[-1][2]] = 1
        
        for i in range(1, len(f) - 1):
            if f[i][0] < f[i + 1][0]:
                answer[f[i][2]] = 1
        
        print(s + (n - f[-1][1]) * m)
        
        print(*answer)
        
    #State of the program after the  for loop has been executed: `i` is `k`, `z` is less than `t`, `f` is a list of `k` elements, including \((1, 0, 0)\) and tuples \((c[i][0], c[i][1], c[i][2])\) where \( c[i][1] > f[-1][1] \) for \( i \) from \( 0 \) to \( k-1 \), `answer` is a list of `k` ones, each `answer[f[j][2]]` is 1 if \( f[j][0] < f[j + 1][0] \) for \( j \) in the range \([1, len(f) - 2]\), `n` and `m` are as given, `k` is the number of fountains, and `c` is a list of `k` tuples sorted based on the first element of each tuple.
#Overall this is what the function does:The function processes multiple test cases, each containing integers \(n\), \(m\), and \(k\) representing the dimensions of a grid and the number of fountains respectively. The coordinates of \(k\) fountains are provided as pairs of integers \((r_i, c_i)\). The function calculates and prints the area of the smallest rectangle that can cover all the fountains and a sequence indicating which fountains are on the boundary of this rectangle. Specifically, the function:
1. Reads the number of test cases \(t\).
2. For each test case, reads \(n\), \(m\), and \(k\), then the coordinates of \(k\) fountains.
3. Sorts the fountains based on their row coordinates.
4. Constructs a list of boundary points, starting with \((1, 0, 0)\), and iteratively adds new points that have a higher row coordinate than the previous point.
5. Calculates the area of the smallest rectangle covering all fountains by summing up the vertical distances between consecutive boundary points and the horizontal distance from the first point to the last point.
6. Determines which fountains lie on the boundary of this rectangle by checking if their row coordinate is strictly greater than the previous boundary point’s row coordinate.
7. Prints the total area and the sequence of 1s and 0s indicating whether each fountain is on the boundary or not.
8. Handles the case where the coordinates of the fountains do not include \((n, 1)\).

The function assumes that the input data meets the specified constraints and that the coordinates of the fountains are unique and within the grid boundaries. Potential edge cases include:
- The case where no fountains are on the boundary (all fountains lie on a single horizontal line).
- The case where the fountains' coordinates do not include \((n, 1)\), requiring special handling.

