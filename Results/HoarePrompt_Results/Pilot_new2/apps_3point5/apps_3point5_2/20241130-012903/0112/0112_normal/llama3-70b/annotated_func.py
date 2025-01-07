#State of the program right berfore the function call: n is a positive integer. Each cube has 6 integers representing the digits on its faces, where each integer is between 0 and 9.**
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `cubes` is a 2D list containing n lists of integers, `digits` is a set containing all the individual digits of all the integers in the `cubes` list
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *`n` is a positive integer, `cubes` is a 2D list of n lists of integers, `digits` is a set containing all the individual digits of all the integers in the `cubes` list except '0'.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:The function `func` takes user input for the number of cubes, creates a 2D list of cubes with random digits on each face, and finds the maximum number that can be formed by combining all unique digits from the cubes except '0'. The function then prints this maximum number.

