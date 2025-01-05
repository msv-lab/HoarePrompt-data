#State of the program right berfore the function call: L is a positive integer such that 1 ≤ L ≤ 10^5, and A is a positive integer such that 1 ≤ A ≤ 10^{100000}.**
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
                
            #State of the program after the  for loop has been executed: `L`, `A` are positive integers such that 1 ≤ L ≤ 10^5 and 1 ≤ A ≤ 10^100000 respectively. `n` is an input integer greater than 0. `s` is a string. `ans1` is a string containing concatenated substrings of the first `n` characters of `s. `tem` is a list containing the first `n` characters of `s` where all elements are set to '0'
            ans2 = ''.join(tem) * (len(s) // n)
            print(ans1 if ans1 > s else ans2)
        #State of the program after the if-else block has been executed: *L is a positive integer such that 1 ≤ L ≤ 10^5, A is a positive integer such that 1 ≤ A ≤ 10^100000, n is an input integer, s is a string. If s[:n] is equal to a string of all '9's, then the code will print a string of all '9's if it is greater than s, otherwise it will print a string of '10's repeated n times.
    #State of the program after the if-else block has been executed: *L is a positive integer such that 1 ≤ L ≤ 10^5, A is a positive integer such that 1 ≤ A ≤ 10^100000, n is an input integer, s is a string. If the length of s is not divisible by n, then the program will print the original values of L, A, n, and s. If s[:n] is equal to a string of all '9's, then the code will print a string of all '9's if it is greater than s, otherwise it will print a string of '10's repeated n times.
#Overall this is what the function does:The function `func` accepts two input parameters, L and A, both positive integers with specific ranges. The function reads an integer input `n` and a string `s`. It then performs various operations based on the length of `s` and the content of certain substrings. If the length of `s` is not divisible by `n`, it prints a specific pattern. If the initial substring of `s` contains all '9's, it prints a string of '9's if it is greater than `s`, otherwise a string of '10's repeated multiple times. The function does not have a specified return value.

