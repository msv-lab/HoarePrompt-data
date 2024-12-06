#State of the program right berfore the function call: n is a positive integer representing the number of baloons, k is a positive integer representing the number of friends, and s is a string of length n consisting of lowercase letters of the Latin alphabet representing the colors of the baloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `color_count` is a dictionary where each key is a unique color from the string `s`, and each value is the count of occurrences of that color in `s`. `n` is a positive integer, `k` is a positive integer, and `s` is a string of length `n`. If `s` is an empty string, then `color_count` remains empty.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`color_count` is a dictionary where each key is a unique color from the string `s`, and each value is the count of occurrences of that color in `s`; `n` is a positive integer; `k` is a positive integer; if `max_color_count` is less than or equal to `k`, then the program continues processing without any output. Otherwise, if `max_color_count` is greater than `k`, the program outputs 'NO'.
#Overall this is what the function does:The function accepts two positive integers `n` (the number of balloons) and `k` (the number of friends), along with a string `s` representing the colors of the balloons. It counts the occurrences of each color in `s`. If the maximum count of any color is less than or equal to `k`, it outputs 'YES'; otherwise, it outputs 'NO'. It does not return any values or perform additional operations such as returning a concatenation of colors.

