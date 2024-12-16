#State of the program right berfore the function call: n and k are non-negative integers such that 1 ≤ n, k ≤ 100, and s is a string consisting of lowercase letters of the Latin alphabet representing the colors of the balloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer, `s` is a non-empty string (now empty), and `color_count` is a dictionary where each key is a unique character from `s` and its value is the frequency of that character in `s`.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an input integer, `k` is an input integer, `s` is an empty string, `color_count` is an empty dictionary, `max_color_count` is None. If `max_color_count` is less than or equal to `k`, the program prints 'YES'. Otherwise, the program prints 'NO'.
#Overall this is what the function does:The function `func` accepts three parameters: `n`, `k`, and `s`. It reads `n` and `k` from input, where both are non-negative integers between 1 and 100, and `s` is a string consisting of lowercase letters representing the colors of the balloons. It then counts the frequency of each color in the string `s`. Finally, it checks if the maximum frequency of any color in `s` is less than or equal to `k`. If it is, it prints 'YES'; otherwise, it prints 'NO'.

