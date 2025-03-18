#State of the program right berfore the function call: row is a list of non-negative integers with row[0] and row[-1] being 0, and d is a positive integer such that 1 <= d <= len(row) - 1.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: row is a list of non-negative integers with row[0] = 1, row[i] = row[i] + 2 for 1 <= i < d, and row[-1] = 0.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: row is a list of non-negative integers where row[0] = 1, row[i] = row[i] + 2 for 1 <= i < d, and row[i] for i >= d is updated based on the smallest element in the window of the first d elements of row that are still relevant. min_heap is a valid min-heap containing tuples of the form (row[j], j) for the relevant indices.
    return row[-1]
    #The program returns the last element of the list `row`, which is a non-negative integer updated based on the smallest element in the window of the first `d` elements of `row` that are still relevant.
#Overall this is what the function does:The function `func_1` accepts a list `row` of non-negative integers with the first and last elements being 0, and a positive integer `d` such that 1 <= d <= len(row) - 1. It modifies the list `row` by setting `row[0]` to 1, incrementing each element in the range 1 to d-1 by 2, and then updating each element from index `d` to the end of the list based on the smallest element in a sliding window of the first `d` elements. Finally, it returns the last element of `row`, which is a non-negative integer updated based on the smallest element in the relevant window of the first `d` elements.

#State of the program right berfore the function call: The function does not take any parameters, but it reads input values for n, m, k, and d where n is the number of rows, m is the number of columns, k is the number of bridges, and d is the maximum distance between supports. n, m, k, and d are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 * 10^5, and 1 ≤ d ≤ m. The function also reads n rows of m integers each, forming a 2D list rows where each element rows[i][j] represents the depth a_{i,j} of the river cell, with the constraints 0 ≤ a_{i,j} ≤ 10^6 and a_{i,1} = a_{i,m} = 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `total_costs` is a list of integers where each element is the sum of `k` consecutive elements from the `costs` list, starting from the first element up to the element that allows `k` consecutive elements to be summed. The length of `total_costs` is `len(costs) - (k - 1)`. The values of `n`, `m`, `k`, `d`, `rows`, and `costs` remain unchanged.
    print(min(total_costs))
    #This is printed: - The `print(min(total_costs))` statement will print the smallest sum of `k` consecutive elements in the `costs` list.
    #
    #Output:
#Overall this is what the function does:The function `func_2` reads input values for `n`, `m`, `k`, and `d`, where `n` is the number of rows, `m` is the number of columns, `k` is the number of bridges, and `d` is the maximum distance between supports. It then reads `n` rows of `m` integers each, forming a 2D list `rows` where each element `rows[i][j]` represents the depth of the river cell. The function computes the cost for each row using the function `func_1` and stores these costs in a list `costs`. It calculates the sum of `k` consecutive costs for all possible segments in `costs` and stores these sums in a list `total_costs`. Finally, it prints the minimum value from `total_costs`. The function does not return any value.

