#State of the program right berfore the function call: row is a list of non-negative integers representing the depths of the river cells in a single row, and d is a positive integer representing the maximum distance between supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: row is a list where the first d-1 elements are each incremented by 1, and the rest of the elements remain unchanged. d is unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: The first `d-1` elements are each incremented by 2, and each subsequent element is incremented by the minimum value of the previous `d` elements plus 2.
    return row[-1]
    #The program returns the last element of the list `row`, which has been incremented according to the specified rules.
#Overall this is what the function does:The function accepts a list `row` of non-negative integers and a positive integer `d`. It modifies the list `row` by incrementing the first `d-1` elements by 1, and each subsequent element by the minimum value of the previous `d` elements plus 1. The function returns the last element of the modified list `row`.

#State of the program right berfore the function call: n is a positive integer representing the number of rows, m is a positive integer representing the number of columns, k is a positive integer representing the number of bridges, and d is a positive integer representing the maximum distance between supports. rows is a 2D list of integers where each sublist represents a row in the grid and contains m integers, with the first and last integers in each sublist being 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: - The variables `n`, `m`, `k`, `d`, and `rows` remain unchanged.
    #   - `costs` remains unchanged.
    #   - `total_costs` will contain the sums of `k` consecutive elements from `costs`.
    #
    #Given this understanding, the output state after the loop executes is:
    #
    #Output State:
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of k consecutive elements from the costs list)
#Overall this is what the function does:The function reads input parameters `n`, `m`, `k`, and `d`, and a 2D list `rows`. It calculates the minimum cost of placing `k` consecutive bridges in each row of the grid, where the cost is determined by the values in `rows` and the maximum distance `d` between supports. The function outputs the minimum total cost among all rows.

