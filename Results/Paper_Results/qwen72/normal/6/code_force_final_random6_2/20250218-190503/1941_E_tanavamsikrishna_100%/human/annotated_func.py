#State of the program right berfore the function call: row is a list of non-negative integers where row[0] = row[-1] = 0, and d is a positive integer such that 1 <= d < len(row).
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: `row` is a list of non-negative integers where `row[0] = 1`, `row[-1] = 0`, and for each index `i` in the range `1` to `d-1`, `row[i]` is `row[i] + 2 * (d-1)`. `d` remains a positive integer such that `1 <= d < len(row)`, and `i` is `d-1`.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: The loop will have finished executing, and the final state will be as follows:
    return row[-1]
    #The program returns the last element of the list `row`.
#Overall this is what the function does:The function `func_1` accepts a list `row` of non-negative integers where the first and last elements are 0, and a positive integer `d` such that 1 <= d < len(row). It modifies the list `row` by setting the first element to 1 and incrementing each element in the range from 1 to d-1 by 2. It then processes the list using a min-heap to update each element from index `d` to the end of the list. The function returns the last element of the modified list `row`.

#State of the program right berfore the function call: The function does not take any parameters, but it reads input values for n, m, k, and d, where n is the number of rows in the river grid, m is the number of columns, k is the number of bridges to build, and d is the maximum distance between supports. It also reads n rows of m integers each, representing the depths of the river cells. The values are such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 · 10^5, and 1 ≤ d ≤ m, with the first and last columns having a depth of 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: The loop has completed all iterations, `i` is `len(costs) - k`, and `total_costs` is a list containing the sums of every contiguous subsequence of length `k` in `costs`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where min(total_costs) is the minimum sum of any contiguous subsequence of length k in the costs list)
#Overall this is what the function does:The function reads input values for `n`, `m`, `k`, and `d`, and a grid of river depths. It calculates the minimum total depth of the river cells that need to be bridged to build `k` bridges, ensuring the distance between any two supports does not exceed `d`. The function then prints this minimum total depth.

