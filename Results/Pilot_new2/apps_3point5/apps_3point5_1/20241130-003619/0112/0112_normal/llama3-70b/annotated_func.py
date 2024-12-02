#State of the program right berfore the function call: n is an integer such that 1 <= n <= 3. Each of the n lines contains 6 integers representing the digits on the faces of the cubes. Each digit on the face of the cube is an integer from 0 to 9.**
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: n is an input integer such that 1 <= n <= 3, cubes must have at least n lists of integers, digits is a set containing the string representation of each digit in all cubes
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *n is an input integer such that 1 <= n <= 3, cubes must have at least n lists of integers. Digits is a set containing the string representation of each digit in all cubes except '0'.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:Functionality: The function `func` reads input from the user, including an integer `n` (1 <= n <= 3) followed by n lines, each containing 6 integers representing the digits on the faces of the cubes. It then creates a set of unique digits excluding '0' from the cubes and finds the maximum number that can be formed by arranging these digits in descending order. Finally, it prints the calculated maximum number.

Potential Edge Case: The code does not handle a scenario where there are less than n lines of integers representing the digits on the faces of the cubes. It assumes there will always be at least n lines of input.

