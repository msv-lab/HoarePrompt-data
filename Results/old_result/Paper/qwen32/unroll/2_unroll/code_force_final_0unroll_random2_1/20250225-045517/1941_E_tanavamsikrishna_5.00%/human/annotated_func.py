#State of the program right berfore the function call: row is a list of integers representing the depths of the river cells in a single row, and d is an integer representing the maximum distance between supports such that 1 <= d <= len(row).
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: row is a list of integers where the first d-1 elements have been incremented by 1, and all other elements remain unchanged. d is unchanged.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: row is a list of integers where the first `d-1` elements have been incremented by 1, and each subsequent element is the sum of its original value, the minimum value of the previous `d` elements, and 1.
    return row[-1]
    #The program returns the last element of the list `row`, which is the sum of its original value, the minimum value of the previous `d` elements, and 1.
#Overall this is what the function does:The function accepts a list of integers `row` representing river cell depths and an integer `d` representing the maximum distance between supports. It modifies the list by incrementing the first `d-1` elements by 1 and then each subsequent element by its original value, the minimum value of the previous `d` elements, and 1. Finally, it returns the last element of the modified list.

#State of the program right berfore the function call: n is a positive integer representing the number of rows, m is a positive integer representing the number of columns, k is a positive integer representing the number of bridges, and d is a positive integer representing the maximum distance between supports. rows is a 2D list of integers where each sublist represents a row in the river grid and contains m integers, with the first and last integers being 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: `n`, `m`, `k`, `d`, `rows`, `costs`, `total_costs` (where `total_costs` is a list of sums of every `k` consecutive elements from the `costs` list).
    print(min(total_costs))
    #This is printed: min(total_costs) (where total_costs is a list of sums of every k consecutive elements from the costs list)
#Overall this is what the function does:The function calculates the minimum total cost of placing `k` bridges in a grid such that the maximum distance between supports does not exceed `d`. It reads input values for the number of rows (`n`), number of columns (`m`), number of bridges (`k`), and maximum distance between supports (`d`). It also reads a 2D list `rows` representing the river grid. The function computes the minimum cost among all possible placements of `k` consecutive bridges in each row and prints this minimum cost.

