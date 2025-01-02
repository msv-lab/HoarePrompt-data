#State of the program right berfore the function call: a1, a2, a3, and a4 are non-negative integers such that 1 ≤ a1, a2, a3, a4 ≤ 10^6.
def func():
    a = [int(x) for x in stdin.readline().split()]
    if (abs(a[2] - a[3]) > 1) :
        print(-1)
    else :
        tem, tem2 = ['4'], ['7']
        four, seven = 1, 0
        four2, seven2 = 0, 1
        for i in range(a[2] + a[3]):
            if i & 1:
                tem.append('4')
                tem2.append('7')
                four += 1
                seven2 += 1
            else:
                tem.append('7')
                tem2.append('4')
                four2 += 1
                seven += 1
            
        #State of the program after the  for loop has been executed: `a3 + a4 > 0`, `i` is `a3 + a4 - 1`. If `i & 1` is true, then `tem` will contain alternating '4' and '7' starting with '4' for each odd index up to `a3 + a4 - 1`, and `tem2` will contain alternating '7' and '4' starting with '7' for each odd index up to `a3 + a4 - 1`. The counts `four` and `seven2` will each be incremented by the number of odd indices (i.e., `a3 + a4 // 2` if `a3 + a4` is odd, otherwise `a3 + a4 // 2`). The counts `four2` and `seven` will each be incremented by the number of even indices (i.e., `(a3 + a4 + 1) // 2` if `a3 + a4` is odd, otherwise `(a3 + a4) // 2`). If `i & 1` is false, the same logic applies but starting with '7' and '4' respectively. If the loop does not execute (`a3 + a4 <= 0`), `i` remains 0, `tem` is `['4']`, `tem2` is `['7']`, `four` is 1, `seven2` is 1, `four2` is 0, and `seven` is 0.
        if ((four > a[0] or seven > a[1]) and (four2 > a[0] or seven2 > a[1])) :
            print(-1)
        else :
            if ((four > a[0] or seven > a[1]) or a[2] < a[3]) :
                tem, four, seven = tem2, four2, seven2
            #State of the program after the if block has been executed: *`a3 + a4 > 0`, `i` is `a3 + a4 - 1`, `tem` is `['7']`, `tem2` is `['7']`, `four` is 0, `seven2` is 1, `four2` is 0, `seven` is 1, `i & 1` is false, and the condition `((four > a[0] or seven > a[1]) or a[2] < a[3])` is true, as the else part does not change these values.
            ext4, ext7 = '4' * (a[0] - four), '7' * (a[1] - seven)
            if (tem[-1] == '7') :
                print('%s%s%s%s' % (tem[0], ext4, ''.join(tem[1:]), ext7))
            else :
                print('%s%s%s%s%s' % (tem[0], ext4, ''.join(tem[1:-1]), ext7, tem[-1]))
            #State of the program after the if-else block has been executed: *`a3 + a4 > 0`, `i` is `a3 + a4 - 1`, `tem` is `['7']`, `tem2` is `['7']`, `four` is 0, `seven2` is 1, `four2` is 0, `seven` is 1, `i & 1` is false. If `tem[-1] == '7'`, the printed string is `'7477'`. Otherwise, the print statement outputs `'7' + '4' * a[0] + '7' * (a[1] - 1) + '7'`.
        #State of the program after the if-else block has been executed: *`a3 + a4 > 0`, `i` is `a3 + a4 - 1`. Depending on the if condition `((four > a[0] or seven > a[1]) and (four2 > a[0] or seven2 > a[1]))`, the program either continues with `tem` containing alternating '4' and '7' starting with '4' for each odd index up to `a3 + a4 - 1`, `tem2` containing alternating '7' and '4' starting with '7' for each odd index up to `a3 + a4 - 1`, `four` and `seven2` incremented by the number of odd indices (`a3 + a4 // 2` if `a3 + a4` is odd, otherwise `a3 + a4 // 2`), and `four2` and `seven` incremented by the number of even indices (`(a3 + a4 + 1) // 2` if `a3 + a4` is odd, otherwise `(a3 + a4) // 2`), or it sets `tem` to `['7']`, `tem2` to `['7']`, `four` to 0, `seven2` to 1, `four2` to 0, `seven` to 1, and `i & 1` to false. If `tem[-1] == '7'`, the printed string is `'7477'`. Otherwise, the print statement outputs `'7' + '4' * a[0] + '7' * (a[1] - 1) + '7'`
    #State of the program after the if-else block has been executed: *`a1`, `a2`, `a3`, `a4` are integers, and `a` is a list containing `[a1, a2, a3, a4]`. If `|a[2] - a[3]| > 1`, the printed value is `-1`. Otherwise, depending on the condition `((four > a[0] or seven > a[1]) and (four2 > a[0] or seven2 > a[1]))`, the program either continues with `tem` containing alternating '4' and '7' starting with '4' for each odd index up to `a3 + a4 - 1`, `tem2` containing alternating '7' and '4' starting with '7' for each odd index up to `a3 + a4 - 1`, `four` and `seven2` incremented by the number of odd indices (`a3 + a4 // 2` if `a3 + a4` is odd, otherwise `a3 + a4 // 2`), and `four2` and `seven` incremented by the number of even indices (`(a3 + a4 + 1) // 2` if `a3 + a4` is odd, otherwise `(a3 + a4) // 2`), or it sets `tem` to `['7']`, `tem2` to `['7']`, `four` to 0, `seven2` to 1, `four2` to 0, `seven` to 1, and `i & 1` to false. If `tem[-1] == '7'`, the printed string is `'7477'`. Otherwise, the print statement outputs `'7' + '4' * a[0] + '7' * (a[1] - 1) + '7'`.
#Overall this is what the function does:The function reads four non-negative integers \(a1, a2, a3,\) and \(a4\) from standard input, where \(1 \leq a1, a2, a3, a4 \leq 10^6\). It checks if the absolute difference between \(a3\) and \(a4\) is greater than 1. If it is, the function prints \(-1\). Otherwise, it constructs two strings, `tem` and `tem2`, each of length \(a3 + a4\), containing alternating '4' and '7'. If the total number of '4's and '7's in both `tem` and `tem2` exceed the limits specified by \(a1\) and \(a2\), or if \(a3 < a4\), it switches `tem` to contain only '7's and `tem2` to contain only '7's, setting the respective counters to zero. Finally, it prints a string based on whether `tem` ends with '7' or not. The function does not return any value but prints the result directly.

