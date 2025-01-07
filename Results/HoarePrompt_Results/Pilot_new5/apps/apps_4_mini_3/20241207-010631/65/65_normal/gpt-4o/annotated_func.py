#State of the program right berfore the function call: n is a positive integer representing the number of baloons, k is a positive integer representing the number of friends such that 1 ≤ n, k ≤ 100, and s is a string of length n consisting of lowercase letters of the Latin alphabet representing the colors of the baloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is a positive integer, `s` is a string of length `n`, `color_count` is a dictionary where keys are distinct characters from `s` and values are their respective counts, indicating how many times each color appears in the string.
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is a positive integer, `s` is a string of length `n`, `color_count` contains the counts of each distinct character in `s`, and `can_distribute` is True if all counts are less than or equal to `k`, otherwise `can_distribute` is False if at least one count exceeds `k`.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `k` is a positive integer, and `s` is a string of length `n`. If `can_distribute` is True, then all counts in `color_count` are less than or equal to `k`. If `can_distribute` is False, then at least one count in `color_count` exceeds `k`.
#Overall this is what the function does:The function accepts two positive integers `n` (number of balloons) and `k` (number of friends), and a string `s` representing the colors of the balloons. It counts the occurrences of each color and checks if any color count exceeds `k`. If all color counts are less than or equal to `k`, it prints 'YES', indicating the balloons can be distributed among friends without exceeding their limit. If any color count exceeds `k`, it prints 'NO', indicating that the distribution is not possible. The function does not return any values, it only prints the result.

