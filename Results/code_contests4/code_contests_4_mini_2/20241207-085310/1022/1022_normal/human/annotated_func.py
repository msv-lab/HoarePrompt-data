#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100000, and a_i (for each pile i) is an integer such that 2 ≤ a_i ≤ 10^9.
def func():
    n = int(raw_input())
    a = [int(raw_input()) for _ in xrange(n)]
    mxlba = 0
    for i in xrange(n):
        mxlba = max(mxlba, len(bin(a[i])[2:]))
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100000, `n` is a non-negative integer, `i` is equal to `n`, `mxlba` is the maximum length of the binary representation of all integers in `a`, or 0 if `n` is 0.
    cnt = [0] * (mxlba + 5)
    for i in xrange(n):
        bit = bin(a[i])[2:]
        
        lb = len(bit)
        
        for j in xrange(lb - 1, -1, -1):
            if bit[j] == '1':
                cnt[lb - 1 - j] += 1
                break
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100000, `n` is greater than 0, `i` is equal to `n`, `a` has at least `n` elements, `cnt` contains the counts of the most significant '1' bits for the binary representations of all elements in `a[0]` to `a[n-1]`, with each index in `cnt` representing the count of the most significant '1' bit position across all processed elements; if an element has no '1' bit, the corresponding index in `cnt` remains unchanged.
    axor = 0
    for i in xrange(n):
        axor ^= a[i]
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100000, `n` is greater than 0, `i` is equal to `n`, `a` has at least `n` elements, `cnt` contains the counts of the most significant '1' bits, `axor` is the result of the XOR operation on all elements of `a` from `a[0]` to `a[n-1]`.
    if (axor == 0) :
        print(0)
        exit()
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 100000, `n` is greater than 0, `i` is equal to `n`, `a` has at least `n` elements, `cnt` contains the counts of the most significant '1' bits, and `axor` is the result of the XOR operation on all elements of `a` from `a[0]` to `a[n-1]`. If `axor` is equal to 0, the program has exited.
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
        
    #State of the program after the loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100000, `n` is greater than 0, `i` is equal to `la`, `a` has at least `n` elements, `cnt` may have non-negative counts for each index, `la` is the length of `axor`, and `ans` is the total number of '1's processed from `axor`. If any `cnt[i]` was 0 during the iterations for the corresponding '1's in `axor`, the program would have exited with output value -1 before reaching this state. If all conditions were met, `axor` would have been fully processed.
    print(ans)
#Overall this is what the function does:The function accepts no parameters and reads a positive integer N followed by N integers from input. It computes the maximum length of the binary representation of these integers, counts the occurrences of the most significant '1' bits, and performs an XOR operation on all integers. If the result of the XOR operation is zero, it returns 0. If the XOR result is non-zero, it processes each bit of the XOR result, checking against the counts of '1's. If a required count is zero, it returns -1. Otherwise, it returns the total number of '1's processed from the XOR result. The function can exit early based on certain conditions, such as returning -1 or 0, which may not be explicitly stated in the annotations.

