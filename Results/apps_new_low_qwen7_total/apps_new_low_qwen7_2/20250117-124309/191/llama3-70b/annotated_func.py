#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 1000, representing the number of rows and columns in the star map, respectively. The function takes no parameters but the star map is represented as a 2D list where each element is either a '.' (empty space) or '*' (star).
def func():
    n, m = map(int, input().split())

stars = []
    for _ in range(n):
        row = input()
        
        for j, c in enumerate(row):
            if c == '*':
                stars.append((j, _))
        
    #State of the program after the  for loop has been executed: `n` is `0`, `m` remains unchanged, `stars` is a list of tuples where each tuple contains the index of a '*' character in any of the input rows and its corresponding row number, `c` is undefined, and `j` is `-1`.
    min_x = min(x for x, y in stars)

max_x = max(x for x, y in stars)

min_y = min(y for x, y in stars)

max_y = max(y for x, y in stars)

side = max(max_x - min_x + 1, max_y - min_y + 1)

print(side)
#Overall this is what the function does:The function processes a star map represented as a series of input lines, where each line consists of characters that are either '.' (empty space) or '*' (star). The map dimensions are given by the number of rows (n) and columns (m), with both values being in the range [1, 1000]. After processing, the function calculates and prints the side length of the smallest square that can contain all the stars present in the map. If there are no stars, the function still follows the same process but will print the side length of a square that would be able to contain the stars, which would be 1 in this case.

