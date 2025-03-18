#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 3, and each of the next n lines contains 6 integers a_{i}_{j} where 0 ≤ a_{i}_{j} ≤ 9 representing the digits on the faces of the cubes.
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: `n` is equal to the input integer between 1 and 3, `cubes` is a list of `n` lists containing integers between 0 and 9, `digits` is a set containing string representations of all integers from all cubes.
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 3, `cubes` is a list of `n` lists containing integers from 0 to 9, and `digits` is a set of string representations of all integers from the cubes excluding '0'. If '0' is present in `digits`, it implies that at least one of the lists in `cubes` contains a 0; otherwise, `digits` contains string representations of integers from 1 to 9.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 3) and reads `n` lines, each containing 6 integers between 0 and 9. It collects all unique digits from the cubes, removes '0' if present, and then constructs the largest possible integer from the remaining digits. The function outputs this largest integer. If all digits are 0, the output would be an empty string.

