#State of the program right berfore the function call: a1, a2, a3, and a4 are positive integers such that 1 <= a1, a2, a3, a4 <= 10^6.
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
            
        #State of the program after the  for loop has been executed: `a` is a list containing the integers read from the input, where `a[2]` and `a[3]` are valid integers, the absolute difference between `a[2]` and `a[3]` is less than or equal to 1, and `a[2] + a[3]` is non-negative; `tem` is a list containing alternating '4' and '7' based on whether the index `i` is odd or even, `tem2` is a list containing alternating '7' and '4' based on whether the index `i` is odd or even, `four` is the count of times `tem` appends '4', `seven2` is the count of times `tem2` appends '7', `four2` is the count of times `tem` appends '7', and `seven` is the count of times `tem2` appends '4'.
        if ((four > a[0] or seven > a[1]) and (four2 > a[0] or seven2 > a[1])) :
            print(-1)
        else :
            if ((four > a[0] or seven > a[1]) or a[2] < a[3]) :
                tem, four, seven = tem2, four2, seven2
            #State of the program after the if block has been executed: *`tem` and `tem2` are lists containing alternating '4' and '7' or '7' and '4' based on the index parity. `four` and `seven2` are counts of '7' in `tem` and `tem2` respectively, while `seven` and `four2` are counts of '4' in `tem2` and `tem` respectively. If the condition `((four > a[0] or seven > a[1]) or a[2] < a[3])` is true, then either `four` is less than or equal to `a[0]` and `seven2` is less than or equal to `a[1]`, or `four2` is less than or equal to `a[0]` and `seven` is less than or equal to `a[1]`. If the condition is false, no change is made to `four`, `seven`, `four2`, and `seven2`.
            ext4, ext7 = '4' * (a[0] - four), '7' * (a[1] - seven)
            if (tem[-1] == '7') :
                print('%s%s%s%s' % (tem[0], ext4, ''.join(tem[1:]), ext7))
            else :
                print('%s%s%s%s%s' % (tem[0], ext4, ''.join(tem[1:-1]), ext7, tem[-1]))
            #State of the program after the if-else block has been executed: *`tem` and `tem2` are lists containing alternating '4' and '7' or '7' and '4' based on the index parity. `four` and `seven2` are counts of '7' in `tem` and `tem2` respectively, `seven` and `four2` are counts of '4' in `tem2` and `tem` respectively. `ext4` is a string of '4's equal to `a[0] - four`, `ext7` is a string of '7's equal to `a[1] - seven`. If the last element of `tem` is '7', then `tem` is updated to `tem[0] + '4' * (a[0] - four) + ''.join(tem[1:]) + '7' * (a[1] - seven)`. Otherwise, `tem` is updated to `tem[0]` followed by a string of '4's of length `length_tem - four`, then a sequence of alternating '4' and '7' from `tem[1:-1]`, followed by a string of '7's of length `a[1] - seven`, and ending with a '4'.
        #State of the program after the if-else block has been executed: `a` is a list containing the integers read from the input, where `a[2]` and `a[3]` are valid integers, the absolute difference between `a[2]` and `a[3]` is less than or equal to 1, and `a[2] + a[3]` is non-negative; `tem` and `tem2` are lists containing alternating '4' and '7' or '7' and '4' based on the index parity; `four` and `seven2` are counts of '7' in `tem` and `tem2` respectively, `seven` and `four2` are counts of '4' in `tem2` and `tem` respectively. If `((four > a[0] or seven > a[1]) and (four2 > a[0] or seven2 > a[1]))` is true, the program prints -1. Otherwise, `tem` is updated according to the specified rules involving `a[0]` and `a[1]`.
    #State of the program after the if-else block has been executed: `a` is a list containing integers read from the input. If the absolute difference between the third and fourth elements of `a` is greater than 1, then -1 is printed. Otherwise, `a[2] + a[3]` is non-negative, and `tem` and `tem2` are lists containing alternating '4' and '7' or '7' and '4' based on the index parity. `four` and `seven2` are counts of '7' in `tem` and `tem2` respectively, while `seven` and `four2` are counts of '4' in `tem2` and `tem` respectively. The program either prints -1 if `((four > a[0] or seven > a[1]) and (four2 > a[0] or seven2 > a[1]))` is true, or updates `tem` according to the specified rules involving `a[0]` and `a[1]`.
#Overall this is what the function does:The function reads two positive integers a2 and a3 from standard input, where 1 ≤ a2, a3 ≤ 10^6, and checks if their absolute difference is greater than 1. If it is, it prints -1. Otherwise, it generates two lists, `tem` and `tem2`, containing alternating '4' and '7', or '7' and '4', depending on the parity of the index. It then counts the occurrences of '4' and '7' in these lists. Based on certain conditions involving another pair of integers a0 and a1 (also read from standard input, 1 ≤ a0, a1 ≤ 10^6), it either updates the `tem` list or prints -1. Finally, it constructs and prints a string using the counts of '4' and '7' and the contents of the `tem` list, ensuring that the total number of '4's and '7's matches a0 and a1, respectively.

