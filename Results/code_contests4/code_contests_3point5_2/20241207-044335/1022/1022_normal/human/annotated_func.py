#State of the program right berfore the function call: **
def func():
    n = int(raw_input())
    a = [int(raw_input()) for _ in xrange(n)]
    mxlba = 0
    for i in xrange(n):
        mxlba = max(mxlba, len(bin(a[i])[2:]))
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `a` is a list of `n` integers, `mxlba` is the maximum length of the binary representation of any integer in list `a`
    cnt = [0] * (mxlba + 5)
    for i in xrange(n):
        bit = bin(a[i])[2:]
        
        lb = len(bit)
        
        for j in xrange(lb - 1, -1, -1):
            if bit[j] == '1':
                cnt[lb - 1 - j] += 1
                break
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `n` is greater than 0, `a` is a list of `n` integers, `mxlba` is the maximum length of the binary representation of any integer in list `a`, `cnt` is a list with values representing the count of '1's at each position from right to left in the binary representations of all integers in list `a` based on the respective positions in the binary representations. The loop has iterated through all elements in list `a` and updated `cnt` accordingly.
    axor = 0
    for i in xrange(n):
        axor ^= a[i]
        
    #State of the program after the  for loop has been executed: Output State: After the loop, `n` is greater than 0, `a` is a list of `n` integers, `mxlba` is the maximum length of the binary representation of any integer in list `a`, `cnt` is a list with values representing the count of '1's at each position from right to left in the binary representations of all integers in list `a` based on the respective positions in the binary representations, and `axor` is the result of bitwise XOR operation on all elements of list `a`.
    if (axor == 0) :
        print(0)
        exit()
    #State of the program after the if block has been executed: *After the if statement, all variables retain their initial values: `n` is greater than 0, `a` is a list of `n` integers, `mxlba` is the maximum length of the binary representation of any integer in list `a`, `cnt` is a list with values representing the count of '1's at each position from right to left in the binary representations of all integers in list `a`, `axor` is the result of bitwise XOR operation on all elements of list `a`, and `axor` is still equal to 0.
    axor = bin(axor)[2:]
    la = len(axor)
    ans = 0
    i = -1
    while i < la:
        i += 1
        
        if axor[i] == '1':
            if cnt[i] == 0:
                print(-1)
                exit()
            else:
                ans += 1
                cnt[i] -= 1
                if la - i - 1 == 0:
                    break
                tmp = int('1' * (la - i - 1), 2)
                axor = int(axor, 2) ^ tmp
                axor = bin(axor)[2:]
        
    #State of the program after the loop has been executed: `axor` is a binary string, `la` is 1, `ans` is the total number of times `axor` had a '1' at the corresponding index in the loop, `i` is equal to `la`
    print(ans)
#Overall this is what the function does:The function reads an integer input `n` and a list of `n` integers. It calculates the maximum length of the binary representation of the integers, counts the occurrences of '1's at each position in the binary representation, performs a bitwise XOR operation on all elements, and then manipulates the XOR result based on certain conditions. Finally, it prints the total count of manipulations performed. The function does not accept any parameters and does not have a specific return value.

