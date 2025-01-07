#State of the program right berfore the function call: n is a positive integer representing the number of balloons, k is a positive integer representing the number of friends, and s is a string of length n consisting of lowercase letters of the Latin alphabet representing the colors of the balloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is a positive integer, `s` is a string of length `n`, and `color_count` is a dictionary where each key is a unique character from `s`, and the corresponding value is the count of occurrences of that character in `s`.
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is a positive integer, `s` is a string of length `n`, `color_count` is a dictionary with character counts, and `can_distribute` is False if any character count in `color_count` exceeds `k`, otherwise it is True.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `k` is a positive integer, `s` is a string of length `n`, and `color_count` is a dictionary with character counts. If `can_distribute` is True, it indicates that no character count in `color_count` exceeds `k`, allowing for distribution. If `can_distribute` is False, the output is 'NO' due to at least one character count exceeding `k`.
#Overall this is what the function does:The function determines if a given number of balloons in various colors can be distributed among a specific number of friends, such that no friend receives more than one balloon of the same color. It accepts two positive integers `n` (the number of balloons) and `k` (the number of friends), as well as a string `s` (representing the colors of the balloons). If any color appears more frequently than `k`, it prints 'NO', indicating that fair distribution is not possible. If all colors have a count less than or equal to `k`, it prints 'YES', meaning the balloons can be distributed without exceeding the limit for any friend. Note that the function does not explicitly handle invalid inputs or cases where `n` or `k` are less than or equal to zero, which could lead to erroneous behavior.

