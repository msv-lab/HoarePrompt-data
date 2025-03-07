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
        
    #State: For each of the `t` test cases, the variables `ac` and `bc` will hold the count of 'A's and 'B's in the respective string of length 5, but these values will not be stored or accessible after the loop for each test case completes. The state of `t` and the input strings remains unchanged.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: For each of the `t` test cases, the variables `ac` and `bc` will hold the count of 'A's and 'B's in the respective string of length 5. If `ac` is greater than `bc`, then `ac` is greater than `bc`. Otherwise, `ac` is less than or equal to `bc`. The state of `t` and the input strings remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string of length 5 consisting only of 'A' and 'B'. It then prints 'A' if the string contains more 'A's than 'B's, otherwise it prints 'B'. The function does not return any value; it only prints the result for each test case.

