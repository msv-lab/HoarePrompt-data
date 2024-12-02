#State of the program right berfore the function call: **
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `cubes` is a list of lists of integers, `digits` is a set containing the string representation of each digit in all the inner lists of `cubes` combined
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *`n` is an input integer, `cubes` is a list of lists of integers, `digits` is a set containing the string representation of each digit in all the inner lists of `cubes` combined. If '0' is not in digits, then the program continues without any changes.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:The function `func` reads an integer `n` from the input, then reads `n` lists of integers and creates a set `digits` containing the string representation of each digit in all the lists. If '0' is in `digits`, it is removed. The function then finds the maximum number by sorting the digits in descending order, converting them to an integer, and prints the result. The function does not have any return value.

