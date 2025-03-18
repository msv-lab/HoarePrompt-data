#State of the program right berfore the function call: row is a list of non-negative integers representing the depths of river cells in a row, and d is a positive integer representing the maximum allowed distance between adjacent supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: Output State: row is a list where each element at index i (0 <= i < d-1) is increased by 1 compared to its initial value, while the rest of the elements remain unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: Output State: row is updated such that for each index \(i\) from \(d-1\) to \(len(row)-1\), the value of \(row[i]\) is incremented by 1 plus the minimum value of the previous \(d\) elements (including itself if \(i > 0\)). If \(i = 0\), then it is incremented by 1. All other elements in the list remain unchanged.
    return row[-1]
    #The program returns the last element of the list 'row' after it has been updated according to the specified rule. This means for each index \(i\) from \(d-1\) to \(len(row)-1\), the value of \(row[i]\) is incremented by 1 plus the minimum value of the previous \(d\) elements (including itself if \(i > 0\)). If \(i = 0\), then it is incremented by 1. All other elements in the list remain unchanged.
#Overall this is what the function does:The function accepts a list of non-negative integers `row` and a positive integer `d`. It updates the list `row` by incrementing each element from index \(d-1\) to the last index by 1 plus the minimum value among the previous \(d\) elements (including itself if applicable). The function returns the last element of the updated list `row`.

#State of the program right berfore the function call: (n, m, k, d) are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 × 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells. The first and last elements of each inner list are guaranteed to be 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list containing the sum of every consecutive `k` elements from the `costs` list.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of every consecutive k elements from the costs list)
#Overall this is what the function does:The function accepts four integer parameters \( n \), \( m \), \( k \), and \( d \), along with a list of lists named `rows`. It calculates the sum of every consecutive \( k \) elements from a transformed list `costs`, which is derived from `rows` using `func_1`. Finally, it prints the minimum value from the `total_costs` list.

