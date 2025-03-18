#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a row, and d is a positive integer representing the maximum distance between supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: Output State: `row` is a list of integers with its first element being 1, and each subsequent element being the original second element plus 2 times its index (starting from 0), `i` is equal to `d`, `d` must be greater than 2, and the length of `row` is `d`.
    #
    #This means that after the loop has executed all its iterations, the `row` list will have `d` elements. The first element remains 1, and each subsequent element starting from the second one will be calculated as the original value of the second element plus 2 times its index position. For example, if `d` was 5, the `row` list would look like this: `[1, 3, 5, 7, 9]` assuming the original second element was 1.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: After all iterations, the loop terminates when `i` is greater than or equal to `len(row)`. The `min_heap` contains pairs of updated values from `row` and their respective indices. Each element in `row` has been updated according to the rule: `row[i] = e[0] + row[i] + 1`, where `e[0]` is the value popped from `min_heap`. The `row` list is now fully updated based on the operations performed within the loop.
    return row[-1]
    #The program returns the last element of the updated `row` list, which is the result of applying the update rule `row[i] = e[0] + row[i] + 1` for each element in `row`, where `e[0]` is the value popped from the `min_heap`.
#Overall this is what the function does:The function accepts a list of integers `row` representing the depths of river cells and a positive integer `d` representing the maximum distance between supports. It updates each element in `row` by incrementing it with the value popped from a minimum heap and then adding 1. Finally, it returns the last element of the updated `row` list.

#State of the program right berfore the function call: (n, m, k, d) are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2⋅10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells. The first and last elements of each inner list are guaranteed to be 0. The sum of n⋅m for all sets of input data does not exceed 2⋅10^5.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list containing the sum of every `k` consecutive elements from `costs`, `rows` remains unchanged, `costs` remains unchanged, `i` is `len(costs) - (k - 1) - 1`, and `len(costs)` must be greater than or equal to `k - 1`.
    #
    #In simpler terms, after the loop has executed all its iterations, `total_costs` will contain the sum of every `k` consecutive elements from the `costs` list. The `rows` and `costs` lists will remain unchanged. The variable `i` will be set to `len(costs) - k`, indicating the last iteration of the loop. Additionally, the length of the `costs` list must be at least `k - 1` for the loop to execute properly.
    print(min(total_costs))
    #This is printed: min(sum of every k consecutive elements from costs)
#Overall this is what the function does:The function accepts four integers \( n \), \( m \), \( k \), and \( d \), along with a list of \( n \) lists named `rows`. Each inner list in `rows` contains \( m \) positive integers representing the depths of river cells, with the first and last elements being 0. The function calculates the sum of every \( k \) consecutive elements from a derived list `costs`, which is computed using `func_1` for each row in `rows`. Finally, it prints the minimum value among these sums.

