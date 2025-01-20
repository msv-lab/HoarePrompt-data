#State of the program right berfore the function call: The input string consists of lowercase Latin letters and the special characters «*» and «?», where «*» represents a snowflake and «?» represents a candy cane. These special characters can only appear immediately after a letter. The length of the input string is at most 200. The integer k satisfies 1 ≤ k ≤ 200.
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
        
    #State of the program after the loop has been executed: After the loop has completed all executions: `s` is a non-empty string, `k` is an integer between 1 and 200, `i` is equal to the length of `s` or the loop condition `len(ans) < k` is no longer satisfied. `ans` is a list containing up to `k` alphabetic characters from `s`, with any characters followed by '?' skipped over, and any characters followed by '*' repeated until no more '*' characters follow. If `s` does not contain enough alphabetic characters to fill `ans` to length `k`, `ans` will contain fewer than `k` elements. The variable `i` is the index just past the last character processed in `s`, or it is the length of `s` if the entire string has been processed.
    if (len(ans) == k) :
        print(''.join(ans))
    else :
        print('Impossible')
    #State of the program after the if-else block has been executed: *`s` is a non-empty string, `k` is an integer between 1 and 200, `i` is equal to the length of `s` or the loop condition `len(ans) < k` is no longer satisfied. `ans` is a list containing up to `k` alphabetic characters from `s`, with any characters followed by '?' skipped over, and any characters followed by '*' repeated until no more '*' characters follow. If `len(ans) == k`, `ans` contains exactly `k` alphabetic characters. If `len(ans) < k`, `ans` contains fewer than `k` elements because `s` does not contain enough alphabetic characters to fill `ans` to length `k`. The variable `i` is the index just past the last character processed in `s`, or it is the length of `s` if the entire string has been processed.
#Overall this is what the function does:The function reads an input string `s` and an integer `k`. It processes the string `s` to construct a new string `ans` by including alphabetic characters from `s`. If an alphabetic character is followed by a '*', the character is repeated in `ans` until no more '*' characters follow. If an alphabetic character is followed by a '?', the character is skipped. The process continues until `ans` contains `k` characters or there are no more characters to process in `s`. If `ans` reaches exactly `k` characters, the function prints the constructed string `ans`. If `ans` cannot reach `k` characters due to insufficient alphabetic characters in `s`, the function prints 'Impossible'. The final state of the program is that `s` remains unchanged, `k` is still an integer between 1 and 200, and `ans` is a list containing up to `k` alphabetic characters from `s`, or fewer if `s` does not have enough alphabetic characters. The index `i` is either the length of `s` or the point where the loop condition `len(ans) < k` was no longer satisfied.

