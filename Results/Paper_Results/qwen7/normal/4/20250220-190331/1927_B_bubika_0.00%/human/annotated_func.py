#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: Output State: After the loop executes all the iterations, `b` will be a list where each element's count reflects the total number of times that corresponding integer (from 0 to 25) appeared across all inputs `s` provided by the loop. The variable `r` will be a string constructed by repeating characters from `a` based on the cumulative counts of the integers in `s`. Each character in `a` will be repeated according to how many times its corresponding integer in `b` was incremented throughout the entire loop execution.
    #
    #In simpler terms, `b` will show the total frequency of each integer from `s` across all iterations, and `r` will be a string where each character from `a` is repeated according to the total count of its corresponding integer in `b`.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer `t` indicating the number of subsequent test cases. For each test case, it reads a positive integer `n` and a list `s` of `n` non-negative integers. It then constructs a string `r` by mapping each integer in `s` to a character in the alphabet `a` (where `a` contains the first 26 lowercase letters of the English alphabet) and repeats each character according to the frequency of its corresponding integer in `s`. The function updates a count array `b` to keep track of the total occurrences of each integer across all test cases. Finally, it prints the constructed string `r` for each test case.

