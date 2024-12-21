#State of the program right berfore the function call: n is a positive integer representing the number of baloons, k is a positive integer representing the number of friends, and s is a string of length n consisting of lowercase letters representing the colors of the baloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string of length `n`, `k` is a positive integer, `color_count` is a dictionary containing the frequency of each character in `s`, where the keys are the unique characters from `s` and the values are the counts of those characters.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`s` is a non-empty string of length `n`, `k` is a positive integer, and `color_count` is a dictionary containing the frequency of each character in `s`. If the maximum frequency value `max_color_count` from `color_count` is less than or equal to `k`, 'YES' has been printed. Otherwise, if `max_color_count` is greater than `k`, the output is 'NO'.
#Overall this is what the function does:The function determines if the maximum frequency of any color of balloons, represented by the string `s`, is less than or equal to the number of friends `k`. It accepts two integers (n and k) and a string (s) representing the colors of the balloons. After processing, if the maximum count of any color is less than or equal to k, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value, and it assumes valid input where n is the length of s, which should be non-empty and composed of lowercase letters. Edge cases, such as an empty input for `s` or characters not being lowercase letters, are not explicitly handled in the code.

