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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `k` is an integer between 1 and 100, `s` is a string input from the user, and `color_count` is a dictionary where the key is a character from `s` and the value is the count of that character in `s`.
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
    #State of the program after the if-else block has been executed: *`can_distribute` remains `False`. If the condition `can_distribute` is `True`, it does not change; otherwise, it remains `False`.
#Overall this is what the function does:The function accepts two parameters \( n \) and \( k \), both of which are positive integers such that \( 1 \leq n, k \leq 100 \), and a string \( s \) consisting of lowercase letters. It counts the frequency of each color (character) in the string \( s \). Then, it checks if the frequency of any color exceeds \( k \). If no color frequency exceeds \( k \), it prints 'YES', indicating that it is possible to distribute the balloons according to the given conditions. Otherwise, it prints 'NO', indicating that it is not possible to do so. The function does not return any value but prints the result directly. Potential edge cases include invalid inputs (e.g., non-integer values for \( n \) and \( k \) or characters other than lowercase letters in \( s \)), which are handled by the input processing part of the code. However, the function does not explicitly handle these edge cases in its logic; it assumes valid inputs.

