#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 50, and for each of the next n lines, ti is a positive integer (1 ≤ ti ≤ 10^6) and diri is a string that is one of: "North", "South", "West", "East".
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
        
    #State of the program after the  for loop has been executed: `n` is within the range of 1 to 50, `HEIGHT` is 20000, `height` is the final calculated height based on the inputs, `sat` is True if height is between 0 and 20000 after all iterations, otherwise `sat` is False.
    sat &= height == HEIGHT
    print('YES' if sat else 'NO')
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 50) and processes `n` lines of input, each containing a positive integer `ti` (1 ≤ ti ≤ 10^6) and a direction string (`"North"` or `"South"`). It adjusts a height variable starting from 20,000 based on the specified directions and distances. If the height goes out of bounds (less than 0 or greater than 20,000) during the iterations, it sets a flag `sat` to False. After processing all inputs, it checks if the final height is equal to 20,000 and prints 'YES' if `sat` is True and the height is 20,000; otherwise, it prints 'NO'. The function does not handle invalid direction inputs ("West" and "East") explicitly and ignores them without any alert or error.

