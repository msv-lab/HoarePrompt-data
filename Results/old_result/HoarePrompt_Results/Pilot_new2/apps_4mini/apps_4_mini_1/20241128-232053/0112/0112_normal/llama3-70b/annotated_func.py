#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 3, and each of the following n lines contains 6 integers a_{i}_{j} (0 ≤ a_{i}_{j} ≤ 9) representing the digits on the faces of the cubes.
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 3; `cubes` is a list of 3 lists of integers; `digits` is a set containing the string representations of all integers from all sublists in `cubes`.
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ n ≤ 3; `cubes` is a list of 3 lists of integers; `digits` is a set containing the string representations of all integers from all sublists in `cubes`. If '0' is in `digits`, then '0' is included in the set of string representations.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 3) and reads `n` lines of 6 integers each (with each integer in the range 0 to 9) representing the digits on the faces of cubes. It collects all unique digits from these integers, removes '0' if present, and constructs the largest possible integer using the remaining digits. The largest integer is then printed. If all digits are '0', the output will be an empty string since no number will be formed.

