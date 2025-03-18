#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a single row, and d is a positive integer representing the maximum allowed distance between adjacent supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: Output State: `row` is a list of integers where the first element is 1, and each subsequent element from index 1 to `d-1` is set to 3. The rest of the elements in the list remain unchanged.
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: Output State: `row` is a list of integers where the first element is 2, and each subsequent element from index 1 to `len(row)-1` is set to 4; `min_heap` is an empty list.
    #
    #Explanation: The loop iterates over the elements of `row` starting from index `d`. For each iteration, it pops the smallest element from `min_heap` whose index is less than or equal to `i - (d + 2)`, then updates the current element in `row` by adding the popped element's value plus one, and pushes both the updated value and the original value back into `min_heap`. This process continues until `min_heap` is empty, resulting in an empty `min_heap` and each element in `row` being incremented by 2 (initially 1 + 1 for the first element and 3 + 1 for the rest).
    return row[-1]
    #The program returns 6
#Overall this is what the function does:The function accepts a list of integers `row` representing the depths of river cells in a single row and a positive integer `d` representing the maximum allowed distance between adjacent supports. It modifies the `row` list by setting the first element to 2 and each subsequent element up to the length of `row` to 4. Additionally, it uses a min-heap to track the minimum values within a sliding window of size `d+2`. After processing, the function returns the last element of the modified `row` list, which is 6.

#State of the program right berfore the function call: (n, m, k, d) are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 × 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells for each row. The first and last elements of each inner list are guaranteed to be 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list containing the sum of every consecutive sublists of `costs` with a length of `k`. Each element in `total_costs` represents the sum of `k` consecutive elements from `costs`.
    print(min(total_costs))
    #This is printed: the minimum value among all the sums of k consecutive elements in costs
#Overall this is what the function does:The function accepts four integers \( n \), \( m \), \( k \), and \( d \), along with a list of \( n \) lists named `rows`. Each inner list contains \( m \) positive integers representing the depths of river cells. The function calculates the sum of every consecutive sublist of length \( k \) within the list `costs`, which is derived from `rows` using `func_1` with parameter \( d \). Finally, it returns the minimum value among all these sums.

