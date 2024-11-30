#State of the program right berfore the function call: n and m are integers such that 1 <= n <= 100 and 1 <= m <= n. The input colors of lightsabers are represented by n integers in the range {1, 2, ..., m}. The desired counts of lightsabers of each color are represented by m integers k_1, k_2, ..., k_{m} such that 1 <= sum of k_i <= n.**
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: n and m are integers such that 1 <= n <= 100 and 1 <= m <= n, colors is a list of integers obtained from the input with at least n colors, color is the last color in the list, counts is a list of integers obtained by splitting the input, color_counts is a dictionary with the key as each distinct color in colors and the value is the count of that color in the list.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than or equal to `m`, `m` is an integer, `colors` is a list of integers with at least `n` colors, `color` is the last color in the list, `counts` is a list of integers, `color_counts` is a dictionary with keys as distinct colors in `colors` and values as the count of each color in the list, `found` is a boolean indicating whether the condition was met, `window_counts` is a dictionary with keys as colors in the range `colors[i:n]` and values as the count of each color in that range, `i` is an integer indicating the current iteration, `j` is an integer less than `n`
    print('YES' if found else 'NO')
#Overall this is what the function does:The function reads input data regarding the colors and desired counts of lightsabers for each color. It then iterates through the colors to find a window of colors that match the desired counts. If such a window is found, it prints 'YES'; otherwise, it prints 'NO'. The function does not accept any parameters.

