#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a single row, and d is an integer representing the maximum distance between supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: `row` is a list where the first element is `1` and each subsequent element up to index `d-1` is incremented by `2`; `d` remains unchanged.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: row is a list where the first `d` elements are as initially defined, and each subsequent element is updated based on the loop logic.
    return row[-1]
    #The program returns the last element of the list `row`
#Overall this is what the function does:The function modifies a list of integers `row` by setting the first element to 1 and incrementing each of the next `d-1` elements by 2. It then updates each subsequent element in `row` based on a specific logic involving a min-heap, ensuring that each element is influenced by the minimum value within a sliding window of size `d`. Finally, the function returns the last element of the modified list `row`.

#State of the program right berfore the function call: n and m are positive integers representing the number of rows and columns in the grid respectively, k is a positive integer representing the number of consecutive rows for which bridges are to be built, and d is a positive integer representing the maximum distance between supports. rows is a 2D list of integers where each sublist represents a row in the grid and contains m integers, with the first and last integers in each sublist being 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `total_costs` is a list containing the sums of every possible `k`-sized contiguous sublist within `costs`. All other variables remain unchanged.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of every possible k-sized contiguous sublist within the costs list)
#Overall this is what the function does:The function `func_2` calculates and prints the minimum total cost required to build bridges over a series of `k` consecutive rows in a grid. The grid is defined by `n` rows and `m` columns, with each row represented as a list of integers. The integers in each row represent the cost of building bridges at each position, except for the first and last integers which are always 0. The parameter `d` specifies the maximum distance between supports. The function evaluates all possible sets of `k` consecutive rows and computes the total cost for each set, then outputs the minimum of these total costs.

