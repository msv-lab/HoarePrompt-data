#State of the program right berfore the function call: row is a list of non-negative integers representing the depths of the river cells in a single row, with row[0] and row[-1] being 0 (river banks). d is a positive integer such that 1 <= d < len(row).
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: `row` is a list of non-negative integers with `row[0]` set to 1, `row[-1]` is 0, and each element in `row` from index 1 to index `d-1` is increased by 2. The value of `d` remains unchanged.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: `row` is updated for indices from `d` to `len(row) - 1` based on the smallest element in `min_heap` within a certain range, and `min_heap` is a valid heap containing all elements of `row` and their indices.
    return row[-1]
    #The program returns the last element of the list `row`, which has been updated based on the smallest element in `min_heap` within a certain range.
#Overall this is what the function does:The function `func_1` accepts a list `row` of non-negative integers representing river depths, with the first and last elements being 0, and a positive integer `d` such that 1 <= d < len(row). It updates the list `row` by setting the first element to 1, increasing the elements from index 1 to index d-1 by 2, and then updating the elements from index d to the end based on the smallest element in a min-heap within a certain range. The function returns the last element of the updated list `row`.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads input from the standard input, where the first line contains four integers n, m, k, and d such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 * 10^5, and 1 ≤ d ≤ m. The following n lines each contain m integers representing the depths of the river cells, with the first and last elements of each row being 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `total_costs` is a list of sums of `k` consecutive elements from `costs`, starting from the first element up to the `(n - k + 1)`-th element. The lengths of `rows`, `costs`, and `total_costs` are `n`, `n`, and `n - k + 1` respectively. All other variables (`n`, `m`, `k`, `d`) remain unchanged.
    print(min(total_costs))
    #This is printed: - The `print(min(total_costs))` statement will print the smallest sum of `k` consecutive elements in the `costs` list.
    #
    #Since the exact values of `costs` and `k` are not provided, we can't compute the exact numerical value of `min(total_costs)`. However, based on the structure of the problem, the print statement will output the smallest sum of `k` consecutive elements in the `costs` list.
    #
    #Output:
#Overall this is what the function does:The function `func_2` reads input from the standard input, where the first line contains four integers `n`, `m`, `k`, and `d` (with constraints `1 ≤ k ≤ n ≤ 100`, `3 ≤ m ≤ 2 * 10^5`, and `1 ≤ d ≤ m`). The following `n` lines each contain `m` integers representing the depths of the river cells, with the first and last elements of each row being 0. The function processes these depths using the `func_1` function for each row, calculates the sum of `k` consecutive elements from the resulting list of costs, and prints the minimum sum of these `k` consecutive elements. The function does not return any value.

