#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each of the following t lines contains a single binary string s (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: For each binary string `s`, the output is the count of segments where a '1' is followed by a '0', plus one. The variable `t` remains unchanged, and each binary string `s` is processed individually to produce a corresponding output value.
#Overall this is what the function does:The function processes a series of binary strings, each representing a test case, and outputs the count of segments where a '1' is immediately followed by a '0', plus one for each string.

