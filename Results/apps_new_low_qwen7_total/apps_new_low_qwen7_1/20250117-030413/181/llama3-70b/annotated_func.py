#State of the program right berfore the function call: The first line is a string consisting of lowercase Latin letters, «*», and «?». The string length does not exceed 200. The second line is an integer \( k \) such that \( 1 \leq k \leq 200 \).
def func():
    s = input()

k = int(input())

ans = []

i = 0
    while i < len(s) and len(ans) < k:
        if s[i].isalpha():
            ans.append(s[i])
            if i + 1 < len(s) and s[i + 1] == '?':
                i += 2
            elif i + 1 < len(s) and s[i + 1] == '*':
                while i + 1 < len(s) and s[i + 1] == '*':
                    ans.append(s[i])
                    i += 2
                i += 1
            else:
                i += 1
        else:
            i += 1
        
    #State of the program after the loop has been executed: s is a string of lowercase Latin letters, «*», and «?» with a length not exceeding 200, `k` is greater than 0, `ans` is a list containing characters from `s` starting from the first character up to the last «*» encountered, `i` is the next appropriate index based on the conditions described (next even index after the last «*», or the end of the string if no «*» is found, or adjusted as per the special cases involving «?» and 'i' values), and `len(ans)` is exactly equal to `k`.
    if (len(ans) == k) :
        print(''.join(ans))
    else :
        print('Impossible')
    #State of the program after the if-else block has been executed: `s` is a string of lowercase Latin letters, «*», and «?» with a length not exceeding 200, `k` is greater than 0, `ans` is a list containing characters from `s` starting from the first character up to the last «*» encountered, `i` is the next appropriate index based on the conditions described (next even index after the last «*», or the end of the string if no «*» is found, or adjusted as per the special cases involving «?» and 'i' values). If the length of `ans` is exactly equal to `k`, the list `ans` is printed. Otherwise, the length of `ans` is less than `k`.
#Overall this is what the function does:The function processes an input string `s` consisting of lowercase Latin letters, asterisks (`*`), and question marks (`?`). It also takes an integer `k` as input. The function extracts up to `k` characters from `s` starting from the first character and following specific rules:
1. It includes only alphabetical characters in the result.
2. When encountering a `?`, it skips the next character.
3. When encountering a `*`, it repeats the previous character until another `*` is encountered, then skips the next character.
4. The function ensures the resulting list `ans` contains exactly `k` characters.
5. If the resulting list `ans` contains exactly `k` characters, it prints the joined version of `ans`. Otherwise, it prints "Impossible".

