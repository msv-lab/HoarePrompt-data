#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a row, and d is a positive integer representing the maximum distance between supports.
def func_1(row, d):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
        
    #State: Output State: row is a list of integers where the first element is 1 and each subsequent element (from index 1 to d-1) is 2 more than its initial value. For example, if d is 4, then row will be [1, 3, 5, 7].
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        
        row[i] = e[0] + row[i] + 1
        
        heappush(min_heap, e)
        
        heappush(min_heap, (row[i], i))
        
    #State: A modified version of the original `row` list where for each element at index `i` (where `i >= d`), it has been incremented by 1 if the smallest element in the min-heap (considering elements from `row[:d]` and their indices) whose index is less than or equal to `i - (d + 2)` has been popped and then reinserted into the heap twice. The min-heap property is maintained throughout the process.
    return row[-1]
    #The program returns the last element of the modified `row` list, where for each element at index `i` (where `i >= d`), it has been incremented by 1 if the smallest element in the min-heap (considering elements from `row[:d]` and their indices) whose index is less than or equal to `i - (d + 2)` has been popped and then reinserted into the heap twice.
#Overall this is what the function does:The function accepts a list of integers `row` representing the depths of river cells and a positive integer `d` representing the maximum distance between supports. It modifies the `row` list such that for each element at index `i` (where `i >= d`), it increments the element by 1 if the smallest element in a min-heap (consisting of elements from `row[:d]` and their indices) whose index is less than or equal to `i - (d + 2)` has been popped and then reinserted into the heap twice. Finally, it returns the last element of the modified `row` list.

#State of the program right berfore the function call: (n, m, k, d) are integers where 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 × 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells. The first and last elements of each inner list are guaranteed to be 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list of length `n - (k - 1)`, where each element is the sum of every consecutive sub-list of `costs` with length `k`.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of every consecutive sub-list of costs with length k)
#Overall this is what the function does:The function accepts four integers \( n \), \( m \), \( k \), and \( d \), along with a list of \( n \) lists named `rows`. Each inner list in `rows` contains \( m \) positive integers, with the first and last elements being 0. The function calculates the sum of every consecutive sub-list of length \( k \) within the list of costs derived from `rows` using `func_1`, and then finds and prints the minimum value among these sums.

