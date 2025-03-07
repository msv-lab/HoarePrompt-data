#State of the program right berfore the function call: row is a list of non-negative integers representing the depths of river cells in a row, and d is a positive integer representing the maximum allowed distance between adjacent supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: Output State: The value of `i` is `d-1`; each element `row[i]` from index 0 to `d-2` has been incremented by its respective index value (i.e., `row[0]` is incremented by 0, `row[1]` by 1, ..., `row[d-2]` by `d-2`).
    #
    #This means that after the loop has executed all its iterations, the variable `i` will have the value `d-1`, and each element in the `row` list from index 0 up to `d-2` will have been incremented by its own index value.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: The value of `i` is `len(row)`, each element `row[i]` from index 0 to `len(row)-1` has been updated to the minimum value of the slice `row[max(0, i - (d + 1)):i]` plus 1, if `i` is greater than 0; otherwise, it is set to 0 plus the original value of `row[i]` plus 1.
    return row[-1]
    #The program returns the last element of the list 'row', which has been updated according to the specified rules.
#Overall this is what the function does:The function `func_1` accepts a list of non-negative integers `row` and a positive integer `d`. It updates each element in `row` based on specific rules: first, it increments elements from index 0 to `d-2` by their respective indices. Then, it updates elements from index `d-1` to the end by setting them to the minimum value of a sliding window of size `d+1` plus one. Finally, it returns the last element of the updated `row` list.

#State of the program right berfore the function call: (n, m, k, d) are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 × 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells. The first and last elements of each inner list are guaranteed to be 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `total_costs` now contains the sum of costs from index `i` to `i + k - 1` for every possible `i` such that `0 <= i <= len(costs) - k`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs[i] is the sum of costs from index i to i + k - 1 for every possible i such that 0 <= i <= len(costs) - k)
#Overall this is what the function does:The function accepts four parameters: n, m, k, and d, all of which are integers with specific constraints. It also accepts a list named rows, which contains n lists. Each inner list has m positive integers, and the first and last elements of each inner list are guaranteed to be 0. The function calculates the minimum sum of costs over every possible subsequence of length k in the costs list, which itself is derived from the input rows list using another function func_1. Finally, it prints this minimum sum.

