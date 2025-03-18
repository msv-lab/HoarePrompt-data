#State of the program right berfore the function call: row is a list of non-negative integers, and d is a positive integer such that 1 <= d <= len(row) - 2.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: `row` is a list where elements at indices 1 to d-1 are each incremented by 2 compared to the initial `row`, and all other elements remain unchanged.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: `row` is a list where elements at indices 1 to d-1 are each incremented by 2 compared to the initial `row`, and elements from index d to the end are updated by adding the smallest values from the heap plus the current values of the elements in the `row` list plus 1. `min_heap` is a heapified list of tuples reflecting these updated values.
    return row[-1]
    #The program returns the last element of the `row` list, which is updated by adding the smallest values from the heap plus the current values of the elements in the `row` list plus 1, starting from index `d` to the end.
#Overall this is what the function does:The function `func_1` takes a list `row` of non-negative integers and an integer `d` such that 1 <= d <= len(row) - 2. It modifies the elements of `row` starting from index `d` by adding the smallest values from a heap plus the current values of the elements in `row` plus 1, and returns the last element of the updated `row` list.

#State of the program right berfore the function call: n is a positive integer representing the number of rows, m is a positive integer representing the number of columns, k is a positive integer representing the number of bridges, d is a positive integer representing the maximum distance between supports, and rows is a 2D list of integers where each sublist represents a row in the grid with the first and last elements being 0 and the rest being non-negative integers.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `n` is the first input integer, `m` is the second input integer, `k` is the third input integer, `d` is the fourth input integer, `rows` is a 2D list of integers where each sublist represents a row of `n` space-separated integers read from the input, `costs` is a list of values returned by `func_1(row, d)` for each `row` in `rows`, `total_costs` is a list containing the sums of every possible `k` consecutive elements from the `costs` list.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of every possible k consecutive elements from the costs list)
#Overall this is what the function does:The function reads a grid configuration defined by the number of rows (`n`), columns (`m`), bridges (`k`), and maximum distance between supports (`d`). It calculates a cost for each row using `func_1` and then determines the minimum total cost of selecting `k` consecutive rows' costs. The final output is this minimum total cost.

