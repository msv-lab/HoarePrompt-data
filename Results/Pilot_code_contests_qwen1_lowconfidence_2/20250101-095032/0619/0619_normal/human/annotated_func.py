#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, and the second line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i ≤ 2^{30}-1.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    s = []
    for i in a:
        ts = bin(i)[2:]
        
        ts = ts[::-1]
        
        while len(ts) < 32:
            ts += '0'
        
        s.append(ts)
        
    #State of the program after the  for loop has been executed: `a` is a list of `n` integers, where each integer is converted to a 32-bit binary string (reversed and padded with leading zeros if necessary), `s` is a list of the same 32-bit binary strings, each corresponding to the integers in `a`.
    ans = ''
    brk = -1
    leftp = 0
    ansl = -1
    ansr = -1
    for j in range(31, -1, -1):
        c1 = 0
        
        c0 = 0
        
        for i in range(n):
            if s[i][j] == '0':
                c0 += 1
            else:
                c1 += 1
        
        if c1 == n:
            ans += '1'
        elif c0 == n:
            ans += '0'
        else:
            mx0 = 0
            mx1 = 0
            ans += '1'
            leftp = int(ans, 2)
            leftp <<= j
            for i in range(n):
                if s[i][j] == '0':
                    mx0 = max(mx0, int(s[i][:j][::-1], 2))
                else:
                    mx1 = max(mx1, int(s[i][:j][::-1], 2))
            ansl = leftp + mx0
            ansr = leftp + mx1
            break
        
    #State of the program after the  for loop has been executed: `a` is a list of `n` integers, `s` is a list of `n` 32-bit binary strings, `ans` is a binary string, `brk` is -1, `leftp` is `2^32 - 1`, `ansl` is `2^32 - 1`, `ansr` is `2^32 - 1`, `j` is -1, `c0` is `n`, `c1` is `n`, and `i` is `n`.
    if (ansl == -1) :
        leftp = int(ans, 2)
        a1 = 0
        for i in a:
            a1 = max(a1, leftp ^ i)
            
        #State of the program after the  for loop has been executed: `a` is a list of `n` integers, `s` is a list of `n` 32-bit binary strings, `ans` is a binary string, `brk` is -1, `leftp` is the integer value of `ans`, `ansl` is -1, `ansr` is \(2^{32} - 1\), `j` is -1, `c0` is `n`, `c1` is `n`, `i` is the last element of `a`, and `a1` is the maximum value of `leftp ^ i` for each `i` in `a`.
        print(a1)
    else :
        m1 = 0
        m0 = 0
        for i in a:
            m1 = max(m1, ansr ^ i)
            
            m0 = max(m0, ansl ^ i)
            
        #State of the program after the  for loop has been executed: `a` is a list of `n` integers, `s` is a list of `n` 32-bit binary strings, `ans` is a binary string, `brk` is -1, `leftp` is \(2^{32} - 1\), `ansl` is the maximum of all `ansl ^ i` where `i` is an integer in `a`, `ansr` is the maximum of all `ansr ^ i` where `i` is an integer in `a`, `j` is -1, `c0` is `n`, `c1` is `n`, `i` is `n`, `m0` is the maximum of all `ansl ^ i` where `i` is an integer in `a`, `m1` is the maximum of all `ansr ^ i` where `i` is an integer in `a`.
        print(min(m1, m0))
    #State of the program after the if-else block has been executed: `a` is a list of `n` integers, `s` is a list of `n` 32-bit binary strings, `ans` is a binary string, `brk` is -1, `leftp` is either the integer value of `ans` (if `ansl` == -1) or \(2^{32} - 1\) (otherwise), `ansl` is either -1 (if `ansl` == -1) or the maximum of all `ansl ^ i` where `i` is an integer in `a` (otherwise), `ansr` is either \(2^{32} - 1\) (if `ansl` == -1) or the maximum of all `ansr ^ i` where `i` is an integer in `a` (otherwise), `j` is -1, `c0` is `n`, `c1` is `n`, `i` is `n`, and either `a1` is the maximum value of `leftp ^ i` for each `i` in `a` (if `ansl` == -1) or the minimum of `m1` and `m0` (where `m0` is the maximum of all `ansl ^ i` and `m1` is the maximum of all `ansr ^ i` for each `i` in `a`) is printed.
#Overall this is what the function does:The function takes an integer `n` and an array of `n` integers `a_1, a_2, ..., a_n`. It converts each integer in the array to a 32-bit binary string, reverses the binary string, and pads it with leading zeros if necessary. The function then iterates through the binary strings to construct a final binary string `ans`. If all bits in any position are the same, it sets the corresponding bit in `ans` accordingly. Otherwise, it determines the maximum value by flipping the bit in `ans` and considering the maximum XOR value with the original integers. Finally, it prints either the maximum XOR value when `ans` is all ones or the minimum of two possible maximum XOR values based on the constructed `ans`.

