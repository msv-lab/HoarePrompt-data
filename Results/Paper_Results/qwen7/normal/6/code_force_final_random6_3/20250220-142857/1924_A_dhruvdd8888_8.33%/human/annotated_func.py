#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5, n and k are integers such that 1 ≤ n, k ≤ 26, m is an integer such that 1 ≤ m ≤ 1000, and s is a string of length m comprising only the first k lowercase English alphabets.
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
        
    #State: `win` is a set of the first `k` lowercase English alphabets, `us` is a set of the first `k` lowercase English alphabets, `ans` is a list containing exactly `m` elements, each being one of the first `k` lowercase English alphabets, `ps` is `m`, `i` is the last element in `s`, and `s` is the same set.
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES'
    #State: `win` is a set of the first `k` lowercase English alphabets, `us` is a set of the first `k` lowercase English alphabets, `ans` is a list containing exactly `m` elements, each being one of the first `k` lowercase English alphabets, `ps` is `m`, `i` is the last element in `s`, and `s` is the same set, with `ps` being less than `n`
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: Output State: `win` is a set of the first `k` lowercase English alphabets, `us` is a set of the first `k` lowercase English alphabets, `ans` is a list containing exactly `m` elements, each being one of the first `k` lowercase English alphabets, `ps` is `m`, `i` is the last element in `us` but not in `win`, and `s` is the same set as `us`. If any element in `us` is not in `win`, it gets appended to `ans` followed by `a` repeated `n - len(ans) - 1` times.
    #
    #In simpler terms, after all iterations of the loop, the variable `win` will still contain the first `k` lowercase English alphabets. The variable `us` will also remain the same, containing the first `k` lowercase English alphabets. The list `ans` will have exactly `m` elements, each being one of the first `k` lowercase English alphabets. The variable `ps` will still be equal to `m`. The variable `i` will be the last element in `us` that is not in `win`. The set `s` will remain unchanged, being the same as `us`. The loop will continue appending elements from `us` to `ans` until all elements in `us` that are not in `win` have been processed, with each appended element followed by `a` repeated `n - len(ans) - 1` times.
#Overall this is what the function does:The function accepts four parameters: n and k (both integers between 1 and 26), m (an integer between 1 and 1000), and s (a string of length m comprising only the first k lowercase English alphabets). It does not return any value but checks if the string s contains at least n distinct characters from the first k lowercase English alphabets. If it does, the function prints 'YES'. Otherwise, it prints 'NO' and appends missing characters to the end of the string s, each followed by 'a' repeated `n - len(ans) - 1` times.

