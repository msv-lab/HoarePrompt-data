#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a row, and d is a positive integer representing the maximum allowed distance between supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: Output State: The final state of the loop will have `i` equal to `d-1`, `d` must be greater than 1, and each element in the list `row` from index 1 to `d-1` will be incremented by 2 for each corresponding index. In other words, `row[i]` for each `i` in the range from 1 to `d-1` will be `1 + 2*(i)`. All other variables and their initial conditions remain unchanged.
    #
    #This means that if `d` is, for example, 5, then after the loop completes, `row` will be `[1, 3, 5, 7, 9]`.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: Output State: `i` is 0, `d` must be greater than 1, `len(row)` must be greater than `d-1`, and `min_heap` contains tuples where the second element is non-negative, with the first elements being updated values from the `row` list according to the given logic. Specifically, each tuple in `min_heap` has the form `(new_value, index)` where `new_value` is calculated as `e[0] + row[index] + 1` for some `index` starting from `d-1` and incrementing as the loop progresses until `i` reaches 0.
    #
    #This means that after all iterations of the loop, `i` will have decremented from `d-1` to 0, and `min_heap` will contain updated values from the `row` list, reflecting the operations performed within the loop.
    return row[-1]
    #The program returns the last element of the list 'row' after updating the min_heap according to the given logic.
#Overall this is what the function does:The function accepts a list of integers `row` representing the depths of river cells and an integer `d` representing the maximum allowed distance between supports. It updates the list `row` by modifying its elements based on a minimum heap operation. Specifically, it increments certain elements in `row` by 2 for the first `d-1` indices, then uses a minimum heap to update the remaining elements according to a specific logic. Finally, it returns the last element of the updated list `row`.

#State of the program right berfore the function call: n, m, k, and d are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 × 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells for each row. The first and last elements of each inner list are guaranteed to be 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list containing the sum of every consecutive `k` elements from the `costs` list, starting from the first element and ending at the second-to-last element of the `costs` list.
    #
    #This means that if the `costs` list has `n` elements, `total_costs` will contain `n - (k - 1)` sums, each representing the sum of `k` consecutive elements from the `costs` list.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs contains the sums of every consecutive k elements from the costs list)
#Overall this is what the function does:The function accepts four integers \( n \), \( m \), \( k \), and \( d \), along with a list of \( n \) lists called `rows`. Each inner list in `rows` contains \( m \) positive integers representing the depths of river cells, with the first and last elements being 0. The function calculates the sum of every consecutive \( k \) elements from a list of costs derived from `rows`, and then prints the minimum of these sums.

