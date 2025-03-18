#State of the program right berfore the function call: The function should take a single argument, `s`, which is a binary string (a string consisting of characters '0' and '1') with a length of 1 to 500.
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
        
    #State: The value of `t` is decreased by the number of iterations the loop has executed, and `s` will be the last input binary string provided during the loop's execution. The variables `count` and `flag` will be reset to 0 at the start of each iteration and will be used to calculate the number of adjacent character changes and the presence of an increasing sequence, respectively, for each input string `s`. After the loop finishes, `t` will be 0, and `s` will be the last input binary string.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of binary strings to process. For each of the `t` binary strings `s` (where `s` is a string of '0's and '1's with a length between 1 and 500), the function calculates the number of adjacent character changes in `s`. If there is no increasing sequence (i.e., no '0' followed by '1') in `s`, it prints the count of adjacent changes plus one; otherwise, it prints the count of adjacent changes. After processing all `t` strings, the function completes and the value of `t` is 0, while `s` will be the last input binary string. The function does not return any value.

