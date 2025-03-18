#State of the program right berfore the function call: row is a list of non-negative integers representing the depths of river cells in a row, and d is a positive integer representing the maximum allowed distance between adjacent supports.
def func_1(row, d):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
        
    #State: Output State: The list `row` is a list of non-negative integers where each element has been increased by 1, except for the element at index `d-1`, which has been increased by 2; the variable `d` remains greater than 1; the final value of `i` is `d - 1`; every element in `row` from index 0 to `d-2` (inclusive) has been incremented once more due to the loop executing `d-1` times.
    #
    #In simpler terms, after the loop has executed all its iterations, each element in the list `row` will have been incremented by 1, except for the element at index `d-1`, which will have been incremented by 2. All elements from index 0 to `d-2` will have been incremented twice because the loop runs `d-1` times.
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
        
    #State: Output State: After the loop executes all its iterations, each element in the list `row` will have been incremented by 1, except for the element at index `d-1`, which will have been incremented by 2. All elements from index 0 to `d-2` will have been incremented twice because the loop runs `d-1` times. The variable `i` will have the value `len(row) - 1`, and the variable `d` will remain greater than 1.
    #
    #In simpler terms, every element in the list `row` will have been incremented by 1, except for the last element, which will have been incremented by 2. Elements from the start of the list up to the second-to-last element will have been incremented twice.
    return row[-1]
    #The program returns the last element of the list `row`, which has been incremented by 2 compared to its original value. All other elements in the list have been incremented by 1, with the first `d-2` elements incremented twice.
#Overall this is what the function does:The function accepts a list `row` of non-negative integers and a positive integer `d`. It increments the last element of `row` by 2, increments all other elements by 1, and increments the first `d-2` elements by 1 again. The function returns the modified list.

#State of the program right berfore the function call: (n, m, k, d) are integers such that 1 ≤ k ≤ n ≤ 100, 3 ≤ m ≤ 2 × 10^5, and 1 ≤ d ≤ m. rows is a list of n lists, where each inner list contains m positive integers representing the depths of the river cells, and the first and last elements of each inner list are guaranteed to be 0.
def func_2():
    n, m, k, d = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
        
    #State: Output State: `total_costs` is a list containing the sum of every `k` consecutive elements from the `costs` list, including the sum of the last `k` elements if they are available. `rows` remains a list of `n` lists, and `costs` remains a list of `n` elements. The variable `i` is set to `len(costs) - k`.
    #
    #In simpler terms, after the loop completes all its iterations, `total_costs` will contain sums of all possible consecutive groups of `k` elements from the `costs` list, starting from the beginning and moving towards the end. If the `costs` list has fewer than `k` elements remaining at the end of the loop, those elements will be summed as well. The `rows` and `costs` lists remain unchanged, and `i` is set to the index just after the last group of `k` elements considered.
    print(min(total_costs))
    #This is printed: min(sum of every k consecutive elements from costs list)
#Overall this is what the function does:The function accepts four integers `n`, `m`, `k`, and `d`, along with a list `rows` of `n` lists, each containing `m` positive integers. It calculates the sum of every `k` consecutive elements from a derived list `costs`, which is itself derived from `rows` using `func_1`. The function then prints the minimum sum among these calculated values. The function returns nothing but prints the result.

