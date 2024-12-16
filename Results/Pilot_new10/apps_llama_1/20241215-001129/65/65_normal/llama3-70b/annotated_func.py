#State of the program right berfore the function call: n is a positive integer representing the number of balloons, k is a positive integer representing the number of friends, and s is a string of length n containing only lowercase letters of the Latin alphabet, where each letter represents the color of a balloon.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer, `s` is an input string, `c` is the last character in `s` if `s` is not empty, otherwise `c` is undefined, and `color_count` is a dictionary where each key is a unique character from `s` and the value associated with each key is the frequency of that character in `s`.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an input integer, `k` is an input integer, `s` is an input string, `c` is the last character in `s` if `s` is not empty, otherwise `c` is undefined, `color_count` is a dictionary where each key is a unique character from `s` and the value associated with each key is the frequency of that character in `s`, and `max_color_count` is the maximum value in `color_count.values()`. If `max_color_count` is less than or equal to `k`, 'YES' has been printed to the output. Otherwise, 'NO' has been printed to the console.
#Overall this is what the function does:The function accepts the number of balloons `n`, the number of friends `k`, and a string `s` representing balloon colors, and prints 'YES' if the maximum frequency of any color is less than or equal to `k`, or 'NO' otherwise, without input validation or error handling.

