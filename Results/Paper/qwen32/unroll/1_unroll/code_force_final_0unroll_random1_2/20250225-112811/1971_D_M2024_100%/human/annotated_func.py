#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a string consisting of characters '0' and '1' with length 1 ≤ |s| ≤ 500.
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
        
    #State: The output state is determined by the last iteration's print statement, which is either `cut1 + 1` if `cut0` is 0, or `cut0 + cut1` otherwise.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` consisting of '0's and '1's. It then calculates and prints the number of transitions between '0' and '1' and between '1' and '0' in the string. If there are no '0' to '1' transitions, it adds 1 to the count of '1' to '0' transitions before printing the result.

