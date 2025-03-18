#State of the program right berfore the function call: row is a list of non-negative integers where the first and last elements are 0, representing the depths of the river cells in a row, and d is a positive integer such that 1 <= d <= len(row).
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: `row` is a list of non-negative integers where the first `d-1` elements are each incremented by 1, and the last element remains 0; `d` is a positive integer such that 1 <= d <= len(row); `i` is `d-2`.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: After the loop has executed all iterations, `row` will have its first `d-1` elements each incremented by 1, and the elements from index `d-1` to the end of the list will each be set to the value of their respective index plus 1. The value of `d` and `i` remain unchanged.
    return row[-1]
    #The program returns the value of the last element in the list `row`, which is equal to the index of the last element plus 1.
#Overall this is what the function does:The function `func_1` takes a list `row` of non-negative integers (where the first and last elements are 0) and a positive integer `d` such that 1 <= d <= len(row). It modifies the list `row` by incrementing the first `d-1` elements by 1 and setting each subsequent element (from index `d-1` to the end) to the minimum value of the previous `d+1` elements (or 0 if there are fewer than `d+1` elements) plus the current value plus 1. The function returns the value of the last element in the modified list `row`, which is equal to the index of the last element plus 1.

#State of the program right berfore the function call: n, m, k, and d are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 · 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m integers representing the depths of the river cells, with the constraints 0 ≤ a_{i, j} ≤ 10^6, a_{i, 1} = a_{i, m} = 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: After all iterations of the loop, `total_costs` is a list containing the sums of every contiguous subsequence of `k` elements in `costs`. The length of `total_costs` is `len(costs) - (k - 1)`. The variables `n`, `m`, `k`, and `d` remain unchanged, as do `rows` and `costs`. The loop variable `i` has reached the value `len(costs) - k`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where min(total_costs) is the smallest sum of any contiguous subsequence of k elements in the costs list)
#Overall this is what the function does:The function reads input values for `n`, `m`, `k`, and `d`, and a list of `n` lists (`rows`) containing `m` integers each. It then computes a list of costs using the function `func_1` for each row in `rows`. The function calculates the minimum sum of every contiguous subsequence of `k` elements in the `costs` list and prints this minimum sum. The function does not return any value; it only prints the result. The input variables `n`, `m`, `k`, `d`, and `rows` remain unchanged after the function execution.

