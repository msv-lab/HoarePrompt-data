#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a single row, and d is a positive integer representing the maximum distance between supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: Each element from `row[0]` to `row[d-2]` is incremented by 1, while elements from `row[d-1]` onwards remain unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: Elements from `row[0]` to `row[d-2]` are incremented by 1, and elements from `row[d-1]` to `row[len(row)-1]` are updated to `min(row[max(0, i - (d+1)):i]) + row[i] + 1`.
    return row[-1]
    #The program returns the last element of the list `row` which is calculated as `min(row[max(0, i - (d+1)):i]) + row[i] + 1` for `i` ranging from `d-1` to `len(row)-1`.
#Overall this is what the function does:The function modifies a list of integers representing river depths by incrementing the first `d-1` elements by 1 and then updating each subsequent element from index `d-1` to the end using a specific formula. It returns the last modified element of the list.

#State of the program right berfore the function call: n is a positive integer representing the number of rows, m is a positive integer representing the number of columns, k is a positive integer representing the number of bridges, and d is a positive integer representing the maximum distance between supports. rows is a 2D list of integers where each sublist represents a row in the grid, with the first and last elements of each sublist being 0. costs is a list of integers where each element represents the cost of installing supports for the corresponding row in rows. total_costs is a list of integers where each element represents the total cost of installing supports for k consecutive rows starting from a particular row.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `n`, `m`, `k`, and `d` are integers read from the input; `rows` is a 2D list of integers where each sublist represents a row in the grid, with the first and last elements of each sublist being 0; `costs` is a list of integers where each element represents the result of `func_1(row, d)` for the corresponding row in `rows`; `total_costs` is a list containing the sums of every possible subarray of length `k` from `costs`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is the list of sums of every possible subarray of length k from costs)
#Overall this is what the function does:The function reads input values for the number of rows (`n`), number of columns (`m`), number of bridges (`k`), and maximum distance between supports (`d`). It processes a grid represented by a 2D list (`rows`) where each row starts and ends with 0. It calculates the cost of installing supports for each row using a helper function `func_1` with the constraint `d`. Then, it computes the total cost for every possible set of `k` consecutive rows and outputs the minimum of these total costs.

