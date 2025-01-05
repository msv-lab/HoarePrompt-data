#State of the program right berfore the function call: A is a positive integer and L is a positive integer such that 1 ≤ L ≤ 10^5 and 1 ≤ A ≤ 10^100000.**
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
                
            #State of the program after the  for loop has been executed: After the loop finishes executing, `A`, `L`, `n`, `s`, `ans1` are positive integers, `tem` is a list containing the first `n` characters of `s` with a specific pattern modified, `i` is 0
            ans2 = ''.join(tem) * (len(s) // n)
            print(ans1 if ans1 > s else ans2)
        #State of the program after the if-else block has been executed: *A is a positive integer, L is a positive integer such that 1 ≤ L ≤ 10^5 and 1 ≤ A ≤ 10^100000, n is an input integer, s is a string. The length of s is divisible by n. If the first n characters of s are all '9', then ans1 is a string consisting of '9' repeated len(s) times, ans2 is a string consisting of '1' followed by '0' repeated n times, and the output is either ans1 if ans1 is greater than s, otherwise, it is '10' repeated len(s) // n times. Otherwise, after the loop execution, `A`, `L`, `n`, `s`, `ans1` are positive integers, `tem` is a list containing the first `n` characters of `s` with a specific pattern modified, `i` is 0, and `ans2` is a string representing the concatenation of the first `n` characters of `s` repeated `(len(s) // n)` times.
    #State of the program after the if-else block has been executed: *A is a positive integer, L is a positive integer such that 1 ≤ L ≤ 10^5 and 1 ≤ A ≤ 10^100000, n is an input integer, s is a string. If the length of s is not divisible by n, then `tem` is a string consisting of '1' followed by (n - 1) zeros, and the repeated string s. If the length of s is divisible by n, and the first n characters of s are all '9', then ans1 is a string consisting of '9' repeated len(s) times, ans2 is a string consisting of '1' followed by '0' repeated n times, and the output is either ans1 if ans1 is greater than s, otherwise, it is '10' repeated len(s) // n times. Otherwise, after the loop execution, A, L, n, s, ans1 are positive integers, tem is a list containing the first n characters of s with a specific pattern modified, i is 0, and ans2 is a string representing the concatenation of the first n characters of s repeated (len(s) // n) times.
#Overall this is what the function does:The function `func` reads an integer `n` and a string `s` as input. It then performs different operations based on the length of `s` and the contents of the first `n` characters of `s`. If the length of `s` is not divisible by `n`, it creates a specific string pattern and prints it. If the first `n` characters of `s` are all '9', it generates specific strings `ans1` and `ans2` and prints the larger one. Otherwise, it modifies the first `n` characters of `s` based on a certain pattern, generates strings `ans1` and `ans2`, and prints the larger one. The function does not have a return value.

