#State of the program right berfore the function call: n and m are positive integers such that 1 <= m <= n. The list of colors of Jedi Knights contains n integers in the range {1, 2, ..., m}. The list of desired counts of lightsabers for each color contains m integers such that the sum of all desired counts is between 1 and n (inclusive).**
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: n and m are positive integers such that 1 <= m <= n; colors list contains n integers in the range {1, 2, ..., m} and is not empty; counts list is populated with integers obtained from splitting the input; color_counts dictionary contains the count of each color in colors
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `n` remains unchanged, `m` remains a positive integer such that 1 <= m <= n, `colors` list still contains n integers in the range {1, 2, ..., m} and is not empty, `counts` list is still populated with integers obtained from splitting the input, `color_counts` dictionary still contains the count of each color in colors, `found` remains True if all counts in `window_counts` after sorting match the corresponding targets in `counts`, `window_counts` dictionary includes the count of each color as a key with the corresponding value for the last iteration of the loop.
    print('YES' if found else 'NO')
#Overall this is what the function does:The function reads input values for the number of Jedi Knights, the range of colors, the colors of Jedi Knights, and the desired counts of lightsabers for each color. It then calculates the total number of lightsabers needed based on certain constraints and relationships. Finally, it determines if the total number of lightsabers needed can be achieved and prints 'YES' if possible, or 'NO' otherwise. The function does not accept any parameters explicitly.

