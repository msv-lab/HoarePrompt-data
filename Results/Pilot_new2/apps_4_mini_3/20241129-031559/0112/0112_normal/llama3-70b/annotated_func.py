#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 3, and each of the next n lines contains 6 integers a_{i}_{j} where 0 ≤ a_{i}_{j} ≤ 9 representing the digits on the faces of each cube.
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 3; `cubes` is a list containing `n` lists of integers; `cube` is the last list in `cubes`; `digits` includes string representations of all unique integers from all lists in `cubes`.
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 3; `cubes` is a list containing `n` lists of integers; `cube` is the last list in `cubes`; and `digits` includes string representations of all unique integers from all lists in `cubes`. If '0' is present in `digits`, then `digits` includes all unique integers excluding '0'.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:The function reads an integer `n` (where 1 ≤ n ≤ 3) and then reads `n` lines of 6 integers each, representing the digits on the faces of cubes. It collects all unique digits from these inputs, removes '0' if present, and constructs the largest possible integer by sorting the remaining digits in descending order. The resulting integer is then printed.

