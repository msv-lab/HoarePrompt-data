#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with a length between 1 and 500, inclusive.
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
        
    #State: Output State: The value of `t` is reduced to 0, and for each input string `s` provided in the range of original `t`, the output is either `count + 1` if no two consecutive characters are equal and `flag` remains 0, or `count` if there exists at least one pair of consecutive characters where the second character is greater than the first, with `flag` set to 1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and a binary string `s`. For each test case, it counts the number of positions where consecutive characters in the string `s` are different. If no two consecutive characters are equal, it prints the count plus one; otherwise, it prints the count. After processing all test cases, it outputs the results.

