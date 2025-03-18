#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string such that 1 ≤ |s| ≤ 500.
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
        
    #State: Output State: The value printed is either `cut1 + 1` when `cut0` is 0, or `cut0 + cut1` otherwise, where `cut0` and `cut1` are counts of adjacent "01" and "10" pairs in the binary string `a`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and a binary string `s`. For each test case, it counts the number of "01" and "10" pairs in the binary string `s`. If no "01" pairs are found, it prints the count of "10" pairs plus one. Otherwise, it prints the sum of the counts of "01" and "10" pairs. The function does not return any value but prints the result for each test case.

