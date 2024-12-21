#State of the program right berfore the function call: n is a positive integer representing the number of balloons, k is a positive integer representing the number of friends, and s is a string of lowercase letters where each letter represents the color of a balloon, such that 1 <= n, k <= 100.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer, `s` is the original input string, `c` is the last character in `s` if `s` is not empty, and `color_count` is a dictionary where each key is a unique character from `s` and each value is the count of that character in `s`. If `s` is empty, `color_count` is empty.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an input integer, `k` is an input integer, `s` is the original input string, `c` is the last character in `s` if `s` is not empty, `color_count` is a dictionary where each key is a unique character from `s` and each value is the count of that character in `s`, and `max_color_count` is the maximum value in `color_count`. If `max_color_count` is less than or equal to `k`, 'YES' has been printed to the console. Otherwise, 'NO' has been printed to the console because `max_color_count` is greater than `k`.
#Overall this is what the function does:The function accepts parameters n and k as positive integers and a string s of lowercase letters representing balloon colors, and returns a message to the console indicating whether the maximum number of balloons of the same color (max_color_count) can be distributed among k friends, printing 'YES' if max_color_count is less than or equal to k, and 'NO' otherwise, effectively determining the feasibility of distributing the balloons of the same color among the given number of friends.

