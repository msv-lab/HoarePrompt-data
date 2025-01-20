#State of the program right berfore the function call: The input string consists only of lowercase Latin letters, «*», and «?». The string length does not exceed 200. The integer k is an integer such that 1 <= k <= 200.
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
        
    #State of the program after the loop has been executed: `ans` is `['z', 'p', 'p', 'a', 'l', 'e']`, `s` is `"apple"`, `k` is `3`, and `i` is `5`.
    if (len(ans) == k) :
        print(''.join(ans))
    else :
        print('Impossible')
    #State of the program after the if-else block has been executed: `ans` is `['z', 'p', 'p', 'a', 'l', 'e']`, `s` is `"apple"`, `k` is `3`. If the length of `ans` equals `k`, the program does nothing. Otherwise, the output is "Impossible"."
#Overall this is what the function does:The function `func` accepts a string `s` consisting only of lowercase Latin letters, «*», and «?», with a maximum length of 200, and an integer `k` such that 1 ≤ `k` ≤ 200. It constructs a new list `ans` by iterating through the string `s` and appending characters to `ans` under certain conditions. Specifically, it appends characters that are alphabetic and handles special cases where the character is followed by «*» or «?». After processing, if the length of `ans` equals `k`, it prints the joined string of `ans`. Otherwise, it prints "Impossible". Potential edge cases include strings with no alphabetic characters or invalid input lengths.

