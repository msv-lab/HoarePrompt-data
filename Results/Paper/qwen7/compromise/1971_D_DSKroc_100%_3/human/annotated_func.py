#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string such that 1 ≤ |s| ≤ 500.
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
        
    #State: All iterations of the loop have completed. The variable `q` is equal to `t-1`, meaning the loop has executed `t` times. For each input string `s`, the variable `count` holds the number of times a character is followed by a smaller character, plus one if no such pair exists. The variable `flag` is 1 if there is at least one pair of consecutive characters where the first character is less than the second character, and 0 otherwise. The variable `i` is `-1` after the loop completes, indicating the end of the last iteration through the string `s`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and a binary string `s`. For each test case, it calculates the number of positions in the string `s` where a character is followed by a smaller character, adding one to this count if no such pair exists. If there is at least one pair of consecutive characters where the first character is less than the second, a flag is set. After processing all test cases, it prints the calculated count for each case.

