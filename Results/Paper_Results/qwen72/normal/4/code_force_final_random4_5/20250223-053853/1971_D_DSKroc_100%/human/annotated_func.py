#State of the program right berfore the function call: The function should take a binary string `s` as input, where `s` consists only of characters '0' and '1', and its length is between 1 and 500 inclusive.
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
        
    #State: The loop will print the number of transitions between '0' and '1' in each input string `s` during each iteration. If the string `s` is non-increasing (i.e., it does not have any '0' followed by '1'), it will print the number of transitions plus one. The final state of the variables `s` and `count` will be the last input string and the count of transitions in that string, respectively. The variable `flag` will be 1 if the last string had at least one '0' followed by '1', otherwise it will be 0.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, then for each test case, it reads a binary string `s` and prints the number of transitions between '0' and '1' in the string. If the string is non-increasing (i.e., it does not have any '0' followed by '1'), it prints the number of transitions plus one. The function does not return any value. After the function concludes, the final state of the program is that `t` test cases have been processed, and the number of transitions (or transitions plus one if non-increasing) has been printed for each input string. The variables `s`, `count`, and `flag` will reflect the state of the last processed test case.

