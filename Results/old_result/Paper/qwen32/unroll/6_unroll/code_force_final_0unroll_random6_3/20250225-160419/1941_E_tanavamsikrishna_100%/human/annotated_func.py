#State of the program right berfore the function call: row is a list of integers representing the depths in a single row of the river grid, and d is an integer representing the maximum distance between supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: `row` is a list where the first element is 1 and each element from index 1 to `d-1` is increased by 2, with the rest of the elements unchanged.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: `row` is a list where the first `d` elements are initialized as `1 + 2*i` for `i` from 0 to `d-1`, and each element from index `d` to `n-1` is updated based on the value of the last popped element from `min_heap`, the original value of `row[i]`, and 1; `min_heap` is a heapified list of tuples `(row[i], i)` for all indices `i` from 0 to `n-1`.
    return row[-1]
    #The program returns the last element of `row`, which is the result of the last update operation involving the last popped element from `min_heap`, the original value of `row[-1]`, and 1.
#Overall this is what the function does:The function `func_1` modifies a given list `row` of integers by setting the first element to 1 and incrementing the next `d-1` elements by 2. It then updates the remaining elements of `row` based on a min-heap data structure, which considers the maximum distance `d` between supports. Finally, the function returns the last element of the modified `row`.

#State of the program right berfore the function call: n is a positive integer representing the number of rows, m is a positive integer representing the number of columns such that m >= 3, k is a positive integer representing the number of bridges such that 1 <= k <= n, d is a positive integer representing the maximum distance between supports such that 1 <= d <= m.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: - The `total_costs` list will contain sums of `k` consecutive elements from the `costs` list.
    #   - The number of elements in `total_costs` will be `len(costs) - (k - 1)`, which is equivalent to `n - (k - 1)` because `len(costs) == n`.
    #
    #The final output state will be:
    #
    #Output State:
    print(min(total_costs))
    #This is printed: - The `print(min(total_costs))` statement will print the smallest sum of `k` consecutive elements from the `costs` list.
    #
    #Since the exact values of `costs` and `k` are not provided, we cannot compute the exact numerical value of `min(total_costs)`. However, based on the structure of the problem, the print statement will output the minimum sum of `k` consecutive elements from the `costs` list.
    #
    #Output:
#Overall this is what the function does:The function reads input values for the number of rows (`n`), columns (`m`), number of bridges (`k`), and maximum distance between supports (`d`). It then calculates the minimum sum of costs for `k` consecutive rows, where each row's cost is determined by a separate function `func_1` with the maximum distance `d`. The function outputs this minimum sum.

