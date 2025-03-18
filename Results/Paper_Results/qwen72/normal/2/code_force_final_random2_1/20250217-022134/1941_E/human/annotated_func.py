#State of the program right berfore the function call: row is a list of non-negative integers where the first and last elements are 0, representing the depths of the river cells in a row; d is a positive integer representing the maximum distance between supports, such that 1 <= d <= len(row).
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: `row` is a list of non-negative integers where the first `d-1` elements are incremented by 1, and the last element remains 0; `d` is a positive integer representing the maximum distance between supports, such that 1 <= d <= len(row); `i` is `d-2`.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: `row` is a list of non-negative integers where the first `d-1` elements are incremented by 1, and the last element is the sum of the minimum values of the sublists of length `d+1` starting from each position in the list, plus the original value of the last element plus the number of iterations (len(row) - d + 1). The variable `i` is `len(row) - 1`.
    return row[-1]
    #The program returns the sum of the minimum values of the sublists of length `d+1` starting from each position in the list, plus the original value of the last element of `row`, plus the number of iterations (`len(row) - d + 1`).
#Overall this is what the function does:The function `func_1` takes a list `row` of non-negative integers (where the first and last elements are 0) and a positive integer `d` (where 1 <= d <= len(row)). It modifies the first `d-1` elements of `row` by incrementing each by 1. For the remaining elements, it sets each element to the minimum value of the sublist of length `d+1` ending at that element, plus the original value of that element, plus 1. Finally, it returns the last element of the modified `row`, which represents the sum of the minimum values of the sublists of length `d+1` starting from each position in `row`, plus the original value of the last element of `row`, plus the number of iterations (`len(row) - d + 1`).

#State of the program right berfore the function call: n, m, k, and d are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 · 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m integers representing the depths of the river cells, with the constraints 0 ≤ a_{i, j} ≤ 10^6 and a_{i, 1} = a_{i, m} = 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: After the loop executes all iterations, `i` is `len(costs) - k`, `costs` remains a list of length `n`, and `total_costs` is a list containing the sums of every consecutive `k` elements in `costs`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where min(total_costs) is the minimum sum of any consecutive k elements in the costs list)
#Overall this is what the function does:The function reads four integers `n`, `m`, `k`, and `d` from input, followed by `n` lines of `m` integers each, representing the depths of river cells. It processes these inputs to calculate the minimum cost of a sequence of `k` consecutive rows, where the cost of each row is determined by a helper function `func_1`. The function then prints the minimum cost of any such sequence of `k` rows. The final state of the program includes the variables `n`, `m`, `k`, `d`, `rows`, `costs`, and `total_costs`, with `total_costs` containing the sums of every consecutive `k` elements in `costs`.

