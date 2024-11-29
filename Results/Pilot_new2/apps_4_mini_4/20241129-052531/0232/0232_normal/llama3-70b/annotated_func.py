#State of the program right berfore the function call: n is an integer between 1 and 100, m is an integer between 1 and n, the second line contains n integers each in the range {1, 2, ..., m} representing the colors of the lightsabers, and the third line contains m integers representing the desired counts k_1, k_2, ..., k_m, where 1 <= sum(k_i) <= n.
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `m` is an integer between 1 and `n`, `colors` is a list of integers containing at least `n` integers, `counts` is a list of integers obtained from user input, and `color_counts` is a dictionary where each key is a unique color from the `colors` list, and the value is the count of how many times that color appears in the `colors` list.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `found` is True if there exists a window in `colors` that matches the counts in the `counts` list, otherwise `found` is False. `window_counts` contains counts of colors from the `colors` list corresponding to the last evaluated window when `found` is True or remains empty if `found` is False. `i` is the index of the first window where a match was found, or equals `n` if no match was found.
    print('YES' if found else 'NO')
#Overall this is what the function does:The function accepts two integers `n` (1 to 100) and `m` (1 to `n`), a list of `n` integers representing the colors of lightsabers, and a list of `m` integers representing desired counts. It checks if there exists a contiguous subarray of the `colors` list where the frequency of each unique color matches the corresponding desired counts. If such a subarray exists, it prints 'YES'; otherwise, it prints 'NO'.

