#State of the program right berfore the function call: n is the number of balloons and k is the number of friends, both are integers between 1 and 100 (inclusive), and s is a string representing the colors of the balloons, where each character in the string is a lowercase letter of the Latin alphabet.
def func():
    n, k = map(int, input().split())
    s = input()
    color_count = {}
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer, `s` is a string, `color` is the last character in `s` if `s` is not empty, and `color_count` is a dictionary where each key is a unique character from `s` and each value is the count of that character in `s`. If `s` is empty, `color_count` is an empty dictionary.
    can_distribute = True
    for count in color_count.values():
        if count > k:
            can_distribute = False
            break
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer, `s` is a string, `color` is the last character in `s` if `s` is not empty, `color_count` is a dictionary where each key is a unique character from `s` and each value is the count of that character in `s`, and `can_distribute` is `False` if any character count in `color_count` is greater than `k`, otherwise `can_distribute` is `True`.
    if can_distribute :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an input integer, `k` is an input integer, `s` is a string, `color` is the last character in `s` if `s` is not empty, `color_count` is a dictionary where each key is a unique character from `s` and each value is the count of that character in `s`. If `can_distribute` is `True`, 'YES' has been printed to the console. If `can_distribute` is `False`, there exists at least one character count in `color_count` that is greater than `k`, and 'NO' has been printed to the console.
#Overall this is what the function does:The function determines whether it is possible to distribute balloons of different colors to a certain number of friends, given the constraint that no friend can receive more than one balloon of the same color. The function takes three inputs: the number of balloons (`n`), the number of friends (`k`), and a string representing the colors of the balloons (`s`). It returns 'YES' if it is possible to distribute the balloons among the friends without any friend receiving more than one balloon of the same color, and 'NO' otherwise. The function handles edge cases where the input string `s` is empty, in which case it will print 'YES' because no distribution is needed. Additionally, the function does not validate the inputs, so it assumes that `n` and `k` are integers between 1 and 100 (inclusive), and `s` is a string of lowercase letters. After execution, the program's state is determined by the output ('YES' or 'NO') printed to the console, indicating whether the balloon distribution is possible under the given conditions.

