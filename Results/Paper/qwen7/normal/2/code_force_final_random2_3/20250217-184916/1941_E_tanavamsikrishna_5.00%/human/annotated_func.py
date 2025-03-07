#State of the program right berfore the function call: row is a list of non-negative integers representing the depths of river cells in a single row, and d is a positive integer representing the maximum allowed distance between adjacent supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: Output State: The list `row` is a list of non-negative integers where each element from index 0 up to index `d-2` has been incremented by 1, `d` is a positive integer representing the maximum allowed distance between adjacent supports, and `i` is equal to `d-1`.
    #
    #In simpler terms, after the loop has executed all its iterations, every element in the `row` list from the start up to the second last element will have been incremented by 1, depending on the value of `d`. The variable `d` remains unchanged, and `i` will be set to `d-1` after the last iteration.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: After the loop executes all its iterations, the value of `i` will be `len(row)`, `d` will remain as the initial positive integer representing the maximum allowed distance between adjacent supports, and each element in the `row` list from index 0 up to index `d-2` will have been incremented by 1. The elements from index `d-1` to the end of the list will retain their original values unless they were updated during the loop's execution.
    return row[-1]
    #The program returns the last element of the list 'row', which is either incremented by 1 for indices from 0 to d-2 during the loop, or retains its original value otherwise.
#Overall this is what the function does:The function accepts a list of non-negative integers `row` and a positive integer `d`. It increments the first `d-1` elements of the list by 1 and leaves the rest unchanged. The function returns the last element of the modified list `row`.

#State of the program right berfore the function call: (n, m, k, d) are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2⋅10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells. The first and last elements of each inner list are guaranteed to be 0. The sum of n⋅m for all sets of input data does not exceed 2⋅10^5.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list containing the sum of every `k` consecutive elements from `costs`, `rows` remains unchanged, `costs` remains unchanged, `i` is `len(costs) - (k - 1)`, and `len(costs) - (k - 1)` must be equal to the length of `costs`.
    #
    #In simpler terms, after the loop has executed all its iterations, `total_costs` will contain the sum of every `k` consecutive elements from the original `costs` list. The `rows` list and the `costs` list remain unchanged. The variable `i` will be equal to the last index where the sum could be calculated, which is `len(costs) - (k - 1)`. This means that the loop has processed as many sums as possible based on the value of `k` and the length of the `costs` list.
    print(min(total_costs))
    #This is printed: the minimum value among all the sums of k consecutive elements from the costs list
#Overall this is what the function does:The function accepts four integers \( n \), \( m \), \( k \), and \( d \), along with a list of \( n \) lists named `rows`. Each inner list in `rows` contains \( m \) positive integers with the first and last elements being 0. The function calculates the sum of every \( k \) consecutive elements from a list derived from `rows` using `func_1`, then finds and prints the minimum value among these sums. The original `rows` list remains unchanged.

