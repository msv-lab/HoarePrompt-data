#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100000, and a_i are integers such that 2 ≤ a_i ≤ 10^9 for each pile i from 1 to N.
def func():
    n = int(raw_input())
    a = [int(raw_input()) for _ in xrange(n)]
    mxlba = 0
    for i in xrange(n):
        mxlba = max(mxlba, len(bin(a[i])[2:]))
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100000, `n` is a non-negative integer, `mxlba` is the maximum length of the binary representation of the integers in `a` if `n` > 0, otherwise `mxlba` is 0.
    cnt = [0] * (mxlba + 5)
    for i in xrange(n):
        bit = bin(a[i])[2:]
        
        lb = len(bit)
        
        for j in xrange(lb - 1, -1, -1):
            if bit[j] == '1':
                cnt[lb - 1 - j] += 1
                break
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100000, `n` is the total number of integers processed, `mxlba` is either 0 or a positive integer, `cnt` is a list of size `mxlba + 5` containing the counts of '1's at each bit position across all binary representations of the integers in `a`, and if `n` is 0, `cnt` remains all 0s.
    axor = 0
    for i in xrange(n):
        axor ^= a[i]
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100000, `n` is the total number of integers processed, `i` is `n - 1`, and `axor` is the bitwise XOR of all integers in the array `a` from index 0 to `n - 1`.
    if (axor == 0) :
        print(0)
        exit()
    #State of the program after the if block has been executed: *`N` is a positive integer such that 1 ≤ `N` ≤ 100000, `n` is the total number of integers processed, `i` is `n - 1`, and `axor` is the bitwise XOR of all integers in the array `a` from index 0 to `n - 1`. If `axor` equals 0, the output is 0.
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
        
    #State of the program after the loop has been executed: `i` is equal to `la`, `ans` is the count of '1's in `axor` that had corresponding non-zero values in `cnt`, `cnt` has been decremented as necessary, and `axor` has been potentially modified based on the bitwise XOR operations throughout the loop.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer N (1 ≤ N ≤ 100000) and a list of integers a_i (2 ≤ a_i ≤ 10^9 for each pile i from 1 to N). It calculates the maximum length of the binary representations of the integers in the list, counts the occurrences of '1's at each bit position across these representations, and computes the bitwise XOR of all integers. If the XOR result is 0, it outputs 0. If not, it determines the number of significant '1's in the XOR result that can be matched with available counts from the bit positions, returning this count. If any significant '1' in the XOR result cannot be matched, it outputs -1. The function does not handle cases where N is 0, which should ideally not occur given the constraints.

