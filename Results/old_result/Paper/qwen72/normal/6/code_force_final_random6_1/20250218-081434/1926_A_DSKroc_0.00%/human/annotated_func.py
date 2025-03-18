#State of the program right berfore the function call: The function `func` is expected to be called within a loop or context where it processes multiple test cases. Each test case provides a string `s` of length 5 consisting of letters \texttt{A} and \texttt{B}. The total number of test cases `t` is an integer such that 1 <= t <= 32, and all `t` strings are distinct.
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
        
    #State: `t` is an integer such that 1 <= t <= 32, `s` is an input string of length 5 consisting of letters 'A' and 'B', `q` is `t-1`, `ac` is the number of 'A' characters in the last input string `s`, and `bc` is the number of 'B' characters in the last input string `s`.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: *`t` is an integer such that 1 <= t <= 32, `s` is an input string of length 5 consisting of letters 'A' and 'B', `q` is `t-1`, `ac` is the number of 'A' characters in the last input string `s`, and `bc` is the number of 'B' characters in the last input string `s`. If `ac` > `bc`, the number of 'A' characters in `s` is greater than the number of 'B' characters in `s`. Otherwise, `ac` is less than or equal to `bc`.
#Overall this is what the function does:The function `func` processes multiple test cases, each providing a distinct string `s` of length 5 consisting of letters `A` and `B`. The total number of test cases `t` is an integer between 1 and 32. After processing all test cases, the function prints either 'A' or 'B' based on the last input string `s`: it prints 'A' if the number of 'A' characters in `s` is greater than the number of 'B' characters, and 'B' otherwise. The function does not return any value.

