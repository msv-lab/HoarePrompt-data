#State of the program right berfore the function call: The function should take a single argument, a binary string `s` (1 ≤ |s| ≤ 500), where |s| denotes the length of the string `s`. The string `s` consists only of characters '0' and '1'.
def func():
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut0 = 0
        
        cut1 = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut1 += 1
            if a[i] == '0' and a[i + 1] == '1':
                cut0 += 1
        
        if cut0 == 0:
            print(cut1 + 1)
        else:
            print(cut0 + cut1)
        
    #State: The loop will execute `t` times, and for each iteration, it will read a binary string `a` from the input. It will then count the number of transitions from '1' to '0' (stored in `cut1`) and from '0' to '1' (stored in `cut0`) in the string `a`. If there are no transitions from '0' to '1' (`cut0 == 0`), it will print `cut1 + 1`. Otherwise, it will print `cut0 + cut1`. The values of `cut0` and `cut1` will be reset to 0 at the start of each iteration. The initial binary string `s` and the integer `t` will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads a binary string `a` from the input. It then counts the number of transitions from '1' to '0' (stored in `cut1`) and from '0' to '1' (stored in `cut0`) in the string `a`. If there are no transitions from '0' to '1' (`cut0 == 0`), it prints `cut1 + 1`. Otherwise, it prints `cut0 + cut1`. The function does not return any value, and it does not modify the initial binary string `s` or the integer `t`.

