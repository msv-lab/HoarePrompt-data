#State of the program right berfore the function call: n is an integer representing the number of baloons (1 ≤ n ≤ 100), k is an integer representing the number of friends (1 ≤ k ≤ 100), and s is a string of lowercase letters of length n representing the colors of the baloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for c in s:
        if c in color_count:
            color_count[c] += 1
        else:
            color_count[c] = 1
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers based on input, `s` is a non-empty string of lowercase letters, `color_count` is a dictionary where the keys are the unique characters from `s` and the values are the counts of how many times each character appears in `s`.
    max_color_count = max(color_count.values())
    if (max_color_count <= k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` and `k` are integers; `s` is a non-empty string of lowercase letters; `color_count` is a dictionary where the keys are unique characters from `s` and the values are their counts; if `max_color_count` is less than or equal to `k`, 'YES' has been printed. Otherwise, if `max_color_count` is greater than `k`, 'NO' has been printed.
#Overall this is what the function does:The function accepts two integers, `n` (the number of balloons) and `k` (the number of friends), and a string `s` representing the colors of the balloons. It counts the occurrences of each color in `s` and checks if the maximum count of any color is less than or equal to `k`. If it is, the function prints 'YES', indicating that the balloons can be distributed among friends without any friend receiving more than one of the same color. If the maximum count exceeds `k`, it prints 'NO', indicating that at least one friend would receive more than one balloon of the same color.

