#State of the program right berfore the function call: row is a list of non-negative integers representing the depths of the river cells in a single row, and d is a positive integer representing the maximum distance between supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: The first `d - 1` elements of `row` are each incremented by 1, and the remaining elements remain unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: The first `d - 1` elements of `row` are each incremented by 2, and for each element `row[i]` where `i >= d - 1`, `row[i]` is updated to `min(row[max(0, i - (d + 1)):i]) + row[i] + 1`.
    return row[-1]
    #The program returns the last element of the modified `row` list, which is calculated as `min(row[max(0, i - (d + 1)):i]) + row[i] + 1` for `i = len(row) - 1`.
#Overall this is what the function does:The function modifies a list of non-negative integers (`row`) by incrementing the first `d - 1` elements by 1, and then updating each subsequent element based on the minimum value of the previous `d` elements plus the current element value plus 1. Finally, it returns the last element of the modified list.

#State of the program right berfore the function call: n is an integer representing the number of rows in the grid, m is an integer representing the number of columns in the grid, k is an integer representing the number of bridges, and d is an integer representing the maximum distance between supports. rows is a 2D list where each sublist represents a row in the grid and contains m integers representing the depth in each cell.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `total_costs` is a list containing the sums of all contiguous sub-lists of length `k` from the `costs` list.
    print(min(total_costs))
    #This is printed: min(total_costs) (where min(total_costs) is the smallest sum of any contiguous sub-list of length k from the costs list)
#Overall this is what the function does:The function calculates the minimum cost required to build a specified number of bridges (`k`) across a grid, where each bridge spans over a contiguous segment of cells in a row, and the cost is determined by the depths of the cells within the segment. The function prints the minimum cost among all possible segments of length `k` for each row.

