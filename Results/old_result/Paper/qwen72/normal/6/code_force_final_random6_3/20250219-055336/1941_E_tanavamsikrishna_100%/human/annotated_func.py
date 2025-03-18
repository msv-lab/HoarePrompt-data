#State of the program right berfore the function call: row is a list of non-negative integers where row[0] and row[-1] are initially 0, and d is a positive integer such that 1 <= d < len(row).
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: `row` is a list of non-negative integers where `row[0]` is 1, `row[1]` to `row[d-1]` each have their values increased by 2, and `row[-1]` is 0; `d` must be greater than 0 and less than the length of `row`; `i` is `d-1`.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: The loop has completed all its iterations. `row` is a list of non-negative integers where `row[0]` is 1, `row[1]` to `row[d-1]` each have their values increased by 2, and `row[-1]` is 0; `d` is greater than 0 and less than the length of `row`; `i` is equal to the length of `row`; `min_heap` is a min-heap containing elements from `row[:d]` with their indices, but the first `d` elements and their indices have been removed, and the tuples `(row[j], j)` for `j` from `d` to the length of `row` - 1 have been added to the heap. Each element in `row` from `row[d]` to `row[-2]` has been updated to `e[0] + row[j] + 1` where `e` is the last value popped from `min_heap` and did not satisfy the loop condition.
    return row[-1]
    #The program returns 0.
#Overall this is what the function does:The function `func_1` accepts a list `row` of non-negative integers with the first and last elements being 0, and a positive integer `d` such that 1 <= d < len(row). It modifies the list `row` by setting the first element to 1, increasing each element from index 1 to d-1 by 2, and updating each element from index d to the second-to-last element based on the minimum values from a heap. The function always returns 0, which is the last element of the list `row`.

#State of the program right berfore the function call: The function does not take any parameters, but it reads input from the standard input. The first line of input contains four integers n, m, k, and d such that 1 ≤ k ≤ n ≤ 100 and 3 ≤ m ≤ 2 · 10^5 and 1 ≤ d ≤ m. The next n lines each contain m integers representing the depths of the river cells, where 0 ≤ a_{i, j} ≤ 10^6 and a_{i, 1} = a_{i, m} = 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `n` must be at least `k`, `i` is `n - k + 1`, `costs` is a list of length `n`, `total_costs` is a list with `n - k + 1` elements, where each element is the sum of `k` consecutive elements in `costs`, starting from index `0` to `n - k`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where min(total_costs) is the minimum sum of any k consecutive elements in the costs list)
#Overall this is what the function does:The function reads input from the standard input, which includes four integers `n`, `m`, `k`, and `d`, followed by `n` lines of `m` integers representing the depths of river cells. It calculates the cost for each row using a helper function `func_1` and then finds the minimum sum of `k` consecutive row costs. The function prints this minimum sum. After the function concludes, `n` is at least `k`, `costs` is a list of length `n`, and `total_costs` is a list with `n - k + 1` elements, where each element is the sum of `k` consecutive elements in `costs`.

