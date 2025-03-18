#State of the program right berfore the function call: The function should take three parameters: n, k, and s. n is an integer such that 1 <= n <= 26, k is an integer such that 1 <= k <= 26, and s is a string of length m (1 <= m <= 1000) comprising only the first k lowercase English alphabets.
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
        
    #State: Output State: `n` remains unchanged, `k` remains unchanged, `m` remains unchanged, `s` remains unchanged, `us` remains unchanged, `win` is an empty set, `ans` contains the characters that were the `k`-th unique characters from `us` found in `s` in the order they appeared, `ps` is the number of times a `k`-th unique character from `us` was found in `s`.
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES' and returns None.
    #State: `n` remains unchanged, `k` remains unchanged, `m` remains unchanged, `s` remains unchanged, `us` remains unchanged, `win` is an empty set, `ans` contains the characters that were the `k`-th unique characters from `us` found in `s` in the order they appeared, `ps` is the number of times a `k`-th unique character from `us` was found in `s`, and `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: Output State: `n` remains unchanged, `k` remains unchanged, `m` remains unchanged, `s` remains unchanged, `us` remains unchanged, `win` is an empty set, `ans` contains the characters that were the `k`-th unique characters from `us` found in `s` in the order they appeared, `ps` is the number of times a `k`-th unique character from `us` was found in `s`, and `ps` is less than `n`. The loop will print a string that consists of the characters in `ans` concatenated with the first unique character from `us` that is not in `win` and then padded with `a` characters to reach a total length of `n`.
#Overall this is what the function does:The function `func_1` takes no parameters and reads `n`, `k`, and `s` from user input. It processes the string `s` to find the `k`-th unique characters from the first `k` lowercase English alphabets. If the function finds at least `n` such `k`-th unique characters, it prints 'YES' and returns `None`. If fewer than `n` such characters are found, it prints 'NO' followed by a string that consists of the characters found in `ans`, the first unique character from `us` that is not in `win`, and then padded with `a` characters to reach a total length of `n`. The function does not modify the input variables `n`, `k`, `m`, or `s`.

