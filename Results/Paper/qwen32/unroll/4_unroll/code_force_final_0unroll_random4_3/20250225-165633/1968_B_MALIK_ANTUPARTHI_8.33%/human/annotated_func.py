#State of the program right berfore the function call: The function takes no arguments but operates on input provided as described. The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there are three lines: two integers n and m (1 ≤ n, m ≤ 2 · 10^5) representing the lengths of binary strings a and b, respectively, followed by the binary strings a and b themselves. The sum of all n and m across all test cases does not exceed 2 · 10^5.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e.index(d[j]) + 1
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: The output state consists of `a` printed values of `k`, each representing the number of characters from the start of string `d` that can be matched in order within string `e` for each test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two binary strings, and for each test case, it outputs the number of characters from the start of the first string that can be matched in order within the second string.

