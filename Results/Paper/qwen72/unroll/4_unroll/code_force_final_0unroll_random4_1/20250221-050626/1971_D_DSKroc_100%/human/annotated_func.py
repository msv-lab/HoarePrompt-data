#State of the program right berfore the function call: The function should take a single argument, `s`, which is a binary string (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'. The function will be called multiple times with different test cases, where the number of test cases, `t`, is an integer (1 ≤ t ≤ 500).
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
        
    #State: `t` is an input integer (1 ≤ t ≤ 500), `s` is the last binary string input (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'. The loop has executed `t` times, and for each input string `s`, it has printed the number of adjacent character changes, with an additional 1 added if there are no increases in value between adjacent characters.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, then for each of the `t` binary strings `s` provided as input, it calculates and prints the number of adjacent character changes in the string. If there are no increases in value between adjacent characters in the string, it prints the count of changes plus one. After processing all `t` test cases, the function concludes.

