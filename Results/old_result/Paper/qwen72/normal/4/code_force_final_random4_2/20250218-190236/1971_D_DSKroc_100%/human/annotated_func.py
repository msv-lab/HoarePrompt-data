#State of the program right berfore the function call: The function should take a single parameter, a string `s` consisting of characters '0' and '1' where 1 <= len(s) <= 500. The function is expected to handle multiple test cases, where the number of test cases `t` is an integer such that 1 <= t <= 500.
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
        
    #State: `t` is an input integer such that 1 <= t <= 500, `q` is `t - 1`, `s` is a new input string with at least 2 characters, `i` is `len(s) - 2`, `count` is the number of positions in the string `s` where the integer value of the character at position `i` is not equal to the integer value of the character at position `i + 1`. If `flag` is 0, indicating that there is no position in the string `s` where the integer value of the character at position `i` is less than the integer value of the character at position `i + 1`, then the program prints `count + 1`. If `flag` is 1, indicating that there is at least one position in the string `s` where the integer value of the character at position `i` is less than the integer value of the character at position `i + 1`, then the program prints `count`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases, where 1 <= t <= 500. For each test case, it reads a string `s` consisting of characters '0' and '1' (1 <= len(s) <= 500). It then processes each string `s` to count the number of positions where the integer value of the character at position `i` is not equal to the integer value of the character at position `i + 1`. If there is no position where the integer value of the character at position `i` is less than the integer value of the character at position `i + 1`, the function prints `count + 1`. Otherwise, it prints `count`. After processing all test cases, the function concludes.

