#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 100, and s is a string consisting of lowercase Latin letters representing the colors of the balloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `n` is an integer, `k` is an integer, `s` is a non-empty string, `color_count` is a dictionary where the keys are unique characters from `s` and the values are the counts of those characters in `s`.
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `can_distribute` is a boolean indicating whether it is possible to distribute the colors such that each color appears at most `k` times, `n` is an integer, `k` is an integer, `s` is a non-empty string, and `color_count` is a dictionary where the keys are unique characters from `s` and the values are the counts of those characters in `s`.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`can_distribute` is a boolean indicating whether it is possible to distribute the colors such that each color appears at most `k` times. If `can_distribute` is true, the condition remains unchanged. If `can_distribute` is false, it remains false. `n`, `k`, `s`, and `color_count` retain their original states as described in the precondition.
#Overall this is what the function does:The function accepts two positive integers `n` and `k` (both within the range of 1 to 100) and a string `s` consisting of lowercase Latin letters representing the colors of the balloons. It counts the occurrences of each color in the string and checks if it is possible to distribute the colors such that no color appears more than `k` times. If such a distribution is possible, it prints 'YES'; otherwise, it prints 'NO'.

