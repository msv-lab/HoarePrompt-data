#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each of the following t lines contains a single binary string s (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'.
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        count = 1
        
        flag = False
        
        j = 0
        
        while j < len(s) - 1:
            if s[j] != s[j + 1]:
                count += 1
                if s[j] == '0' and s[j + 1] == '1':
                    flag = True
                    j += 1
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: The printed count values for each of the `t` test cases.
#Overall this is what the function does:The function processes `t` binary strings, each consisting of characters '0' and '1', and prints the count of segments of consecutive identical characters minus one if there is at least one transition from '0' to '1'.

