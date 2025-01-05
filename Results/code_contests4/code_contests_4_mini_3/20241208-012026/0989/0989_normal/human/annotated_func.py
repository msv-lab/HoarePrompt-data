#State of the program right berfore the function call: L is a positive integer such that 1 ≤ L ≤ 10^5, and A is a positive integer represented as a string with a length between 1 and 100,000 characters, where each character is a digit from 1 to 9, and A is strictly less than 10^100,000.
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
                
            #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `tem` contains the first `n` characters of `s`, with the last character incremented by 1 (if it was not '9'), or all characters set to '0' if they were all '9'.
            ans2 = ''.join(tem) * (len(s) // n)
            print(ans1 if ans1 > s else ans2)
        #State of the program after the if-else block has been executed: *`n` is an input integer and `s` is a string of length that is a multiple of `n`. If the first `n` characters of `s` are all '9's, the output is `ans1` (a string of '9's repeated `len(s) // n` times). Otherwise, if `n` is greater than or equal to 1, `tem` is formed by taking the first `n` characters of `s` and incrementing the last character (if it is not '9'), or setting all characters to '0' if they are all '9'. The output is `ans1` if it is greater than `s`, otherwise it is `ans2` (the modified `tem` repeated `len(s) // n` times).
    #State of the program after the if-else block has been executed: *`n` is an input integer and `s` is a string stripped of whitespace. If the length of `s` is not a multiple of `n`, the output is a string `tem` which consists of '1' followed by (n - 1) zeros, repeated `len(s) // n + 1` times. If the length of `s` is a multiple of `n`, and if the first `n` characters of `s` are all '9's, the output is a string of '9's repeated `len(s) // n` times. Otherwise, if `n` is greater than or equal to 1, `tem` is formed by taking the first `n` characters of `s` and incrementing the last character (if it is not '9'), or setting all characters to '0' if they are all '9'. The output will be `ans1` if it is greater than `s`, otherwise, it will be `ans2`, which is the modified `tem` repeated `len(s) // n` times.
#Overall this is what the function does:The function accepts an integer `n` and a string `s` representing a positive integer. It processes `s` based on its length relative to `n`. If the length of `s` is not a multiple of `n`, it outputs a string '1' followed by `n-1` zeros, repeated enough times to cover the length of `s`. If the length is a multiple of `n` and the first `n` characters of `s` are all '9's, it outputs a string of '9's repeated for the length of `s`. Otherwise, it creates a modified version of the first `n` characters of `s` by incrementing the last digit (unless it is '9' in which case it turns to '0'), and then outputs the greater of this modified string or the original repetition of the first `n` characters of `s`. The function does not return any value directly, but it prints the resulting string based on these conditions.

