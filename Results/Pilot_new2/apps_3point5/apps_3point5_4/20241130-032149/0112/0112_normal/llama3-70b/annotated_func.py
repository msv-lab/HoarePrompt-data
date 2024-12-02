#State of the program right berfore the function call: n is an integer such that 1 <= n <= 3. Each of the n lines contains 6 integers representing the numbers on the faces of the cubes, where each number is between 0 and 9 (inclusive).**
def func():
    n = int(input())
    cubes = [list(map(int, input().split())) for _ in range(n)]
    digits = set()
    for cube in cubes:
        digits.update(str(digit) for digit in cube)
        
    #State of the program after the  for loop has been executed: Output State: n is an input integer such that 1 <= n <= 3, cubes is a list of lists where each inner list contains integers entered by the user for the respective cube and must have at least n cubes, digits is a set containing the string representation of each digit in all the cubes combined using the `update` method. The `digits` set contains the string representation of each digit in all the cubes.
    if ('0' in digits) :
        digits.remove('0')
    #State of the program after the if block has been executed: *n is an input integer such that 1 <= n <= 3, cubes is a list of lists where each inner list contains integers entered by the user for the respective cube and must have at least n cubes. The `digits` set contains the string representation of each digit in all the cubes excluding '0'. After the if condition, there is at least one cube in which the digit 0 is not present.
    max_num = int(''.join(sorted(digits, reverse=True)))
    print(max_num)
#Overall this is what the function does:The function reads an integer n followed by n lines of 6 integers representing the numbers on the faces of the cubes. It then extracts all unique digits present in the cubes, removes '0' if it exists, calculates the maximum possible number by sorting the digits in descending order and joining them, and finally prints this maximum number.

