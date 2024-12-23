#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 100, and s is a string consisting of lowercase letters representing the colors of the balloons.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer, `s` is an input string, `color_count` is a dictionary where each key is a unique character from `s` and its corresponding value is the count of that character in `s`.
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `can_distribute` is `False`
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`can_distribute` remains `False`. If `can_distribute` is `True`, the state does not change. Otherwise, `can_distribute` remains `False`.
#Overall this is what the function does:The function `func` accepts two parameters `n` and `k`, which are positive integers such that \(1 \leq n, k \leq 100\), and a parameter `s`, which is a string consisting of lowercase letters representing the colors of the balloons. It checks whether it is possible to distribute the balloons such that no more than `k` balloons of the same color are together.

Specifically, the function performs the following steps:
1. Reads the values of `n`, `k`, and `s` from standard input.
2. Counts the occurrences of each color in the string `s` and stores them in a dictionary `color_count`.
3. Checks if the count of any color exceeds `k`. If it does, sets `can_distribute` to `False`.
4. Prints 'YES' if no color count exceeds `k`, otherwise prints 'NO'.

Potential edge cases and missing functionality:
- The function does not handle the case where the input string `s` is empty or contains no characters. In such cases, the behavior is undefined based on the current implementation.
- The function does not validate that `n` and `k` are within the specified range (1 to 100). If `n` or `k` are out of this range, the behavior is also undefined.
- The function does not return anything; it only prints 'YES' or 'NO' to the console.

