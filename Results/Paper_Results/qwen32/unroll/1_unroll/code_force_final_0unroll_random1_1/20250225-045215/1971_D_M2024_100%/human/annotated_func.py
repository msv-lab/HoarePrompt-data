#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, s is a string consisting of characters '0' and '1' with length 1 <= |s| <= 500.
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
        
    #State: A series of printed values, each being either `cut1 + 1` or `cut0 + cut1` depending on the transitions in the respective input string `a` for each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` consisting of characters '0' and '1'. It then calculates and prints the number of transitions between '0' and '1' plus one if there are no '0' to '1' transitions.

