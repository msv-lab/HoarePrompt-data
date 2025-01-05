#State of the program right berfore the function call: n is an integer between 1 and 50 inclusive, and each journey segment consists of an integer ti (1 ≤ ti ≤ 10^6) and a string diri which is one of "North", "South", "West", "East".
def func():
    HEIGHT = 20000
    f = sys.stdin
    height = HEIGHT
    n = int(f.readline())
    sat = True
    for i in range(n):
        dst, directon = f.readline().strip().split(' ')
        
        if directon not in {'South', 'North'}:
            continue
        
        if directon == 'South':
            height -= int(dst)
        elif directon == 'North':
            height += int(dst)
        else:
            raise ValueError('Invalid directon')
        
        if height < 0 or height > HEIGHT:
            sat = False
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 50 inclusive, `HEIGHT` is 20000, `sat` is either True or False depending on whether `height` has stayed within the range of 0 to 20000 throughout all iterations, and `height` is either a value within the range of 0 to 20000 or has gone below 0 or above 20000, causing `sat` to be False.
    sat &= height == HEIGHT
    print('YES' if sat else 'NO')
#Overall this is what the function does:The function accepts an integer `n` (1 to 50 inclusive) representing the number of journey segments, where each segment consists of a distance `dst` and a direction `directon`. It only considers movements in the "South" or "North" directions, adjusting a height variable accordingly. The function checks if the height remains within the range of 0 to 20000 throughout the journey. After processing all segments, it returns 'YES' if the final height is exactly 20000 and 'NO' otherwise. The function ignores any segments with directions other than "South" or "North".

