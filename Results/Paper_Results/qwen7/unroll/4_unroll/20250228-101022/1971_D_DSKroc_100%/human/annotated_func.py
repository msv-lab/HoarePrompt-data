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
        
    #State: Output State: t is a positive integer between 1 and 500, s is a binary string with a length between 1 and 500, and after executing the loop, for each input string s, if no two consecutive characters are different (i.e., s is either "000...0" or "111...1"), the output is the length of s plus one; otherwise, the output is the number of positions where consecutive characters differ.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer t and a binary string s. It counts the number of positions where consecutive characters in s differ. If no two consecutive characters are different, it adds one to this count. The function then prints the result for each test case.

