#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. The string s consists of only the first k lowercase English alphabets and has a length of m. It is guaranteed that the sum of m and the sum of n over all test cases does not exceed 10^6.
def func_1():
    n, k, m = tuple(map(int, input().split()))
    s = input()
    us = set(chr(i + 97) for i in range(k))
    win = set()
    ans = []
    ps = 0
    for i in s:
        if i in us:
            win.add(i)
            if len(win) == k:
                ans.append(i)
                ps += 1
                win.clear()
        
    #State: All characters in the string `s` have been processed.
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES'
    #State: All characters in the string `s` have been processed, and the value of `ps` is less than `n`
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: All characters in the string `s` have been processed, and the value of `ps` is equal to `n`.
#Overall this is what the function does:The function processes a string `s` consisting of the first `k` lowercase English alphabets of length `m`. For each test case defined by integers `n` and `k`, it checks if the string `s` contains at least `n` unique characters from the first `k` lowercase English alphabets. If the condition is met, it prints 'YES'; otherwise, it prints 'NO' and appends any missing characters from the first `k` lowercase English alphabets to the result string `ans`, followed by 'a' repeated `n - len(ans) - 1` times.

