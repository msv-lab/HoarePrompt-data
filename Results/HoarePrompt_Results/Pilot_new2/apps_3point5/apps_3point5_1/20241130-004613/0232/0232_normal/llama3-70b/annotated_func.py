#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ m ≤ n. The list of colors of the lightsabers contains n integers in the range {1, 2, ..., m}. The list of desired counts of lightsabers of each color contains m integers such that $1 \leq \sum_{i = 1}^{m} k_{i} \leq n$.**
def func():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        
        color_counts[color] += 1
        
    #State of the program after the  for loop has been executed: n and m are positive integers such that 1 ≤ m ≤ n, colors is a list of integers obtained by splitting the input and must have at least n colors, color is the last color in the list, counts is the list of integers obtained by splitting the input. If color is not in color_counts, color_counts[color] is assigned the value equal to the number of occurrences of color in the colors list.
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
        
    #State of the program after the  for loop has been executed: After the loop executes, `n` is greater than or equal to 1, `m` is a positive integer such that 1 ≤ m ≤ n, `colors` is a list of integers with at least n colors, `color` is the last color in the list, `counts` is the list of integers, `color_counts` contains the updated values with the number of occurrences of each color, `found` is True if all counts in `window_counts` match the targets in `counts`, `window_counts` contains the count of each color until index `n`. If `found` is True, then we break out of the loop or if statement we were directly inside.
    print('YES' if found else 'NO')
#Overall this is what the function does:The function `func` reads input for the number of colors of lightsabers, the list of colors, and the desired counts of lightsabers for each color. It then checks if there exists a contiguous subsequence of the colors list such that the counts of each color match the desired counts. If such a subsequence exists, it prints 'YES'; otherwise, it prints 'NO'. The function ensures valid input parameters based on the constraints provided.

