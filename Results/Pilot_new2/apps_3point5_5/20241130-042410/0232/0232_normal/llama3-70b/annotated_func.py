#State of the program right berfore the function call: n, m, k_1, k_2, ..., k_{m} are integers such that 1 ≤ n ≤ 100, 1 ≤ m ≤ n, 1 ≤ k_i, 1 ≤ i ≤ m and 1 ≤ ∑_{i=1}^{m} k_i ≤ n.**
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: `n`, `m` are integers obtained from the input split, `colors` is a non-empty list of colors, `counts` is a list containing the mapped integers from the input split. `color_counts` is a dictionary where each color in `colors` is a key, and the value is the count of occurrences of that color in the `colors` list.
    found = False
    for i in range(n):
        window_counts = {}
        
        for j in range(i, n):
            color = colors[j]
            if color not in window_counts:
                window_counts[color] = 0
            window_counts[color] += 1
            if all(count == target for count, target in zip(sorted(window_counts.
                values()), counts)):
                found = True
                break
        
        if found:
            break
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `found` is either True if the condition is met or False if the condition is not met, `window_counts` is a dictionary where each color in `colors` is a key, and the value is the count of occurrences of that color in the `colors` list within the range of `i` to `n`, `i` is the last value in the range of the loop, `color` is the last color in the `colors` list. If `found` is True, then the condition is met, and the program breaks out of the most internal loop or if statement.
    print('YES' if found else 'NO')
#Overall this is what the function does:The function `func` reads input data and calculates whether a specific condition is met based on the input values. It then prints 'YES' if the condition is satisfied, otherwise 'NO'. The function does not accept any parameters and does not return any value.

