#State of the program right berfore the function call: Input contains two integers n and k, such that 1 ≤ n, k ≤ 100, where n represents the number of balloons and k represents the number of friends, and a string s of length n containing lowercase letters of the Latin alphabet, denoting the colors of the balloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100 (inclusive), `k` is an integer between 1 and 100 (inclusive), `s` is a string (possibly empty), `c` is the last character in `s` if `s` is not empty, and `color_count` is a dictionary where each key is a unique character from `s` and its corresponding value is the frequency of that character in `s`. If `s` is empty, then `color_count` is an empty dictionary.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100 (inclusive), `k` is an integer between 1 and 100 (inclusive), `s` is a string (possibly empty), if `s` is not empty, `c` is the last character in `s`, `color_count` is a dictionary where each key is a unique character from `s` and its corresponding value is the frequency of that character in `s`, and `max_color_count` is the maximum frequency of characters in `s` or 0 if `s` is empty. If `max_color_count` is less than or equal to `k`, 'YES' has been printed. Otherwise, 'NO' has been printed, indicating that the maximum frequency of characters in `s` is greater than `k`.
#Overall this is what the function does:The function determines if it's possible to distribute balloons of different colors among a group of friends such that no friend gets more than a certain number of balloons of the same color. It accepts input in the form of the number of balloons (n), the number of friends (k), and a string of balloon colors (s), then prints 'YES' if the maximum frequency of any balloon color does not exceed the number of friends (k), indicating a possible distribution. Otherwise, it prints 'NO'. The function handles edge cases, including empty strings, single-character strings, and cases where the number of balloons or friends is at the boundary of the specified range (1 to 100). It does not consider scenarios where the distribution strategy or the exact number of balloons each friend can get is required; its sole output is a feasibility indication.

