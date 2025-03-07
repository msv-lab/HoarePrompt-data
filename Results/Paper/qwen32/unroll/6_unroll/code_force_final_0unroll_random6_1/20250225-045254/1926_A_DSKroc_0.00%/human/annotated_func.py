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
        
    #State: After the loop executes all the iterations, for each of the `t` test cases, the variables `ac` and `bc` hold the count of 'A's and 'B's respectively in the string `s` of that test case. The variable `s` holds the last input string processed, and `q` holds the value `t-1`. The initial value of `t` and the distinct strings provided as input remain unchanged.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: After the loop executes all the iterations, for each of the `t` test cases, the variables `ac` and `bc` hold the count of 'A's and 'B's respectively in the string `s` of that test case. The variable `s` holds the last input string processed, and `q` holds the value `t-1`. The initial value of `t` and the distinct strings provided as input remain unchanged. If `ac` is greater than `bc`, then `ac` is greater than `bc`; otherwise, `ac` is less than or equal to `bc`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case consists of a distinct string of length 5 containing only 'A' and 'B'. For each test case, the function counts the occurrences of 'A' and 'B' in the string and prints 'A' if there are more 'A's than 'B's, otherwise it prints 'B'.

