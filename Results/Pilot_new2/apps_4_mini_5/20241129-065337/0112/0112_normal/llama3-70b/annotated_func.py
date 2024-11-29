#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 3, and each of the next n lines contains exactly 6 integers a_{i}_{j} where 0 ≤ a_{i}_{j} ≤ 9.
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 1 ≤ `n` ≤ 3; `cubes` is a list containing exactly `n` lists of integers; `digits` is the set of string representations of all integers in all lists within `cubes`.
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *`n` is an input integer such that 1 ≤ `n` ≤ 3; `cubes` is a list containing exactly `n` lists of integers; if '0' is in `digits`, then `digits` is the set of string representations of all integers in all lists within `cubes` excluding the string '0'.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 3) and reads `n` lines of input, each containing exactly 6 integers (ranging from 0 to 9). It extracts all the digits from these inputs, forming a set of unique digits. If the digit '0' is present, it is removed from this set. The function then constructs the largest possible integer by sorting the remaining digits in descending order and concatenating them. This integer is printed as output, but the function does not return any value.

