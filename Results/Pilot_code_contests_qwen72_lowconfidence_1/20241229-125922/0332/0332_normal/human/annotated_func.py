#State of the program right berfore the function call: The input consists of two strings, s and t, each of length n (1 ≤ n ≤ 3·10^5), containing only lowercase English letters.
def func():
    rstr = lambda : stdin.readline().strip()
    s, t = sorted(rstr()), sorted(rstr(), reverse=True)
    le = len(s)
    if (le == 1) :
        print(s[0])
    else :
        if (le == 2) :
            print(min(s[0] + t[0], t[0] + s[0]))
        else :
            if (s[0] <= t[0]) :
                ans = []
                for i in range(le):
                    ans.append(t[i >> 1] if i & 1 else s[i >> 1])
                    
                #State of the program after the  for loop has been executed: `s` is a sorted list of characters from the first input string in ascending order, `t` is a sorted list of characters from the second input string in descending order, each of length `n`, `le` is `n` and must be greater than 1, `le` is not equal to 1, `le` is not equal to 2, the first character of `s` is less than or equal to the first character of `t`, `ans` is a list of length `n` where `ans[2k] = s[k]` and `ans[2k+1] = t[k]` for `k` ranging from 0 to `(n-1)//2`.
                if (le & 1 and ans[-1] > ans[-2]) :
                    ans[-1], ans[-2] = ans[-2], ans[-1]
                #State of the program after the if block has been executed: *`s` is a sorted list of characters from the first input string in ascending order, `t` is a sorted list of characters from the second input string in descending order, each of length `n`, `le` is `n` and must be greater than 1, `le` is not equal to 1, `le` is not equal to 2, the first character of `s` is less than or equal to the first character of `t`, `ans` is a list of length `n` where `ans[2k] = s[k]` and `ans[2k+1] = t[k]` for `k` ranging from 0 to `(n-1)//2`. If `le` is odd and the last element of `ans` is greater than the second-to-last element of `ans`, the last two elements of `ans` are swapped so that the last element is now less than the second-to-last element. Otherwise, `ans` remains unchanged.
                print(''.join(ans))
            else :
                mds, mdt, ans = int(ceil(le / 2)) - 1, (le >> 1) - 1, []
                for i in range(le):
                    if i & 1:
                        ans.append(t[mdt])
                        mdt -= 1
                    else:
                        ans.append(s[mds])
                        mds -= 1
                    
                #State of the program after the  for loop has been executed: `s` is a sorted list of characters from the first input string in ascending order, `t` is a sorted list of characters from the second input string in descending order, each of length `le` which is at least 3, `s[0] > t[0]`, `mds` is `-1`, `mdt` is `-1`, `ans` is a list of characters where characters from `s` and `t` are alternately appended starting with a character from `s` if `le` is even or from `t` if `le` is odd, and the final list `ans` contains exactly `le` elements.
                print(''.join(ans[::-1]))
            #State of the program after the if-else block has been executed: *`s` is a sorted list of characters from the first input string in ascending order, `t` is a sorted list of characters from the second input string in descending order, each of length `le` which is at least 3. If `s[0] <= t[0]`, the concatenated string from `ans` is printed, and the state of the variables remains unchanged. If `s[0] > t[0]`, the list `ans` is reversed and joined into a string, which is then printed, and the values of `s`, `t`, `le`, `mds`, `mdt`, and `ans` remain unchanged.
        #State of the program after the if-else block has been executed: *`s` is a sorted list of characters from the first input string in ascending order, `t` is a sorted list of characters from the second input string in descending order, each of length `n`, and `le` is `n` which is not equal to 1. If `le` is 2, the value `s[0] + t[0]` is printed. Otherwise, if `le` is at least 3, and if `s[0] <= t[0]`, the concatenated string from `ans` is printed, and the state of the variables remains unchanged. If `s[0] > t[0]`, the list `ans` is reversed and joined into a string, which is then printed, and the values of `s`, `t`, `le`, `mds`, `mdt`, and `ans` remain unchanged.
    #State of the program after the if-else block has been executed: *`s` is a sorted list of characters from the first input string in ascending order, `t` is a sorted list of characters from the second input string in descending order, each of length `n` and containing only lowercase English letters, and `le` is `n`. If `le` is 1, the first element of `s` is printed. If `le` is 2, the value `s[0] + t[0]` is printed. If `le` is at least 3, and if `s[0] <= t[0]`, the concatenated string from `ans` is printed, and the state of the variables remains unchanged. If `s[0] > t[0]`, the list `ans` is reversed and joined into a string, which is then printed, and the values of `s`, `t`, `le`, `mds`, `mdt`, and `ans` remain unchanged.
#Overall this is what the function does:The function `func` reads two strings `s` and `t` from standard input, both of which are of equal length `n` (1 ≤ n ≤ 3·10^5) and contain only lowercase English letters. The function then processes these strings to produce a new string based on the following rules:

1. If the length of the strings (`n`) is 1, the function prints the single character from `s`.
2. If the length of the strings is 2, the function prints the lexicographically smaller concatenation of the characters from `s` and `t`.
3. If the length of the strings is greater than 2:
   - If the first character of the sorted `s` is less than or equal to the first character of the sorted `t`, the function constructs a new string by alternating characters from `s` and `t` (starting with `s` for even indices and `t` for odd indices). If the length of the strings is odd and the last character in the constructed string is greater than the second-to-last character, the last two characters are swapped.
   - If the first character of the sorted `s` is greater than the first character of the sorted `t`, the function constructs a new string by alternating characters from `s` and `t` (starting with `t` for even indices and `s` for odd indices), and then reverses the resulting string before printing it.

After the function executes, the original strings `s` and `t` remain sorted in ascending and descending order, respectively, and the final state of the program includes the printed output string. The function does not return any value.

