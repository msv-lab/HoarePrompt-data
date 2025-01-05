#State of the program right berfore the function call: L is a positive integer such that 1 ≤ L ≤ 100000, and A is a positive integer represented as a string with a length between 1 and 100000 characters.
def func():
    n, s = int(input()), stdin.readline().strip()
    if (len(s) % n) :
        tem = '1' + '0' * (n - 1)
        print(tem * (len(s) // n + 1))
    else :
        if (s[:n] == '9' * n) :
            ans1, ans2 = '9' * len(s), '1' + '0' * n
            print(ans1 if ans1 > s else ans2 * (len(s) // n))
        else :
            ans1, tem = s[:n] * (len(s) // n), list(s[:n])
            for i in range(n - 1, -1, -1):
                if tem[i] != '9':
                    tem[i] = str(int(tem[i]) + 1)
                    break
                
                tem[i] = '0'
                
            #State of the program after the  for loop has been executed: `L` is a positive integer such that 1 ≤ `L` ≤ 100000; `A` is a positive integer represented as a string with a length between 1 and 100000 characters; `n` is at least 1; `tem` is a list of characters where at least one character has been incremented or all characters are '0'.
            ans2 = ''.join(tem) * (len(s) // n)
            print(ans1 if ans1 > s else ans2)
        #State of the program after the if-else block has been executed: *`L` is a positive integer such that 1 ≤ L ≤ 100000; `A` is a positive integer represented as a string with a length between 1 and 100000 characters; `n` is an input integer; `s` is an input string whose length is divisible by `n`. If the first `n` characters of `s` are all '9's, then `ans1`, a string of '9's with length equal to `len(s)`, is compared to `s`. If `ans1` is greater than `s`, the output is `ans1`; otherwise, the output is '1' followed by `n` zeros repeated `len(s) // n` times. In the else case, `ans2` is formed by repeating the concatenated string of `tem`, `len(s) // n` times, and the output will be `ans1` if it is greater than `s`, otherwise it will be `ans2`.
    #State of the program after the if-else block has been executed: *`L` is a positive integer such that 1 ≤ L ≤ 100000, `A` is a positive integer represented as a string with a length between 1 and 100000 characters, `n` is an input integer, and `s` is an input string. If the length of `s` is not divisible by `n`, the output is `tem` (which is '1' followed by (n - 1) zeros) repeated (len(s) // n + 1) times. Otherwise, if the length of `s` is divisible by `n` and the first `n` characters of `s` are all '9's, the output is '9's with length equal to `len(s)` if it is greater than `s`, otherwise it's '1' followed by `n` zeros repeated `len(s) // n` times. If the first `n` characters of `s` are not all '9's, the output is formed by repeating the concatenated string of `tem` (which is '1' followed by (n - 1) zeros) for `len(s) // n` times, yielding `ans2`, with the output being `ans1` if it exceeds `s`, otherwise it will be `ans2`.
#Overall this is what the function does:The function reads an integer `n` and a string `s` representing a positive integer. It checks if the length of `s` is divisible by `n`. If not, it prints '1' followed by (n-1) zeros repeated (len(s) // n + 1) times. If the length is divisible by `n` and the first `n` characters of `s` are all '9's, it prints a string of '9's of the same length as `s` if it's greater than `s`, otherwise it prints '1' followed by `n` zeros repeated (len(s) // n) times. If the first `n` characters are not all '9's, it increments the last non-'9' character among the first `n` characters of `s`, constructs a new string by repeating it (len(s) // n) times, and prints the greater of this new string or the repeated first `n` characters.

