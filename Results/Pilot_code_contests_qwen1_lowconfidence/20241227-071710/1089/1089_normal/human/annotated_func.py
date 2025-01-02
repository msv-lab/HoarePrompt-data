#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, a and b are integers such that 1 ≤ a, b ≤ n, and the second line is a string of length n consisting only of characters '0' and '1'.
def func():
    n, s, f = map(int, stdin.readline().split())
    numbers = list(map(int, list(stdin.readline().strip())))
    cnt = [(0) for i in range(n)]
    s -= 1
    f -= 1
    s, f = min(s, f), max(s, f)
    if (numbers[0] == numbers[s]) :
        cnt[0] = 1
    #State of the program after the if block has been executed: *`n` is an integer, `s` is the minimum of `original_s - 1` and `original_f - 1`, `f` is the maximum of `original_s - 1` and `original_f - 1`, `a` and `b` remain in their initial states, `cnt` is a list of length `n` with all elements equal to 0 except for the first element which is 1. If the first element of `numbers` is equal to the element at index `s` of `numbers`, then the first element of `cnt` is set to 1. There is no else part specified in the code.
    for i in range(1, n):
        if numbers[i] == numbers[s]:
            cnt[i] = cnt[i - 1] + 1
        else:
            cnt[i] = cnt[i - 1]
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is a positive integer, `s` is the minimum of `original_s - 1` and `original_f - 1`, `f` is the maximum of `original_s - 1` and `original_f - 1`, `a` and `b` remain in their initial states, `cnt` is a list of length `n` where each element `cnt[j]` (for `j` from 0 to `n-1`) is the count of occurrences of `numbers[s]` up to index `j` in the list `numbers`. If `numbers[j]` equals `numbers[s]`, then `cnt[j+1]` is `cnt[j] + 1`; otherwise, `cnt[j+1]` is `cnt[j]`. If the loop does not execute, `cnt` remains as `[1] + [0]*(n-1)`.
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
            
        #State of the program after the loop has been executed: `i` is `n`, `n` is a positive integer, `s` is the minimum of `original_s - 1` and `original_f - 1`, `f` is the maximum of `original_s - 1` and `original_f - 1`, `a` and `b` remain in their initial states, `cnt` remains as `[1] + [0]*(n-1)`, `ans` is `original_f - original_s` if `original_s <= original_f` and `ans` is `original_s - original_f` if `original_s > original_f`, and the current value of `numbers[s]` is not equal to `numbers[f]`; `l` is `0`, `r` is `1`, `m` is `0`. If `cnt[m] > cnt[f]` at this point, `r` is set to `1`. Otherwise, `l` is set to `1` and `m` is `1
        l = -1
        r = n
        while r > l + 1:
            m = (r + l) // 2
            
            if cnt[m] >= cnt[f]:
                r = m
            else:
                l = m
            
        #State of the program after the loop has been executed: `l` is 1, `r` is 2, `m` is 1, `cnt[m]` is less than `cnt[f]`.
        if (r != n) :
            ans = min(ans, f - r)
        #State of the program after the if block has been executed: *`l` is 1, `r` is 2, `m` is 1. If `r` is not equal to `n`, then `ans` is updated to be the minimum between its current value and `f - 2`, and `cnt[m]` remains less than `cnt[f]`. Since there is no else part, these conditions hold true regardless of the if condition's outcome.
    else :
        ans = 0
    #State of the program after the if-else block has been executed: `i` is `n`, `n` is a positive integer, `s` is the minimum of `original_s - 1` and `original_f - 1`, `f` is the maximum of `original_s - 1` and `original_f - 1`, `a` and `b` remain in their initial states, `cnt` remains as `[1] + [0]*(n-1)`. If `numbers[s] != numbers[f]`, then `l` is 1, `r` is 2, `m` is 1, and `ans` is updated to be the minimum between its current value and `f - 2`, with `cnt[m]` remaining less than `cnt[f]`. If `numbers[s] == numbers[f]`, then `ans` is `0`.
    stdout.write(str(ans))
#Overall this is what the function does:The function processes an integer \( n \), two integers \( s \) and \( f \) (which are derived from the inputs \( a \) and \( b \)), and a binary string \( s \) of length \( n \). It calculates the minimum distance within the substring from index \( s \) to index \( f \) where the character changes from the one at index \( s \) to another character. Specifically, it constructs a list `cnt` where each element `cnt[i]` represents the count of occurrences of the character at index \( s \) from the start of the string up to index \( i \). Then, based on whether the character at index \( s \) is different from the character at index \( f \), it either finds the nearest position to \( f \) where the character changes or concludes that no change occurs. The function ultimately writes the minimum distance found to the standard output. Potential edge cases include when \( s \) and \( f \) are the same (resulting in a distance of 0) or when the character at \( s \) is already the same as the one at \( f \) (resulting in a distance of 0). The function does not handle the case where \( s \) and \( f \) are out of bounds of the string, which could lead to undefined behavior.

