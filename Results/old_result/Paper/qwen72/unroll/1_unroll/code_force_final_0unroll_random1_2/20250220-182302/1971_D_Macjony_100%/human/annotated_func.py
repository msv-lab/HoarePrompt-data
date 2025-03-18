#State of the program right berfore the function call: The function should take a single argument, a string s, where s is a binary string (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'. The function is expected to handle multiple test cases, where the number of test cases t is an integer (1 ≤ t ≤ 500).
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
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: The loop will execute `t` times, each time processing a binary string `s`. For each string `s`, the loop will print the number of alternating character sequences in `s`, adjusted by subtracting 1 if the sequence contains a '0' followed by a '1'. The variables `i`, `s`, `count`, `flag`, and `j` will be reset or modified within each iteration, but the value of `t` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads a binary string `s` from the input. It then calculates and prints the number of alternating character sequences in `s`, adjusting the count by subtracting 1 if the sequence contains a '0' followed by a '1'. The function does not return any value; it only prints the results for each test case. After the function concludes, the input has been processed for `t` test cases, and the final state of the program includes the printed counts for each test case.

