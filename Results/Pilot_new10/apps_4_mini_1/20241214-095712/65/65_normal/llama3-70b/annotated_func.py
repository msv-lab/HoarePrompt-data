#State of the program right berfore the function call: n is an integer representing the number of baloons (1 ≤ n ≤ 100), k is an integer representing the number of friends (1 ≤ k ≤ 100), and s is a string of lowercase Latin letters of length n representing the colors of the baloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `n` is the input integer representing the number of balloons, `k` is the input integer representing the number of friends, `s` is a string of lowercase Latin letters, and `color_count` is a dictionary where keys are unique characters from `s` and values are their respective counts in `s`.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is the input integer representing the number of balloons, `k` is the input integer representing the number of friends, `s` is a string of lowercase Latin letters, `color_count` is a dictionary where keys are unique characters from `s` and values are their respective counts in `s`, and `max_color_count` is the maximum count of any character in `color_count`. If `max_color_count` is less than or equal to `k`, the output 'YES' has been printed. Otherwise, `max_color_count` is greater than `k`.
#Overall this is what the function does:The function accepts two integer inputs, `n` (the number of balloons) and `k` (the number of friends), followed by a string `s` representing the colors of the balloons. It counts the occurrences of each color and determines the maximum count of any single color. If this maximum count is less than or equal to the number of friends `k`, it prints 'YES'; otherwise, it prints 'NO'. The function does not return a value; it only outputs the result directly.

