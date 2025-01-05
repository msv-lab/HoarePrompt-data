#State of the program right berfore the function call: **
def func():
    n = int(raw_input())
    a = [int(raw_input()) for _ in xrange(n)]
    mxlba = 0
    for i in xrange(n):
        mxlba = max(mxlba, len(bin(a[i])[2:]))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `a` is a list of integers inputted, `mxlba` is the maximum length of binary representations in the list `a`
    cnt = [0] * (mxlba + 5)
    for i in xrange(n):
        bit = bin(a[i])[2:]
        
        lb = len(bit)
        
        for j in xrange(lb - 1, -1, -1):
            if bit[j] == '1':
                cnt[lb - 1 - j] += 1
                break
        
    #State of the program after the  for loop has been executed: At the end of the loop, `i` is equal to `n-1`, `a` is a list of integers, `mxlba` is the maximum length of binary representations in list `a`, `cnt` is a list of integers representing the count of '1's in the corresponding positions of binary representations of integers in list `a` with updated values at specific indices, `bit` is the binary representation of the last integer in list `a`, `lb` is the length of the binary representation of the last integer in list `a`.
    axor = 0
    for i in xrange(n):
        axor ^= a[i]
        
    #State of the program after the  for loop has been executed: Output State: At the end of the loop, `i` is equal to `n`, `a` is a non-empty list of integers, `mxlba` is the maximum length of binary representations in list `a`, `cnt` has updated values at specific indices, `bit` is the binary representation of the last integer in list `a`, `lb` is the length of the binary representation of the last integer in list `a`, and `axor` is the result of XOR operation with all elements of list `a`.
    if (axor == 0) :
        print(0)
        exit()
    #State of the program after the if block has been executed: *At the end of the loop, `i` is equal to `n`, `a` is a non-empty list of integers, `mxlba` is the maximum length of binary representations in list `a`, `cnt` has updated values at specific indices, `bit` is the binary representation of the last integer in list `a`, `lb` is the length of the binary representation of the last integer in list `a`, `axor` is the result of XOR operation with all elements of list `a`, and `axor` is equal to 0. The program exits.
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
        
    #State of the program after the loop has been executed: At the end of the loop, `i` is equal to `la`, `a` is a non-empty list of integers, `mxlba` is the maximum length of binary representations in list `a`, `cnt` has updated values at specific indices, `bit` is the binary representation of the last integer in list `a`, `lb` is the length of the binary representation of the last integer in list `a`, `axor` is the result of XOR operation with all elements of list `a`, `axor` is equal to 0, `axor` is the binary representation of `axor` without the '0b' prefix, `la` is the length of the binary representation of `axor`, `ans` is the number of times `axor[i]` was equal to '1' and `cnt[i]` was not equal to 0, `axor[i]` equals '1' for all indices `i`, and `cnt[i]` is either 0 or not equal to 0. If `cnt[i] == 0`, then `axor` remains unchanged. If `cnt[i]` is not equal to 0, then `axor` is updated with `tmp` assigned the integer value of a string of '1's of length (la - i - 1).
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from input, creates a list `a` of `n` integers, calculates the maximum length of binary representations in the list `a`, performs various operations on the binary representations of integers, and prints the result. It does not accept any parameters and does not return any value.

