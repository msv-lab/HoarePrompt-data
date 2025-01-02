#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, a and b are integers such that 1 ≤ a, b ≤ n, and the second line is a string of length n consisting only of characters '0' and '1', where '0' indicates that the corresponding airport belongs to the first company and '1' indicates that it belongs to the second company.
def func():
    n, s, f = map(int, stdin.readline().split())
    numbers = list(map(int, list(stdin.readline().strip())))
    cnt = [(0) for i in range(n)]
    s -= 1
    f -= 1
    s, f = min(s, f), max(s, f)
    if (numbers[0] == numbers[s]) :
        cnt[0] = 1
    #State of the program after the if block has been executed: *`n` is a specific integer (previously 1 ≤ n ≤ 10^5), `s` is the smaller of the original `s` and `f`, `f` is the larger of the original `s` and `f`, `a` is a string of length `n` consisting only of characters '0' and '1', `numbers` is a list of `n` integers, each being either 0 or 1, `cnt` is a list of `n` elements, with the first element set to `1` and the rest set to `0`, `s` is `s - 1`. If the first element of `numbers` is equal to the element at index `s` in `numbers`, the first element of `cnt` is set to `1`. Otherwise, the first element of `cnt` remains `0`.
    for i in range(1, n):
        if numbers[i] == numbers[s]:
            cnt[i] = cnt[i - 1] + 1
        else:
            cnt[i] = cnt[i - 1]
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` must be greater than 0, `numbers[i]` is not applicable since `i` is `n`, `cnt[0]` is 0, `cnt[1]` is 0 or 1 depending on the first element of `numbers` and `numbers[s]`, and for all `j` from 2 to `n-1`, `cnt[j]` is the cumulative count of consecutive matches starting from `numbers[s]` up to `numbers[j]`.
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
            
        #State of the program after the loop has been executed: `i` is `n`, `n` must be greater than 0, `cnt[0]` is 0, `cnt[1]` is 0 or 1 depending on the first element of `numbers` and `numbers[s]`, for all `j` from 2 to `n-1`, `cnt[j]` is the cumulative count of consecutive matches starting from `numbers[s]` up to `numbers[j]`, `ans` is `f - s`, `l` is `-1` or `(n - 1) // 2`, `r` is `(n - 1) // 2` or `n`, `m` is `(n - 1) // 2`. After the loop terminates, `l` and `r` will be such that `l <= r` and no further divisions are possible, meaning the final value of `r` will be the greatest index `k` such that `cnt[k] > cnt[f]`, and `l` will be `r - 1`. If no such `k` exists, `l` will be `-1` and `r` will be `n`.
        l = -1
        r = n
        while r > l + 1:
            m = (r + l) // 2
            
            if cnt[m] >= cnt[f]:
                r = m
            else:
                l = m
            
        #State of the program after the loop has been executed: `i` is `n`, `n` must be greater than 3, `cnt[0]` is 0, `cnt[1]` is 0 or 1 depending on the first element of `numbers` and `numbers[s]`, for all `j` from 2 to `n-1`, `cnt[j]` is the cumulative count of consecutive matches starting from `numbers[s]` up to `numbers[j]`, `ans` is `m - s` or `f - s`, `l` is \((n - 1) // 2\), `r` is \((3n - 1) // 4\), `m` is \((5n - 3) // 8\). If `cnt[m] >= cnt[f]`, then `r = (5n - 3) // 8`. Otherwise, `r = (3n - 1) // 4`.
        if (r != n) :
            ans = min(ans, f - r)
        #State of the program after the if block has been executed: *`i` is `n`, `n` must be greater than 3, `cnt[0]` is 0, `cnt[1]` is 0 or 1 depending on the first element of `numbers` and `numbers[s]`, for all `j` from 2 to `n-1`, `cnt[j]` is the cumulative count of consecutive matches starting from `numbers[s]` up to `numbers[j]`, `ans` is `min(ans, f - r)` where `r = (5n - 3) // 8` if `cnt[m] >= cnt[f]` else `r = (3n - 1) // 4`, `l` is \((n - 1) // 2\), `m` is \((5n - 3) // 8\), `r` is \((5n - 3) // 8\) if `cnt[m] >= cnt[f]` else \((3n - 1) // 4\), the current value of `r` is not equal to `n`.
    else :
        ans = 0
    #State of the program after the if-else block has been executed: *`i` is `n`, `n` must be greater than 0, `numbers[i]` is not applicable since `i` is `n`, `cnt[0]` is 0, `cnt[1]` is 0 or 1 depending on the first element of `numbers` and `numbers[s]`, for all `j` from 2 to `n-1`, `cnt[j]` is the cumulative count of consecutive matches starting from `numbers[s]` up to `numbers[j]`, `ans` is the minimum value between `ans` (initially `f - s`) and `f - r` where `r = (5n - 3) // 8` if `cnt[m] >= cnt[f]` else `r = (3n - 1) // 4`, or 0 if the if condition is not met.
    stdout.write(str(ans))
#Overall this is what the function does:The function processes a string of length \( n \) consisting only of '0's and '1's, and two indices \( s \) and \( f \) (both \( 1 \leq s, f \leq n \)). It calculates the maximum number of consecutive matching characters starting from index \( s \) and ending at index \( f \). The function returns the minimum distance between the start and end of the longest sequence of matching characters found. If no such sequence exists, it returns 0. Edge cases include when \( s \) and \( f \) are the same or when the entire string is uniform.

