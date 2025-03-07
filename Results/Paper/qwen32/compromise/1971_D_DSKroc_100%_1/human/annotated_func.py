#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 500) representing the number of test cases. For each test case, it receives a string s (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'.
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
        
    #State: `t` is an integer between 1 and 500 inclusive, `q` has reached the value of `t`, and for each of the `t` iterations, the program has processed a string `s` by calculating `count` (the number of positions where two consecutive characters in `s` are different) and `flag` (indicating whether there is at least one position where a character is less than the next character). The program has printed `count + 1` if `flag` is 0, otherwise it has printed `count`.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it receives a string `s` consisting of characters '0' and '1'. It calculates and prints the number of positions where two consecutive characters in `s` are different, adding 1 to this count if there is no position where a '0' is followed by a '1'.

