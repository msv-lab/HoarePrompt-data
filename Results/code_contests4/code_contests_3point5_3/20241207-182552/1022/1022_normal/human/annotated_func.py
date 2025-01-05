#State of the program right berfore the function call: **
def func():
    n = int(raw_input())
    a = [int(raw_input()) for _ in xrange(n)]
    mxlba = 0
    for i in xrange(n):
        mxlba = max(mxlba, len(bin(a[i])[2:]))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `a` is a list of integers, `mxlba` is the maximum length of binary representation of integers in list `a`
    cnt = [0] * (mxlba + 5)
    for i in xrange(n):
        bit = bin(a[i])[2:]
        
        lb = len(bit)
        
        for j in xrange(lb - 1, -1, -1):
            if bit[j] == '1':
                cnt[lb - 1 - j] += 1
                break
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `n` is greater than 0, `a` is a list of integers, `mxlba` is the maximum length of binary representation of integers in list `a`, `cnt` is a list of integers with a length of `mxlba + 5` where each element represents the count of '1's at a specific position in the binary representation of integers in list `a`.
    axor = 0
    for i in xrange(n):
        axor ^= a[i]
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `a` is a list of integers, `mxlba` is the maximum length of binary representation of integers in list `a`, `cnt` is a list of integers with a length of `mxlba + 5`, `axor` is the result of bitwise XOR operation between all elements in list `a`
    if (axor == 0) :
        print(0)
        exit()
    #State of the program after the if block has been executed: *`n` is greater than 0, `a` is a list of integers, `mxlba` is the maximum length of binary representation of integers in list `a`, `cnt` is a list of integers with a length of `mxlba + 5`, `axor` is the result of bitwise XOR operation between all elements in list `a`. If the bitwise XOR of all elements in list `a` is 0, then the overall state of the program remains unchanged.
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
        
    #State of the program after the loop has been executed: `n` is greater than 0, `a` is a list of integers, `mxlba` is the maximum length of binary representation of integers in list `a`, `cnt` is a list of integers with a length of `mxlba + 5`, `axor` is the binary representation of the result of XOR operation between all elements in list `a`, `la` is the length of `axor`, `ans` is the number of '1's in the binary representation of `axor` for which `cnt` was greater than 0, `i` is equal to `la` after the loop completes
    print(ans)
#Overall this is what the function does:The function reads an integer input, then reads a list of integers. It calculates the maximum length of the binary representation of integers in the list. It then iterates through the list to count the occurrences of '1' bits at different positions in the binary representations. After that, it performs a bitwise XOR operation on all elements in the list. If the result is 0, it prints 0 and exits. Otherwise, it calculates the number of '1' bits at different positions in the XOR result while ensuring that each position has non-zero count in the previous calculation. The function finally prints the total count of '1' bits in the XOR result. The function does not accept any parameters and outputs specific values based on the calculations.

