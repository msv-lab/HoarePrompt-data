#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, m is a positive integer such that 1 ≤ m ≤ n, the second input line contains n integers each in the range {1, 2, ..., m} representing the colors of the lightsabers, and the third input line contains m integers k_1, k_2, ..., k_{m} where 1 ≤ ∑_{i=1}^{m} k_{i} ≤ n, representing the desired counts of lightsabers of each color.
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100; `m` is a positive integer such that 1 ≤ `m` ≤ `n`; `colors` is a list of integers that contains `n` elements; `counts` is a list of integers derived from input values; `color_counts` is a dictionary where each key is a unique color from the `colors` list and the value is the count of occurrences of that color in the list.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100, `found` is True or False depending on whether matching counts were found; `i` is at most `n - 1`; `j` is at most `n - 1`; `window_counts` contains the counts of unique colors encountered in the `colors` list from index `i` to `n-1`; if `found` is True, then the counts in `window_counts` match the sorted `counts`, otherwise `window_counts` indicates the counts of colors as they were accumulated in the last iteration before the loop exited.
    print('YES' if found else 'NO')
#Overall this is what the function does:The function accepts two integers, `n` and `m`, representing the number of lightsabers and the number of colors, respectively. It then takes a list of `n` integers indicating the colors of the lightsabers and a list of `m` integers representing the desired counts of each color. The function checks if there exists a contiguous subarray of lightsabers whose color counts match the desired counts and prints 'YES' if such a subarray exists, or 'NO' if it does not. If there are fewer unique colors in the `colors` list than in the `counts` list, it will also return 'NO', as it's not possible to match the counts in that case.

