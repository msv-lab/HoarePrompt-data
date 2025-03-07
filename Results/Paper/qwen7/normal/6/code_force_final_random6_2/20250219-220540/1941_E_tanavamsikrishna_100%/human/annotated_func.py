#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a row, and d is a positive integer representing the maximum allowed distance between supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: Output State: `row` is a list of integers starting with 1, followed by elements each incremented by 2 up to the value of `d` minus one; `d` is a positive integer greater than or equal to 3; `i` is `d-1`.
    #
    #This means that after the loop has executed all its iterations, the `row` list will start with 1, and each subsequent element will be 2 more than the previous one, up to the length of the list determined by `d`. The value of `d` must be at least 3 for the loop to run at least three times, and `i` will be set to `d-1` after the loop completes.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: The loop will continue to execute until `i` reaches the length of `row`. At this point, `i` will be equal to `len(row)`, and `min_heap` will contain tuples where each tuple consists of an updated value of `row[i]` and the corresponding index `i`. Each element in `row` from index `d` to the end will be updated to `e[0] + row[i] + 1`, where `e[0]` is the smallest value popped from `min_heap` during the execution of the loop. The `min_heap` will reflect these updates, ensuring that the smallest value in `min_heap` is always the smallest updated value in `row` from the current `i` to the end of the list.
    return row[-1]
    #The program returns the last element of the list 'row', which has been updated such that each element from index `d` to the end is incremented by the smallest value found in `min_heap` plus one.
#Overall this is what the function does:The function accepts a list of integers `row` representing the depths of river cells and a positive integer `d` representing the maximum allowed distance between supports. It updates each element in `row` from index `d` to the end by adding the smallest value found in a min-heap plus one. Finally, it returns the last element of the updated `row` list.

#State of the program right berfore the function call: (n, m, k, d) are integers where 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2⋅10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells, and the first and last elements of each inner list are 0. The sum of n⋅m for all sets of input data does not exceed 2⋅10^5. costs is a list of integers calculated by calling func_1(row, d) for each row in rows. total_costs is a list of integers calculated by summing k consecutive elements from costs.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list containing the sum of every consecutive `k` elements of `costs` starting from the first element up to the second-to-last element of `costs`; `rows` is unchanged, `n`, `m`, and `k` retain their original values; `d` retains its original value; `costs` is unchanged; `i` is now equal to `len(costs) - (k - 1)`.
    #
    #This means that after the loop has executed all its iterations, `total_costs` will contain sums of all possible consecutive segments of length `k` within the `costs` list. The loop iterates from the start of `costs` to the point where a segment of length `k` can still fit within the list, hence the condition `range(len(costs) - (k - 1))`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs contains the sums of all possible consecutive segments of length k within the costs list)
#Overall this is what the function does:The function accepts four integers \( n \), \( m \), \( k \), and \( d \), along with a list of \( n \) lists called `rows`. It calculates the sum of every consecutive \( k \) elements from a list `costs`, which is derived from `rows` using `func_1(row, d)` for each row. Finally, it prints the minimum value from the list `total_costs`, which contains these sums. The function does not return any value.

