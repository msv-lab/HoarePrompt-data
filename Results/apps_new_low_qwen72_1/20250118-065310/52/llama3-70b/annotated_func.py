#State of the program right berfore the function call: t is a non-empty string consisting of lowercase Latin letters, with a length not exceeding 100 characters.
def func():
    t = input()
    for i in range(1, len(t)):
        if t[i:] == t[:len(t) - i]:
            print('YES')
            print(t[:len(t) - i])
            exit()
        
    #State of the program after the  for loop has been executed: If `len(t) > 1`, the loop will check each substring `t[i:]` against `t[:len(t) - i]` for `i` from 1 to `len(t) - 1`. If a match is found, 'YES' and the matching substring `t[:len(t) - i]` are printed, and the program exits. If no match is found, the loop completes all iterations without printing anything. If `len(t) <= 1`, the loop does not execute.
    print('NO')
#Overall this is what the function does:The function `func` reads a non-empty string `t` consisting of lowercase Latin letters (with a maximum length of 100 characters) from the user. It then checks if there exists a non-empty proper prefix of `t` that is also a suffix of `t`. If such a prefix-suffix match is found, the function prints "YES" followed by the matched prefix and terminates the program. If no such match is found, the function prints "NO" and continues execution. The function does not return any value. If the input string `t` has a length of 1, the function will always print "NO" because a single-character string cannot have a non-empty proper prefix that is also a suffix.

