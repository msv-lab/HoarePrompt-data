#State of the program right berfore the function call: **Precondition**: **n is a positive integer. The input consists of n lines, each containing an integer ti (1 ≤ ti ≤ 10^6) and a string diri representing the length and direction of the i-th part of Limak's journey.**
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
        
    #State of the program after the  for loop has been executed: After the loop executes, `HEIGHT`, `f`, `n`, `sat`, `i`, `dst`, `direction`, `height` are all updated based on the input values. If the loop executes successfully until the end, the `sat` variable remains `True` indicating that the height constraints were not violated throughout the loop execution. If the loop does not execute at all, the initial state of the variables remains unchanged.
    sat &= height == HEIGHT
    print('YES' if sat else 'NO')
#Overall this is what the function does:The function `func` reads input values representing Limak's journey, updates the `height` variable based on the direction and distance traveled, and checks if the final height remains within the constraints. If the final height is within the constraints, it prints 'YES'; otherwise, it prints 'NO'. The function does not accept any parameters, and the output is determined based on the journey input and height constraints.

