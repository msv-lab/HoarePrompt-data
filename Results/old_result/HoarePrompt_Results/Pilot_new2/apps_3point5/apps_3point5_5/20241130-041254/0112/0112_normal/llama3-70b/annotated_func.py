#State of the program right berfore the function call: **Precondition**: **n is an integer such that 1 <= n <= 3. Each cube has 6 faces with a digit from 0 to 9.**
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 1 <= n <= 3, `cubes` is a list containing `n` sublists, `digits` is a set containing the string representation of each digit in each cube
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *`n` is an input integer such that 1 <= n <= 3, `cubes` is a list containing `n` sublists, `digits` is a set containing the string representation of each digit in each cube except '0'. If '0' is present in digits, it means that there is at least one cube with digit '0' in it.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:The function func reads an integer n followed by n cubes, each represented by a list of digits. It then creates a set of unique digits from all cubes, removes '0' if present, and finds the maximum number that can be formed using the digits from the cubes. The function prints this maximum number. The code does not handle cases where n is outside the range 1 to 3 or where the faces of the cubes contain digits other than 0 to 9.

