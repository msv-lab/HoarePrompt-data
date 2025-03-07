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
        
    #State: For each of the t test cases, `ac` and `bc` will hold the count of 'A's and 'B's respectively in the corresponding string of length 5, but these values will not be retained outside the loop as they are reinitialized in each iteration. The variable `t` and the input strings remain unchanged.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: For each of the t test cases, `ac` and `bc` will hold the count of 'A's and 'B's respectively in the corresponding string of length 5, but these values will not be retained outside the loop as they are reinitialized in each iteration. The variable `t` and the input strings remain unchanged. If the current value of `ac` is greater than the current value of `bc`, then `ac` is greater than `bc`. Otherwise, `ac` is less than or equal to `bc`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where each test case is a distinct string of length 5 consisting only of the characters 'A' and 'B'. For each test case, it counts the occurrences of 'A' and 'B' and prints 'A' if 'A' appears more times than 'B', otherwise it prints 'B'. The function does not return any value; it only prints the result for each test case.

