#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 500) representing the number of test cases. For each test case, there is a single binary string s (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'.
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
        
    #State: For each test case, the number of transitions between '0' and '1' (or '1' and '0') plus one if no '0' to '1' transitions are present, otherwise just the number of transitions.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it accepts a binary string `s`. It then calculates and prints the number of transitions between '0' and '1' (or '1' and '0') in the string, plus one if there are no '0' to '1' transitions.

