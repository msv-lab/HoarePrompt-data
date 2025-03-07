#State of the program right berfore the function call: The function should take a single argument `s` which is a binary string (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'. The function should be called within a loop that processes `t` test cases, where `t` is a positive integer (1 ≤ t ≤ 500).
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: After the loop executes all the iterations, the variable `t` is decremented to 0, and the variable `s` will hold the value of the last input binary string. The variable `count` will be the number of times a '1' appears before a '0' in the last input binary string, plus 1.
#Overall this is what the function does:The function processes `t` test cases, where `t` is a positive integer (1 ≤ t ≤ 500). For each test case, it reads a binary string `s` (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'. It then counts the number of times a '1' appears immediately before a '0' in the string and prints this count plus one. After processing all test cases, the variable `t` is decremented to 0, and `s` holds the value of the last input binary string. The function does not return any value; it only prints the results.

