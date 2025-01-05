#State of the program right berfore the function call: **
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
                
            #State of the program after the  for loop has been executed: `n` is an input integer, `s` is a string input from stdin, the length of `s` is divisible by `n`, the first `n` characters of `s` are all '9's, `ans1` contains the first `n` characters of `s` repeated `len(s) // n` times, `tem` contains the first `n` characters of `s` all set to '0'
            ans2 = ''.join(tem) * (len(s) // n)
            print(ans1 if ans1 > s else ans2)
        #State of the program after the if-else block has been executed: *`n` is an input integer, `s` is a string input from stdin, the length of `s` is divisible by `n`. If the first `n` characters of `s` are all '9's, the code prints a string of '9's with the same length as `s`. Otherwise, the first `n` characters of `s` are all '9's, `ans1` contains the first `n` characters of `s` repeated `len(s) // n` times, `tem` contains the first `n` characters of `s` all set to '0', `ans2` is a string of '0's repeated `len(s) // n` times, and either `ans1` or `ans2` is printed based on the comparison with `s`.
    #State of the program after the if-else block has been executed: *`n` is an input integer, `s` is a string input from stdin. If the length of `s` is not divisible by `n`, `tem` is a string consisting of '1' followed by '0's, and the result of the print statement. If the length of `s` is divisible by `n`, and the first `n` characters of `s` are all '9's, the code prints a string of '9's with the same length as `s`. Otherwise, if the first `n` characters of `s` are all '9's, `ans1` contains the first `n` characters of `s` repeated `len(s) // n` times, `tem` contains the first `n` characters of `s` all set to '0', `ans2` is a string of '0's repeated `len(s) // n` times, and either `ans1` or `ans2` is printed based on the comparison with `s`.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `s` from the standard input. If the length of `s` is not divisible by `n`, it prints a string consisting of '1' followed by '0's repeated enough times. If the length of `s` is divisible by `n`, it checks if the first `n` characters of `s` are all '9's. If they are, it prints a string of '9's with the length of `s`. If not, it modifies `s` based on certain conditions and prints the result. The function does not have a return value.

