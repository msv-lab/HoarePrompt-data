#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n ≤ 10^5, 1 ≤ a, b ≤ n; the string s has a length of n and consists only of characters '0' and '1'.
def func():
    n, s, f = map(int, stdin.readline().split())
    numbers = list(map(int, list(stdin.readline().strip())))
    cnt = [(0) for i in range(n)]
    s -= 1
    f -= 1
    s, f = min(s, f), max(s, f)
    if (numbers[0] == numbers[s]) :
        cnt[0] = 1
    #State of the program after the if block has been executed: *`n` is an input integer, `s` is an input integer -1, `f` is an input string of length `n` consisting only of characters '0' and '1', `a` and `b` are integers such that 1 ≤ a, b ≤ n, `numbers` is a list of integers where each integer is the corresponding character from `f` converted to an integer, `cnt` is a list of length `n` where each element is 0. If the first element of `numbers` is equal to the element at index `s` of `numbers`, then `cnt[0]` is 1.
    for i in range(1, n):
        if numbers[i] == numbers[s]:
            cnt[i] = cnt[i - 1] + 1
        else:
            cnt[i] = cnt[i - 1]
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `s` is an input integer -1, `f` is an input string of length `n` consisting only of characters '0' and '1', `a` and `b` are integers such that 1 ≤ a, b ≤ n, `numbers` is a list of integers where each integer is the corresponding character from `f` converted to an integer, `cnt` is a list of length `n` where each element represents the cumulative count of elements in `numbers` from index 0 to the current index `i` that are equal to `numbers[s]`. If the loop does not execute (i.e., `n` is 1), `cnt` remains `[1]` if `numbers[0]` equals `numbers[s]`, otherwise `cnt` remains `[0]`. For `n > 1`, the final state of `cnt` is such that each element `cnt[i]` (for 1 ≤ i < n) is the cumulative count of elements from `numbers[0]` to `numbers[i]` that are equal to `numbers[s]`.
    ans = f - s
    if (numbers[s] != numbers[f]) :
        l = -1
        r = n
        while r > l + 1:
            m = (r + l) // 2
            
            if cnt[m] > cnt[f]:
                r = m
            else:
                l = m
            
        #State of the program after the loop has been executed: `n` is an input integer greater than 0, `s` is -1, `f` is an input string of length `n` consisting only of characters '0' and '1', `a` and `b` are integers such that 1 ≤ a, b ≤ n, `numbers` is a list of integers where each integer is the corresponding character from `f` converted to an integer, `cnt` is a list of length `n` where each element represents the cumulative count of elements in `numbers` from index 0 to the current index `i` that are equal to `numbers[s]`, the current value of `numbers[s]` is different from `numbers[f]`, `l` is the largest index such that `cnt[l] <= cnt[f]`, `r` is the smallest index such that `cnt[r] > cnt[f]` and `r` is `l + 1`.
        l = -1
        r = n
        while r > l + 1:
            m = (r + l) // 2
            
            if cnt[m] >= cnt[f]:
                r = m
            else:
                l = m
            
        #State of the program after the loop has been executed: `n` is an input integer greater than 0, `s` is -1, `f` is an input string of length `n` consisting only of characters '0' and '1', `a` and `b` are integers such that 1 ≤ a, b ≤ n, `numbers` is a list of integers where each integer is the corresponding character from `f` converted to an integer, `cnt` is a list of length `n` where each element represents the cumulative count of elements in `numbers` from index 0 to the current index `i` that are equal to `numbers[s]`, the current value of `numbers[s]` is different from `numbers[f]`, `r` is `l + 1`, and `m` is the last computed value of `(r + l) // 2` before the loop terminates.
        if (r != n) :
            ans = min(ans, f - r)
        #State of the program after the if block has been executed: *`n` is an input integer greater than 0, `s` is -1, `f` is an input string of length `n` consisting only of characters '0' and '1', `a` and `b` are integers such that 1 ≤ a, b ≤ n, `numbers` is a list of integers where each integer is the corresponding character from `f` converted to an integer, `cnt` is a list of length `n` where each element represents the cumulative count of elements in `numbers` from index 0 to the current index `i` that are equal to `numbers[s]`, the current value of `numbers[s]` is different from `numbers[f]`, `r` is `l + 1`, `m` is the last computed value of `(r + l) // 2` before the loop terminates. If `r` is not equal to `n`, `ans` is updated to the minimum of its previous value and `f - r`.
    else :
        ans = 0
    #State of the program after the if-else block has been executed: *`n` is an input integer greater than 0, `s` is -1, `f` is an input string of length `n` consisting only of characters '0' and '1', `a` and `b` are integers such that 1 ≤ a, b ≤ n, `numbers` is a list of integers where each integer is the corresponding character from `f` converted to an integer, `cnt` is a list of length `n` where each element represents the cumulative count of elements in `numbers` from index 0 to the current index `i` that are equal to `numbers[s]`. If `numbers[s]` is different from `numbers[f]`, `r` is `l + 1`, `m` is the last computed value of `(r + l) // 2` before the loop terminates, and if `r` is not equal to `n`, `ans` is updated to the minimum of its previous value and `f - r`. If `numbers[s]` is equal to `numbers[f]`, `ans` is 0.
    stdout.write(str(ans))
#Overall this is what the function does:The function reads two lines from standard input. The first line contains three integers: `n`, `s`, and `f`. The second line contains a string `s` of length `n` consisting of characters '0' and '1'. The function processes the string `s` to determine the minimum number of steps required to move from position `s` to position `f` under certain conditions. Specifically, it calculates a cumulative count of positions in the string `s` that match the character at position `s` up to each index. If the characters at positions `s` and `f` are different, it uses binary search to find the minimum distance to a position where the cumulative count exceeds the count at position `f`. If the characters at positions `s` and `f` are the same, the result is 0. The function writes the result to standard output. Edge cases include when `n` is 1, in which case the result is 0 if the characters at `s` and `f` are the same, or the distance between `s` and `f` otherwise.

