#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a single row, and d is an integer representing the maximum distance between supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: row[0] is 1, and row[i] for i in the range [1, d-1] is increased by 2 compared to its initial value.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: `row[i]` for `i` in the range `[d, len(row))` is updated to `e[0] + row[i] + 1` where `e` is the element popped from `min_heap` that satisfies the condition `e[1] <= i - (d + 2)`. The `min_heap` contains tuples `(row[i], i)` for all `i` from `d` to `len(row) - 1`.
    return row[-1]
    #The program returns the updated value of `row[-1]` which is `e[0] + row[-1] + 1`, where `e` is the tuple popped from `min_heap` that satisfies the condition `e[1] <= len(row) - (d + 3)`
#Overall this is what the function does:The function modifies a list of integers (`row`) by updating certain elements based on a specified distance (`d`). It returns the updated value of the last element in the list after performing these modifications.

#State of the program right berfore the function call: n and m are positive integers representing the number of rows and columns in the grid respectively, k is a positive integer representing the number of consecutive rows for building bridges such that 1 <= k <= n, d is a positive integer representing the maximum distance between supports, rows is a 2D list of integers representing the depth of the river cells with dimensions n x m, and the first and last elements of each row in rows are 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `n`, `m`, `k`, and `d` are positive integers with `n` being at least `k`; `rows` is a 2D list of integers with dimensions `n` x `m`; `costs` is a list of length `n` where each element is the result of `func_1` applied to the corresponding row in `rows`; `total_costs` is a list containing the sum of each consecutive `k` elements of `costs` from `costs[0]` to `costs[n-k]`; `i` is `n-k`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of each consecutive k elements of costs)
#Overall this is what the function does:The function calculates and prints the minimum total cost of building bridges over a series of river rows, considering constraints on the number of consecutive rows (`k`) and the maximum distance between supports (`d`). The input includes the number of rows (`n`), columns (`m`), the number of consecutive rows for building bridges (`k`), the maximum distance between supports (`d`), and a 2D list (`rows`) representing the depth of the river cells. The function returns the minimum total cost among all possible sets of `k` consecutive rows.

