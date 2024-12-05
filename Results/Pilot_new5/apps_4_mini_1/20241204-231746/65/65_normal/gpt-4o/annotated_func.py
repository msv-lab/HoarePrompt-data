#State of the program right berfore the function call: n is an integer between 1 and 100 inclusive representing the number of balloons, k is an integer between 1 and 100 inclusive representing the number of friends, and s is a string of lowercase letters of the Latin alphabet representing the colors of the balloons with length n.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100 inclusive, `k` is an integer between 1 and 100 inclusive, `s` is a string of lowercase letters with length `n`, and `color_count` is a dictionary where each key is a unique character from the string `s` and its corresponding value is the count of its occurrences in `s`.
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100 inclusive, `k` is between 1 and 100 inclusive, `s` is a string of lowercase letters of length `n`, `color_count` is a dictionary with counts of occurrences of each unique character from `s`, and `can_distribute` is True if all counts in `color_count` are less than or equal to `k`, or False if at least one count is greater than `k`.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is between 1 and 100 inclusive, `k` is between 1 and 100 inclusive, `s` is a string of lowercase letters of length `n`, and `color_count` is a dictionary with counts of occurrences of each unique character from `s`. If `can_distribute` is True, all counts in `color_count` are less than or equal to `k`. Otherwise, if `can_distribute` is False, at least one count in `color_count` is greater than `k.
#Overall this is what the function does:The function accepts two integers `n` (representing the number of balloons) and `k` (representing the number of friends), along with a string `s` (representing the colors of the balloons). It counts the occurrences of each color and checks if it is possible to distribute the balloons to friends such that no friend receives more than `k` balloons of any color. The function prints 'YES' if the distribution is possible and 'NO' if at least one color has more than `k` occurrences.

