#State of the program right berfore the function call: row is a list of non-negative integers representing the depths of the river cells in a row, and d is a positive integer representing the maximum distance between supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: Output State: row is a list where each element (initially at index i) is increased by 1 for every i from 0 to d-2. The first d-1 elements of the row list will each be incremented by 1, while the rest of the elements remain unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: Output State: row is a list where each element (initially at index i) is increased by 1 for every i from 0 to d-2, and then each element from index d-1 to the end of the list is updated to be the minimum value of the previous d elements plus its original value plus 1.
    return row[-1]
    #The program returns the last element of the list 'row', which is updated to be the minimum value of the previous d elements plus its original value plus 1.
#Overall this is what the function does:The function accepts a list of non-negative integers `row` and a positive integer `d`. It updates each element in the list such that the first `d-1` elements are incremented by 1, and each subsequent element is set to the minimum value of the previous `d` elements plus its original value plus 1. Finally, it returns the last element of the updated list `row`.

#State of the program right berfore the function call: (n, m, k, d) are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2⋅10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells, and the first and last elements of each inner list are guaranteed to be 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list of length `n - (k - 1)`, where each element is the sum of `k` consecutive elements from the `costs` list starting from index `i` to `i + k - 1` for each iteration `i` in `range(len(costs) - (k - 1))`. The values of `n`, `m`, `k`, and `d` retain their original values; `rows` retains its original structure and values.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of k consecutive elements from the costs list)
#Overall this is what the function does:The function accepts four integer parameters \( n \), \( m \), \( k \), and \( d \), along with a list of lists named `rows`. It calculates the minimum sum of any \( k \) consecutive elements from a transformed version of the `rows` list, where each element is the result of calling another function `func_1` on the corresponding row of `rows` and the parameter \( d \). The function then prints this minimum sum and returns nothing.

