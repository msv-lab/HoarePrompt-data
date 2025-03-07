#State of the program right berfore the function call: row is a list of non-negative integers representing the depths in a row of the river grid, and d is a positive integer representing the maximum distance between supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: row is a list of non-negative integers where the first d-1 elements are each incremented by 1, and d is a positive integer representing the maximum distance between supports.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: the first d-1 elements are incremented by 1, and each subsequent element is the sum of its original value, the minimum value in the preceding d elements, and 1.
    return row[-1]
    #The program returns the last element of the list `row`. This element is the sum of its original value, the minimum value in the preceding `d` elements, and 1.
#Overall this is what the function does:The function takes a list of non-negative integers `row` and a positive integer `d`. It modifies the list by incrementing the first `d-1` elements by 1 and then each subsequent element by 1 plus the minimum value of the preceding `d` elements. Finally, it returns the last element of the modified list.

#State of the program right berfore the function call: n is a positive integer representing the number of rows, m is a positive integer representing the number of columns, k is a positive integer representing the number of bridges, d is a positive integer representing the maximum distance between supports, rows is a 2D list of integers where each sublist represents a row in the grid and contains m integers, and costs is a list of integers representing the cost of installing supports for each row.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: n is the first input integer, m is the second input integer, k is the third input integer, d is the fourth input integer, rows is a 2D list of integers where each sublist (row) contains m integers read from the input, costs is a list of integers where each integer is the result of func_1(row, d) for the corresponding row in rows, total_costs is a list of integers where each integer is the sum of k consecutive elements from the costs list.
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of k consecutive elements from the costs list, and costs is a list of integers derived from the rows and the value of d)
#Overall this is what the function does:The function reads input values including the number of rows (`n`), number of columns (`m`), number of bridges (`k`), maximum distance between supports (`d`), a 2D list of integers (`rows`), and calculates the cost of installing supports for each row using `func_1`. It then computes the sum of costs for every possible set of `k` consecutive rows and prints the minimum of these sums.

