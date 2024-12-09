#State of the program right berfore the function call: n is an integer representing the number of balloons (1 ≤ n ≤ 100), k is an integer representing the number of friends (1 ≤ k ≤ 100), and s is a string of length n consisting of lowercase letters of the Latin alphabet representing the colors of the balloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ 100), `s` is a string of length `n`, `color_count` is a dictionary where the keys are the unique characters in `s` and the values are the counts of each character in `s`.
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ 100), `s` is a string of length `n`, `color_count` contains the counts of each unique character in `s`, and `can_distribute` is True if all counts in `color_count` are less than or equal to `k`, otherwise `can_distribute` is False.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer (1 ≤ n ≤ 100), `k` is an integer (1 ≤ k ≤ 100), `s` is a string of length `n`, and `color_count` contains the counts of each unique character in `s`. If `can_distribute` is True, the output is 'YES'. If `can_distribute` is False, 'NO' has been printed.
#Overall this is what the function does:The function accepts two integers, `n` (1 ≤ n ≤ 100) representing the number of balloons and `k` (1 ≤ k ≤ 100) representing the number of friends, along with a string `s` of length `n` consisting of lowercase letters that represent the colors of the balloons. It counts the occurrences of each color and determines if it is possible to distribute the balloons such that no friend receives more balloons of the same color than `k`. If this distribution is possible, it prints 'YES'; otherwise, it prints 'NO'. This function does not return any value, it only outputs results based on the distribution logic.

