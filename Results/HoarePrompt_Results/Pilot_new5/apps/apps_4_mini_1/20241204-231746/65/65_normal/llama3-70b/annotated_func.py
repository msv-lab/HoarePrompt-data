#State of the program right berfore the function call: n is a positive integer representing the number of balloons, k is a positive integer representing the number of friends, and s is a string of length n consisting of lowercase letters of the Latin alphabet representing the colors of the balloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is updated as needed, `s` is a string of length `n` consisting of lowercase letters of the Latin alphabet, `color_count` is a dictionary where each key is a unique character from `s` and each value is the count of occurrences of that character in `s`. If `n` is 0, the loop does not execute, and `color_count` remains an empty dictionary.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `k` is updated as needed, `s` is a string of length `n` consisting of lowercase letters of the Latin alphabet, `color_count` is a dictionary where each key is a unique character from `s` and each value is the count of occurrences of that character in `s`. If `max_color_count` is less than or equal to `k`, 'YES' is printed. Otherwise, if `max_color_count` is greater than `k`, 'NO' is printed.
#Overall this is what the function does:The function accepts two positive integers `n` (the number of balloons) and `k` (the number of friends), as well as a string `s` of length `n` representing the colors of the balloons. It counts the occurrences of each color of balloon and determines if the maximum number of balloons of any one color exceeds the number of friends `k`. If the most frequent color has a count less than or equal to `k`, it prints 'YES'; otherwise, it prints 'NO'. The function does not handle cases where the input values are not positive integers or if the string `s` is not of the expected length.

