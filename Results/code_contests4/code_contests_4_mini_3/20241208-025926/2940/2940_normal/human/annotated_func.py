#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and for each i from 1 to n, ti is an integer such that 1 ≤ ti ≤ 10^6, and diri is a string that is one of: "North", "South", "West", "East".
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 50, `height` is the final calculated height after all height adjustments based on the input directions, and `sat` is either True (if height is within [0, 20000]) or False (if height is less than 0 or greater than 20000).
    sat &= height == HEIGHT
    print('YES' if sat else 'NO')
#Overall this is what the function does:The function reads an integer `n` from standard input, which specifies the number of height adjustments. It then processes `n` pairs of inputs consisting of a distance and a direction ("North" or "South"). The function adjusts a variable `height` accordingly, increasing it for "North" and decreasing it for "South". If the direction is neither "North" nor "South", it ignores that input. After processing all inputs, it checks if the final height is exactly 20000 and prints 'YES' if it is, or 'NO' if it is not. If at any point during the adjustments the height goes below 0 or above 20000, it immediately sets a flag to indicate failure and breaks the loop. The function does not return any value but prints the result.

