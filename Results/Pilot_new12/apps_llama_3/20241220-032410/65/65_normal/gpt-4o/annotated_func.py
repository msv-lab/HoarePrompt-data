#State of the program right berfore the function call: n is a positive integer representing the number of balloons, k is a positive integer representing the number of friends, and s is a string of lowercase letters representing the colors of the balloons, where 1 <= n, k <= 100.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer, `s` is the input string, `color_count` is a dictionary containing the frequency of each character in `s`, and if `s` is not empty, `color` is the last character in `s`.
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer, `s` is the input string, `color_count` is a dictionary containing the frequency of each character in `s`, `color` is the last character in `s` if `s` is not empty, and `can_distribute` is `True` if all frequencies in `color_count` are less than or equal to `k`, and `False` otherwise.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an input integer, `k` is an input integer, `s` is the input string, `color_count` is a dictionary containing the frequency of each character in `s`, `color` is the last character in `s` if `s` is not empty. If `can_distribute` is `True`, 'YES' has been printed. If `can_distribute` is `False`, 'NO' has been printed to the console.
#Overall this is what the function does:The function determines whether it's possible to distribute balloons of different colors among a given number of friends, such that no friend gets more than one balloon of the same color. It accepts three inputs: the number of balloons, the number of friends, and a string of colors representing each balloon. The function then prints 'YES' if the distribution is possible and 'NO' otherwise. The final state of the program includes the input parameters, a dictionary containing the frequency of each color, and a printed message indicating whether the distribution is possible. The function does not handle cases where the input string or the number of friends/balloons is empty, and it assumes that the input string only contains lowercase letters. The function also does not consider the actual distribution of balloons among friends, but only checks if such a distribution is theoretically possible.

