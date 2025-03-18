#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a string of length between 1 and 500 consisting only of the characters '0' and '1'.
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
        
    #State: `t` is an integer such that 0 ≤ `t` ≤ 499, `s` is a string of length between 1 and 500 consisting only of the characters '0' and '1', `a` is a string of length between 1 and 500 consisting only of the characters '0' and '1', `cut0` is the number of '01' transitions in `a`, and `cut1` is the number of '10' transitions in `a`. If `cut0` equals 0, then the output is `cut1 + 1`; otherwise, the output is `cut0 + cut1`. This process is repeated `t` times, with `t` starting from the initial value and decremented by 1 after each iteration.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a binary string `s`. For each string, it calculates and prints the number of transitions between '0' and '1' plus one if there are no '01' transitions.

