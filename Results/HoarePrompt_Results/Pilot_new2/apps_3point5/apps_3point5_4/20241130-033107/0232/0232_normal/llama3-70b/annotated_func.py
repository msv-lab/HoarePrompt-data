#State of the program right berfore the function call: **Precondition**: **n and m are positive integers such that 1 <= m <= n. The list of colors of the lightsabers contains n integers in the range {1, 2, ..., m}. The list of desired counts of lightsabers for each color contains m integers such that the sum of all desired counts is between 1 and n inclusive.**
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: n, m are positive integers such that 1 <= m <= n; colors is a list of n integers representing the colors of the lightsabers, counts is a list of integers obtained by mapping the input values to integers, color_counts is a dictionary with each unique color as a key and the number of occurrences of that color as the value. The dictionary will contain all unique colors from the colors list with their respective counts.
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
        
    #State of the program after the  for loop has been executed: At the end of the loop execution, `found` is True. The loop will break at some index `i` and `j` will be equal to `n`. `window_counts` will contain each color from `colors[i]` to `colors[n-1]` with their respective counts sorted in the same order as the corresponding targets in `counts`. `color_counts` will remain the same as the original dictionary.
    print('YES' if found else 'NO')
#Overall this is what the function does:The function reads input values for the number of lightsabers and their colors, processes the data to check if there exists a subsequence of colors that matches the desired counts, and prints 'YES' if such a subsequence is found, 'NO' otherwise. The function handles cases where the desired counts are not achievable or where the provided input does not meet the constraints.

