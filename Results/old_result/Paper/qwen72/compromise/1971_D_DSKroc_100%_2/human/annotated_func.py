#State of the program right berfore the function call: The function should take a single argument, a binary string `s` (1 ≤ |s| ≤ 500), where |s| denotes the length of the string `s`. The string `s` consists only of characters '0' and '1'.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        flag = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) != int(s[i + 1]):
                count += 1
            if int(s[i]) < int(s[i + 1]):
                flag = 1
        
        if flag == 0:
            print(count + 1)
        else:
            print(count)
        
    #State: `s` is an input binary string of length 1 to 500, `i` is `len(s) - 2`, `q` is `t - 1`, `t` remains the same, and `count` is the number of positions in `s` where adjacent characters are different. If `flag` is 0, it indicates that there does not exist any position where the integer value of `s[i]` is less than the integer value of `s[i + 1]` for all `i` from 0 to `len(s) - 2`. If `flag` is 1, it indicates that there exists at least one position where the integer value of `s[i]` is less than the integer value of `s[i + 1]` for all `i` from 0 to `len(s) - 2.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of binary strings to process. For each of the `t` binary strings `s` (where 1 ≤ |s| ≤ 500), it calculates the number of positions where adjacent characters are different. If the string `s` does not contain any position where the integer value of `s[i]` is less than the integer value of `s[i + 1]` for all `i` from 0 to `len(s) - 2`, it prints the count of such positions plus one. Otherwise, it prints the count of such positions. The function does not return any value.

