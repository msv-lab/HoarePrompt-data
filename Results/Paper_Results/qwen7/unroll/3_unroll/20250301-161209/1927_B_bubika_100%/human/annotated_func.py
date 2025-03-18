#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n.
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
        
    #State: Output State: `t` is set to 0, `n` is any positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and `a` is reassigned to the string 'abcdefghijklmnopqrstuvwxyz'. The loop processes `t` inputs, but since `t` is set to 0 inside the loop, no iterations occur. Therefore, `r` remains an empty string.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads a positive integer \( n \) and a list of \( n \) non-negative integers. It then maps each integer in the list to a corresponding character in the alphabet 'abcdefghijklmnopqrstuvwxyz' and constructs a string based on these characters. Finally, it prints the constructed string for each test case.

