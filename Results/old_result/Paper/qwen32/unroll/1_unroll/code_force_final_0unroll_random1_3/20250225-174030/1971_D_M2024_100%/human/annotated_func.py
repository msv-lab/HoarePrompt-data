#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each of the t test cases, there is a binary string s such that 1 ≤ |s| ≤ 500, where s consists only of the characters '0' and '1'.
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
        
    #State: `t` is the same as the initial value, `a`, `cut0`, and `cut1` are reset to their initial state at the start of each iteration, and the output consists of the printed results for each test case.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a binary string `s`. For each binary string, it calculates and prints the number of segments required to split the string into contiguous blocks of identical characters, adding one to the count if there are no transitions from '1' to '0'.

