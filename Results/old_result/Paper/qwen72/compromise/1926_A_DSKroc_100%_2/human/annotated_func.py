#State of the program right berfore the function call: t is an integer such that 1 <= t <= 32, and for each of the t test cases, there is a string of length 5 consisting only of the characters 'A' and 'B'. All t strings are distinct.
def func():
    t = int(input())
    for q in range(t):
        ac = 0
        
        bc = 0
        
        s = input()
        
        for i in s:
            if i == 'A':
                ac += 1
            else:
                bc += 1
        
        if ac > bc:
            print('A')
        else:
            print('B')
        
    #State: `t` is greater than or equal to the number of iterations executed, `q` is equal to `t - 1`, `s` is the last input string, `ac` is the number of 'A' characters in the last input string, and `bc` is the number of non-'A' characters in the last input string. If `ac` is greater than `bc`, the number of 'A' characters in the last input string is greater than the number of non-'A' characters. Otherwise, the number of 'A' characters in the last input string is less than or equal to the number of non-'A' characters.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where each test case is a string of length 5 consisting only of the characters 'A' and 'B'. For each test case, the function counts the occurrences of 'A' and 'B' in the string. It then prints 'A' if the count of 'A' is greater than the count of 'B', otherwise, it prints 'B'. After processing all `t` test cases, the function completes, and the final state includes the printed results for each test case.

