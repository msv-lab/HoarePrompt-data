#State of the program right berfore the function call: row is a list of integers where row[0] and row[-1] are 0, and d is a positive integer such that 1 <= d < len(row).
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: row[0] is 1, row[-1] is 0, and for each i in the range 1 to d-1, row[i] is row[i] + 2.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: For each `i` in the range `d` to `len(row) - 1`, `row[i]` is `row[i] + 2 * (i - d + 1) + 1`. `min_heap` is a min-heap of tuples where each tuple is (`row[i]`, `i`) for `i` in the range 0 to `len(row) - 1`.
    return row[-1]
    #The program returns the value of `row[-1]`, which is `row[len(row) - 1] + 2 * (len(row) - 1 - d + 1) + 1
#Overall this is what the function does:The function `func_1` accepts a list `row` of integers where the first and last elements are 0, and a positive integer `d` such that 1 <= d < len(row). It modifies the list `row` by setting `row[0]` to 1 and incrementing each element in the range 1 to d-1 by 2. For each element in the range `d` to `len(row) - 1`, it updates the element based on the minimum value from a sliding window of size `d` in the list, adding 1 to the sum of the element and the minimum value. The function returns the value of `row[-1]`, which is the last element of the modified list.

#State of the program right berfore the function call: No variables are passed in the function signature, but the function reads input values where n, m, k, and d are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 · 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, each containing m integers where the first and last integers in each row are 0, representing the river banks.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `n`, `m`, `k`, `d`, `rows`, `costs`, and `total_costs` where `total_costs` is a list of sums of `k` consecutive elements from `costs`. The length of `total_costs` is `len(costs) - (k - 1)`. The other variables remain unchanged.
    print(min(total_costs))
    #This is printed: - The `print(min(total_costs))` statement will print the smallest sum of `k` consecutive elements in the `costs` list.
    #
    #Given the initial state and the structure of the problem, the output will be the minimum value in the `total_costs` list, which is the smallest sum of `k` consecutive elements in the `costs` list.
    #
    #Output:
#Overall this is what the function does:The function `func_2` reads input values `n`, `m`, `k`, and `d` (integers) and a list `rows` (a list of `n` lists, each containing `m` integers with the first and last integers being 0). It computes the minimum sum of `k` consecutive elements from a list of costs, where each cost is the result of applying `func_1` to each row in `rows` with the parameter `d`. The function prints this minimum sum and does not return any value. After the function concludes, the variables `n`, `m`, `k`, `d`, `rows`, `costs`, and `total_costs` are defined, with `total_costs` containing the sums of `k` consecutive elements from `costs`.

