#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of characters 'A' and 'B'.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        l = 0
        
        h = 0
        
        for j in a:
            if j == 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        else:
            print('B')
        
    #State: All strings `a` have been fully processed, and for each string, `l` contains the total count of 'A' characters, while `h` contains the total count of non-'A' characters. The variable `i` will range from `0` to `t-1`, and `t` remains the same as its initial value. If for any string `a`, the count of 'A' characters (`l`) is greater than the count of non-'A' characters (`h`), then 'A' is printed for that string. Otherwise, 'B' is printed.
#Overall this is what the function does:The function processes `t` input strings, each of length 5 consisting of characters 'A' and 'B'. For each string, it counts the number of 'A' characters and the number of non-'A' characters. If the count of 'A' characters is greater than the count of non-'A' characters, it prints 'A'; otherwise, it prints 'B'. After processing all strings, the function does not return anything.

