#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 2000, and the following n lines contain exactly m characters each, with characters being either '.' (representing black pixels) or 'w' (representing white pixels), where at least one character is 'w'.
def func():
    n, m = map(int, input().split())
    pixels = [list(input()) for _ in range(n)]
    white_pixels = [(i, j) for i in range(n) for j in range(m) if pixels[i][j] ==
    'w']
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float(
    '-inf')
    for (x, y) in white_pixels:
        min_x, min_y = min(min_x, x), min(min_y, y)
        
        max_x, max_y = max(max_x, x), max(max_y, y)
        
    #State of the program after the  for loop has been executed: `n` is an integer in the range [1, 2000]; `m` is an integer in the range [1, 2000]; `white_pixels` must contain at least one tuple of (x, y); `min_x` is the minimum x-coordinate of all tuples in `white_pixels`; `min_y` is the minimum y-coordinate of all tuples in `white_pixels`; `max_x` is the maximum x-coordinate of all tuples in `white_pixels`; `max_y` is the maximum y-coordinate of all tuples in `white_pixels`.
    frame_size = max(max_x - min_x, max_y - min_y) + 1
    if (frame_size > max(n, m)) :
        print(-1)
    else :
        for i in range(n):
            for j in range(m):
                if (i == min_x or i == max_x or j == min_y or j == max_y) and pixels[i][j
                    ] == '.':
                    pixels[i][j] = '+'
                elif pixels[i][j] == 'w':
                    continue
                else:
                    pixels[i][j] = '.'
            
        #State of the program after the  for loop has been executed: `n` and `m` are integers in the range [1, 2000]; `white_pixels` remains a list containing at least one tuple of (x, y); `min_x`, `min_y`, `max_x`, and `max_y` remain unchanged; `frame_size` is equal to `max(max_x - min_x, max_y - min_y) + 1` and is less than or equal to the maximum of `n` and `m`; `pixels` may contain '+' at positions meeting the specified conditions, and unchanged 'w' pixels will remain 'w', while other pixels will be set to '.' if they were not specified to be '+' through the loop conditions. The loop will execute 'n' times, and for each row, all 'm' columns will be processed. If no conditions are met to change any pixels, the pixels array will retain any original setup except for 'w' pixels, which remain unchanged.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: To understand the state after all iterations of the loop, let’s analyze the provided information clearly. The loop iterates through `pixels`, which is a 2D list containing `n` rows and `m` columns. Each iteration prints a string that represents the contents of the current `row`. 
        #
        #Given that `n` and `m` are integers within the range [1, 2000], and `white_pixels` is guaranteed to contain at least one tuple, it's ensured that the outer loop iterates based on the number of rows in `pixels`, which is `n` times. The properties regarding `min_x`, `min_y`, `max_x`, `max_y`, and `frame_size` remain unchanged during these iterations.
        #
        #After `n` iterations of this loop, the state can be detailed as follows: 
        #1. The loop will print the contents of the 2D list `pixels`, which contains `n` rows with the width of `m` columns.
        #2. Each row's output corresponds to its original state before entering the loop, possibly influenced by modifications made due to conditions regarding `white_pixels`.
        #
        #Considering the conditions, at the end of the loop, `pixels` still has `n` rows and `m` columns, and the unchanged conditions regarding `min_x`, `min_y`, `max_x`, and `max_y` hold true.
        #
        #Thus, summarizing the above conditions:
        #
        #Output State: **`n` is an integer in the range [1, 2000], `m` is an integer in the range [1, 2000], `white_pixels` is a list containing at least one tuple (x, y), `pixels` is a 2D list with `n` rows and `m` columns, `min_x`, `min_y`, `max_x`, and `max_y` remain unchanged, `frame_size` is equal to `max(max_x - min_x, max_y - min_y) + 1` and is less than or equal to the maximum of `n` and `m`.`
    #State of the program after the if-else block has been executed: *`n` is an integer in the range [1, 2000], `m` is an integer in the range [1, 2000], `white_pixels` contains at least one tuple (x, y), `min_x`, `min_y`, `max_x`, and `max_y` remain unchanged, and `frame_size` is equal to `max(max_x - min_x, max_y - min_y) + 1`. If `frame_size` is greater than `max(n, m)`, -1 has been printed. Otherwise, `pixels` is a 2D list with `n` rows and `m` columns, retaining its original state, and the iteration will print the contents of each row of `pixels` accordingly.
#Overall this is what the function does:The function reads an integer pair (n, m) indicating the dimensions of a grid, followed by n lines of m characters each, representing pixels that can be either black ('.') or white ('w'). It identifies the coordinates of all white pixels ('w') and computes the minimum and maximum coordinates of these pixels. Based on the computed coordinates, it checks whether the size of the bounding frame around the white pixels exceeds the grid dimensions. If it does, the function outputs -1. If not, it modifies the grid, marking the edges of the frame (if they contain black pixels) with a '+' sign while leaving white pixels unchanged and any other black pixels as dots. Finally, it prints the modified grid. 

Edge cases include: 
1. The case where the entire grid is composed only of white pixels (which may require handling to ensure that the edges get modified appropriately).
2. A scenario where white pixels are positioned at the edges of the grid so that nothing is modified.
3. Situations where the size of the frame around white pixels is equal to the grid dimensions, ensuring that the '+' marking conditions operate correctly.
4. The function guarantees that there is at least one white pixel, but does not explicitly handle when all other pixels, apart from the white ones, remain untouched if they are adjacent to the bounding frame. 

The final state includes the original grid modified according to the conditions, or -1 is printed if the bounding frame exceeds the grid's size. The function prints each row of the modified or unmodified grid at the end.

