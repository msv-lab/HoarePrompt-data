#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers such that 0 ≤ a_i < n.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: The loop has completed all iterations. The variable `t` is 1 if the user input was greater than 1, otherwise it remains unspecified. The variable `n` is the original input integer. The list `s` is empty since all its elements have been processed. The list `b` is a list of 26 zeros, with each index incremented by the count of its occurrence in `s` across all iterations. The variable `r` is a string that consists of characters from the list `a` (which is 'abcdefghijklmnopqrstuvwxyz') corresponding to the counts of each integer in `s`. The variables `i` and `x` are not specified as they are local to the loop and do not persist outside of it.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads a positive integer `n` and a list of `n` non-negative integers `a`. It then creates a string `r` consisting of 26 lowercase English letters ('a' to 'z'), where each letter's position corresponds to the count of its index value in the list `a`. After processing all test cases, it prints the resulting strings `r` for each case.

