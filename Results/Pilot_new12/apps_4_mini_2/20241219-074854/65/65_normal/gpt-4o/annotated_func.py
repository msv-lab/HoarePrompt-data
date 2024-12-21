#State of the program right berfore the function call: n is a positive integer representing the number of baloons (1 ≤ n ≤ 100), k is a positive integer representing the number of friends (1 ≤ k ≤ 100), and s is a string of length n consisting of lowercase letters of the Latin alphabet representing the colors of the baloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `color_count` is a dictionary mapping each unique character in `s` to the number of occurrences of that character, `s` is a string of length `n` consisting of lowercase letters, and `n` is a positive integer (1 ≤ n ≤ 100).
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `color_count` is a dictionary containing the counts of each character in `s`, `can_distribute` is False if any count exceeds `k`, otherwise `can_distribute` is True.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`color_count` is a dictionary containing the counts of each character in `s`. If `can_distribute` is True, it indicates that no count in `color_count` exceeds `k`, and 'YES' has been printed. If `can_distribute` is False, it indicates that at least one count in `color_count` exceeds `k`, and 'NO' has been printed.
#Overall this is what the function does:The function reads two integers, `n` (number of balloons) and `k` (number of friends), followed by a string `s` representing the colors of the balloons. It counts the occurrences of each color in `s` and checks if any color count exceeds `k`. If no color exceeds `k`, it prints 'YES', indicating that the balloons can be evenly distributed among friends. If any color exceeds `k`, it prints 'NO', indicating that it is not possible to distribute them fairly. The function does not return a value; instead, it directly prints the results. Edge cases to consider include cases where all colors are the same, ensuring that `k` is not zero, and ensuring `n` falls within the specified range.

