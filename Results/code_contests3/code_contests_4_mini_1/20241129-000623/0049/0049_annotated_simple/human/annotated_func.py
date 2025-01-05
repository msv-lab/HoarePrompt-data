#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 3 ⋅ 10^5, and s is a string of length n consisting only of lowercase Latin letters.
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = raw_input()
    flag = False
    for i in range(n - 1):
        if c[i] > c[i + 1]:
            flag = True
            pos = i
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `s` is a string of length `n`, `c` is an input string, `flag` is True if there exists at least one pair of adjacent characters in `c` where the first character is greater than the second, otherwise `flag` is False. `pos` is the index of the last such pair where `c[pos]` is greater than `c[pos + 1]` if `flag` is True, otherwise `pos` is undefined.
    if flag :
        print('YES')
        print(pos + 1, pos + 2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is at least 2, `s` is a string of length `n`, and `c` is an input string. If `flag` is True, indicating that there is at least one pair of adjacent characters in `c` where the first character is greater than the second, then 'YES' is printed, along with the values `pos + 1` and `pos + 2`, where `pos` is the index of the last such pair. If `flag` is False, indicating there are no such pairs, 'NO' is printed and `pos` is undefined.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 300,000) and a string `c` of length `n` consisting only of lowercase Latin letters. It checks for adjacent character pairs in the string where the first character is greater than the second. If such a pair is found, it prints 'YES' along with the 1-based indices of the pair; otherwise, it prints 'NO'. It should be noted that if there are no adjacent pairs that meet this condition, the output will be 'NO' without any additional information.

