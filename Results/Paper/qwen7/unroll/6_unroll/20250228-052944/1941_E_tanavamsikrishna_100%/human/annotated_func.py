#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a single row, and d is a positive integer representing the maximum allowed distance between supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: Output State: row is a list of integers where the first element is 1, and each subsequent element up to d (exclusive) is 2 more than its initial value.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: Output State: `row` is a list of integers where the first element is 3, and each subsequent element is the sum of the initial value plus 1 for each iteration it was updated, and `min_heap` is a list of tuples containing elements from `row[d:]` paired with their indices, maintaining the min-heap property.
    return row[-1]
    #The program returns the last element of the list 'row', which is the sum of the initial value (3) plus 1 for each iteration it was updated.
#Overall this is what the function does:The function accepts a list of integers `row` representing the depths of river cells in a single row and a positive integer `d` representing the maximum allowed distance between supports. It updates the values in `row` based on a minimum heap operation, ensuring that each element is adjusted according to certain conditions. Finally, it returns the last element of the updated `row`, which is the sum of an initial value (3) plus 1 for each iteration it was updated.

#State of the program right berfore the function call: (n, m, k, d) are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2⋅10^5, 1 ≤ d ≤ m; rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells, and costs is a list of n integers where each element is calculated by the function func_1(row, d) for the corresponding row in rows.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list of sums, where each sum is calculated by taking consecutive sublists of length `k` from the `costs` list and then summing the elements within those sublists. The length of `total_costs` is `len(costs) - (k - 1)`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of consecutive sublists of length k from the costs list)
#Overall this is what the function does:The function accepts four integers \( n \), \( m \), \( k \), and \( d \), along with a list of \( n \) lists (`rows`) and a list of \( n \) integers (`costs`). It calculates the sum of every consecutive sublist of length \( k \) from the `costs` list and stores these sums in a new list (`total_costs`). Finally, it prints the minimum value from `total_costs`.

