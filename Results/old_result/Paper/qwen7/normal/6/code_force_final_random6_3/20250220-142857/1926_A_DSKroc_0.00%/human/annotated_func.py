#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string consists of exactly 5 characters where each character is either 'A' or 'B'.
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
        
    #State: After the loop executes all its iterations, `ac` will be equal to the total number of 'A' characters in the string `s`, `q` will be equal to `t-1`, `bc` will be equal to the total number of non-'A' characters in the string `s`, and `s` will be the original input string.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: After the if-else block executes, `ac` will be equal to the total number of 'A' characters in the string `s`, `q` will be equal to `t-1`, `bc` will be equal to the total number of non-'A' characters in the string `s`, and `s` will be the original input string. If `ac` is greater than `bc`, then `ac` remains unchanged and `bc` remains unchanged. If `ac` is less than or equal to `bc`, then `ac` remains unchanged and `bc` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` and `t` strings, each consisting of exactly 5 characters ('A' or 'B'), and counts the number of 'A' and 'B' characters in each string. It then prints 'A' if the count of 'A' characters is greater than the count of 'B' characters in the string; otherwise, it prints 'B'. The function does not return any value but prints the result for each string.

