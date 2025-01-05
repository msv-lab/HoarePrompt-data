#State of the program right berfore the function call: L is a positive integer such that 1 ≤ L ≤ 100000, and A is a positive integer represented as a string with a length of at most 100000 digits, where A is greater than 0.
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
                
            #State of the program after the  for loop has been executed: `L` is a positive integer such that 1 ≤ `L` ≤ 100000; `A` is a positive integer represented as a string; `n` is greater than 0; `tem` is the character list representing the string incremented appropriately; `i` is the index of the last character checked in the loop.
            ans2 = ''.join(tem) * (len(s) // n)
            print(ans1 if ans1 > s else ans2)
        #State of the program after the if-else block has been executed: *`L` is a positive integer such that 1 ≤ L ≤ 100000; `A` is a positive integer represented as a string; `n` is an input integer; `s` is an input string with a length divisible by `n`. If the first `n` characters of `s` are all '9's, then `ans1` is a string of '9' repeated `len(s)` times, and `ans2` is '1' followed by `n` number of '0's; the output will be `ans1` if `ans1` is greater than `s`, otherwise, `ans2` will be printed repeated `len(s) // n` times. If the first `n` characters of `s` are not all '9's, then `ans2` is formed by repeating the concatenated characters of `tem` a number of times determined by `len(s) // n`; the output will be `ans1` if `ans1` is greater than `s`, otherwise, `ans2` is printed.
    #State of the program after the if-else block has been executed: *`L` is a positive integer such that 1 ≤ `L` ≤ 100000; `A` is a positive integer represented as a string; `n` is an input integer; `s` is an input string. If the length of `s` is not divisible by `n`, `tem` is '1' concatenated with '0' repeated (n - 1) times, and the output is `tem` concatenated (len(s) // n + 1) times. If the length of `s` is divisible by `n`, and the first `n` characters of `s` are all '9's, then `ans1` is a string of '9' repeated `len(s)` times, and `ans2` is '1' followed by `n` number of '0's; the output will be `ans1` if `ans1` is greater than `s`, otherwise, `ans2` will be printed repeated `len(s) // n` times. If the first `n` characters of `s` are not all '9's, then `ans2` is formed by repeating the concatenated characters of `tem` a number of times determined by `len(s) // n`; the output will be `ans1` if `ans1` is greater than `s`, otherwise, `ans2` will be printed.
#Overall this is what the function does:The function reads an integer `n` and a string `s` representing a positive integer. If the length of `s` is not divisible by `n`, it outputs a string that consists of '1' followed by `n-1` zeros, repeated enough times to match the length of `s`. If the length of `s` is divisible by `n`, it checks if the first `n` characters of `s` are all '9's; if they are, it outputs a string of '9's of the same length as `s` or '1' followed by `n` zeros, whichever is greater. If the first `n` characters are not all '9's, it increments the last non-'9' character in these `n` characters, constructs a new string by repeating this incremented string to match the length of `s`, and outputs the greater of this new string or the previously constructed string. The function does not accept parameters and has no explicit return value.

