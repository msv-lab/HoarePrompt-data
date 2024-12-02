#State of the program right berfore the function call: n is an integer in the range 1 to 3, and each subsequent line contains 6 integers (each between 0 and 9) representing the digits on the faces of each of the n cubes.
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: `n` is an integer in the range 1 to 3, `cubes` is a list containing `n` lists of integers, `digits` is the set containing string representations of all integers present in all lists of `cubes`.
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *`n` is an integer in the range 1 to 3, `cubes` is a list containing `n` lists of integers, and `digits` is a set containing string representations of all integers present in all lists of `cubes`. If '0' is in `digits`, this means that `digits` contains the string representation of the integer 0; otherwise, `digits` contains string representations of integers from the lists in `cubes`, excluding '0'.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:The function accepts an integer `n` (1 to 3), reads `n` lines of six integers each representing cube face digits, collects unique digits, removes '0' if present, and prints the largest number that can be formed from the remaining digits. The function does not return any value.

