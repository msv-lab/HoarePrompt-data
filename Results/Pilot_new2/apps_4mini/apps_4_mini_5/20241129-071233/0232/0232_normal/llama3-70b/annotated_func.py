#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, m is an integer such that 1 ≤ m ≤ n, the second input is a list of n integers each in the range {1, 2, ..., m} representing the colors of the lightsabers, and the third input is a list of m integers k_1, k_2, ..., k_{m} such that 1 ≤ ∑_{i=1}^{m} k_{i} ≤ n.
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `m` is an integer such that 1 ≤ `m` ≤ `n`, `colors` is a list of integers containing `n` colors, `color_counts` is a dictionary where each unique color from `colors` is a key and the corresponding value is the count of occurrences of that color in the `colors` list.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `m` is an integer such that 1 ≤ `m` ≤ `n`, `colors` is a list of integers containing `n` colors, `color_counts` is a dictionary mapping each unique color from `colors` to its count of occurrences, `found` is `True` if a valid window was found; otherwise, `found` is `False`, `i` is less than or equal to `n`, `j` is equal to `n`, and `window_counts` contains the counts of the colors from the last evaluated window (from the last value of `i` to `n-1`). If the loop does not execute at all, `found` remains `False`, `i` is still the original value, `j` is equal to `i`, and `window_counts` remains an empty dictionary.
    print('YES' if found else 'NO')
#Overall this is what the function does:The function accepts two integers `n` and `m`, a list of `n` integers representing the colors of lightsabers, and a list of `m` integers representing the target counts of those colors. It checks if there exists a contiguous subarray of the `colors` list such that the counts of each color in that subarray match exactly the counts specified in the `counts` list. If such a subarray is found, it prints 'YES'; otherwise, it prints 'NO'. Edge cases include ensuring that the `counts` list does not exceed the available colors and that the counts match exactly.

