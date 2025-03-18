#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a single row, and d is an integer representing the maximum distance between supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: row[0] is 1, and row[i] for i from 1 to d-1 is each increased by 2.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: `row[0]` is 1, `row[i]` for `i` from 1 to `d-1` is `1 + 2*(i-1)`, `row[i]` for `i` from `d` to `len(row) - 1` is `e[0] + row[i] (before the update) + 1` where `e` is the first element in `min_heap` that meets the condition `e[1] > i - (d + 2)`, `min_heap` contains elements where the second value is greater than `i - (d + 2)` including the newly added elements `(row[i], i)` for `i` from `d` to `len(row) - 1`.
    return row[-1]
    #The program returns the final computed value of `row[-1]`, which is determined by the sum of the previous `row[i]` and the first element in `min_heap` that meets the condition `e[1] > i - (d + 2)` for `i` from `d` to `len(row) - 1`.
#Overall this is what the function does:The function modifies the input list `row` by setting `row[0]` to 1 and increasing `row[i]` for `i` from 1 to `d-1` by 2. For indices from `d` to the end of the list, it updates each `row[i]` based on the sum of its current value, the smallest value in a sliding window of size `d+1` (adjusted by the condition `e[1] > i - (d + 2)`), and 1. Finally, it returns the last element of the modified `row` list.

#State of the program right berfore the function call: n is a positive integer representing the number of rows, m is a positive integer representing the number of columns, k is a positive integer representing the number of bridges such that 1 <= k <= n, and d is a positive integer representing the maximum distance between supports such that 1 <= d <= m.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `n` is a positive integer, `m` is a positive integer, `k` is a positive integer such that 1 <= k <= n, `d` is a positive integer such that 1 <= d <= m, `rows` is a 2D list containing `n` rows, each with `m` integers, `costs` is a list of `n` elements where each element is the result of `func_1` applied to the corresponding row in `rows` and the integer `d`, `total_costs` is a list containing `n - k + 1` elements, where each element is the sum of `k` consecutive elements in `costs`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of k consecutive elements in costs, and costs is a list where each element is the result of func_1 applied to a row in rows and the integer d)
#Overall this is what the function does:The function reads input values for the number of rows (`n`), number of columns (`m`), number of bridges (`k`), and maximum distance between supports (`d`). It then calculates costs for each row based on a function `func_1` and computes the total costs for all possible configurations of `k` consecutive rows. Finally, it prints the minimum total cost among these configurations.

