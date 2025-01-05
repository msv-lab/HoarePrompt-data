#State of the program right berfore the function call: **
def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` and `y` are swapped based on their previous values until `y` becomes 0
    return x
    #The program returns the final value of 'x' after swapping with 'y' until 'y' becomes 0
#Overall this is what the function does:The function `func_1` accepts two parameters `x` and `y`, both being integers. It repeatedly swaps the values of `x` and `y` until `y` becomes 0. Finally, it returns the final value of `x` after the swapping process. This function effectively calculates the greatest common divisor of the two input integers `x` and `y`.

#State of the program right berfore the function call: **
def func_2():
    n = int(input())
    a = sorted(zip(map(int, input().split()), range(1, 2 * n + 1)))
    dist = 0
    prev = 1
    for i in range(n):
        pos = a[2 * i][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `a` is a sorted list of tuples containing integers from the input and corresponding numbers from 1 to 2 * n, `dist` is the sum of absolute differences between consecutive positions in the list `a`, `prev` is equal to the last position in the list `a`, `pos` is the last position in the list `a`, `i` is equal to `n-1`
    prev = 1
    for i in range(n):
        pos = a[2 * i + 1][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `a` is a sorted list of tuples containing integers from the input and corresponding numbers from 1 to 2 * n, `dist` is the sum of absolute differences between consecutive positions in the list `a`, `prev` is the value of `pos`, `pos` is the value of the second element in the tuple at index 2 * n - 1 in list `a`, `i` is equal to `n-1`
    print(dist)
#Overall this is what the function does:The function `func_2` reads an integer `n` from the user input, then reads `2n` integers and their corresponding indices to form a list of tuples. It calculates the total distance by summing the absolute differences between consecutive positions in the list. Finally, it prints the total distance as output. The function does not accept any parameters and performs the described operations based on the user input.

