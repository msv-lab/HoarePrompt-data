#State of the program right berfore the function call: n is an integer representing the number of baloons (1 ≤ n ≤ 100), k is an integer representing the number of friends (1 ≤ k ≤ 100), and s is a string of lowercase letters representing the colors of the baloons with a length of n.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of balloons, `k` is an integer representing the number of friends, `s` is a string of length at most `n` where each character represents the color of a balloon, `color_count` is a dictionary with unique colors from string `s` as keys and their corresponding counts as values. If `s` is an empty string, then `color_count` remains an empty dictionary.
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer, `k` is an integer, `s` is a string of length at most `n`, `color_count` can contain zero or more entries, `can_distribute` is False if any value in `color_count` is greater than `k`, otherwise `can_distribute` remains True.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` and `k` are integers, `s` is a string of length at most `n`, and `color_count` can contain zero or more entries. If `can_distribute` is True, the output is 'YES'. Otherwise, if `can_distribute` is False, the output is 'NO'.
#Overall this is what the function does:The function accepts two integers `n` (1 ≤ n ≤ 100) and `k` (1 ≤ k ≤ 100), and a string `s` of lowercase letters representing the colors of `n` balloons. It counts the occurrences of each color in `s` and checks whether it is possible to evenly distribute the balloons among `k` friends, given that no friend should receive more balloons of the same color than available. The function prints 'YES' if distribution is possible and 'NO' otherwise. It assumes that no input validation is performed on the values of `n` and `k`.

