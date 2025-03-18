#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 100, and s is a string consisting of lowercase letters of the Latin alphabet representing the colors of the balloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string, `color_count` is a dictionary where each key is a character from the string `s` and its value is the count of that character in the string `s`.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`s` is a non-empty string, `color_count` is a dictionary where each key is a character from the string `s` and its value is the count of that character in the string `s`; `max_color_count` is the maximum value among the counts of characters in `s`. If `max_color_count <= k`, the console displays 'YES'. Otherwise, the condition `max_color_count > k` holds true.
#Overall this is what the function does:The function `func` accepts two positive integers `n` and `k`, both within the range 1 to 100, and a string `s` consisting of lowercase letters representing the colors of the balloons. It then creates a dictionary `color_count` to store the count of each character in the string `s`. After counting the characters, it determines the maximum count of any character in `s` and checks if this maximum count is less than or equal to `k`. If the maximum count is less than or equal to `k`, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return anything but modifies the state by printing the result to the console. Potential edge cases include when `s` is an empty string or when `n` and `k` are outside the specified range, although these cases are not explicitly handled in the code.

