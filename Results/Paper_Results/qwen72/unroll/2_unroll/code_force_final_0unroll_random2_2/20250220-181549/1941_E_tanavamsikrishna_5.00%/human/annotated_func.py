#State of the program right berfore the function call: row is a list of integers representing the depths of a single row of the river grid, and d is a positive integer such that 1 <= d <= len(row).
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: The first d-1 elements of the row list are incremented by 1, while the rest of the elements in the row list remain unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: The first `d-1` elements of the `row` list are incremented by 1, and each element from `d-1` to the end of the list is updated to the minimum of the previous `d` elements (including the first `d-1` elements and the updated elements) plus the original value of that element plus 1.
    return row[-1]
    #The program returns the last element of the `row` list, which has been updated to the minimum of the previous `d` elements (including the first `d-1` elements and the updated elements) plus the original value of that element plus 1.
#Overall this is what the function does:The function `func_1` accepts a list of integers `row` and a positive integer `d`. It increments the first `d-1` elements of `row` by 1. For each subsequent element from `d-1` to the end of the list, it updates the element to the minimum of the previous `d` elements (including the first `d-1` elements and the updated elements) plus the original value of that element plus 1. The function returns the last element of the updated `row` list.

#State of the program right berfore the function call: n, m, k, and d are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 · 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, each containing m integers where a_{i,1} = a_{i,m} = 0 and 0 ≤ a_{i,j} ≤ 10^6 for all 1 ≤ i ≤ n and 1 ≤ j ≤ m.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `n`, `m`, `k`, `d`, `rows`, `costs` remain unchanged. `total_costs` is a list of integers, where each integer is the sum of `k` consecutive elements from the `costs` list. The length of `total_costs` is `len(costs) - (k - 1)`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of integers, each being the sum of k consecutive elements from the costs list)
#Overall this is what the function does:The function `func_2` reads four integers `n`, `m`, `k`, and `d` from the input, followed by `n` rows of `m` integers each. It then computes the cost for each row using the function `func_1` and stores these costs in a list `costs`. The function calculates the sum of every `k` consecutive elements in `costs` and stores these sums in a list `total_costs`. Finally, it prints the minimum value from `total_costs`. The function does not return any value.

