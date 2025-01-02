#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, k is an integer such that 0 ≤ k ≤ 10^6, and h is a list of n integers where each hi satisfies 1 ≤ hi ≤ 10^6.
def func():
    n, k = [int(x) for x in raw_input().split()]
    hLst = [int(x) for x in raw_input().split()]
    a = i = j = 0
    r = []
    m = M = hLst[0]
    mI = MI = 0
    q1 = []
    q2 = []
    while j < n:
        w = hLst[j]
        
        if w <= m:
            m = w
            mI = j
        
        if w >= M:
            M = w
            MI = j
        
        heapq.heappush(q1, (w, j))
        
        heapq.heappush(q2, (-w, j))
        
        prevJ = j
        
        if M - m > k:
            break
        
        j += 1
        
    #State of the program after the loop has been executed: `n` is the first integer input, `k` is the second integer input, `h` is a list of `n` integers where each `hi` satisfies 1 ≤ `hi` ≤ 10^6, `hLst` is a list of integers from the input, `a` is 0, `i` is 0, `j` is the index where the loop stopped, `r` is an empty list, `m` is the minimum value encountered in `hLst` up to index `j`, `M` is the maximum value encountered in `hLst` up to index `j`, `mI` is the index of the minimum value `m` in `hLst` up to index `j`, `MI` is the index of the maximum value `M` in `hLst` up to index `j`, `q1` is a list of tuples `(value, index)` for each value in `hLst` up to index `j`, `q2` is a list of tuples `(-value, index)` for each value in `hLst` up to index `j`, `w` is the last value processed, `prevJ` is the last index processed. If `M - m > k`, the loop breaks out of the most internal loop or if statement.
    while j < n:
        if j - i > a:
            a = j - i
            r = [(i + 1, j)]
        elif j - i == a:
            r.append((i + 1, j))
        
        if j - i == 1:
            m = M = hLst[j]
            mI = MI = j
            i += 1
        elif mI < MI:
            i = mI + 1
            w, t = heapq.heappop(q1)
            while t < i:
                w, t = heapq.heappop(q1)
            heapq.heappush(q1, (w, t))
            m = w
            mI = t
            w, t = heapq.heappop(q2)
            while t < i:
                w, t = heapq.heappop(q2)
            heapq.heappush(q2, (w, t))
        else:
            i = MI + 1
            w, t = heapq.heappop(q2)
            while t < i:
                w, t = heapq.heappop(q2)
            heapq.heappush(q2, (w, t))
            M = -w
            MI = t
            w, t = heapq.heappop(q1)
            while t < i:
                w, t = heapq.heappop(q1)
            heapq.heappush(q1, (w, t))
        
        while j < n:
            w = hLst[j]
            if w <= m:
                m = w
                mI = j
            if w >= M:
                M = w
                MI = j
            if prevJ != j:
                heapq.heappush(q1, (w, j))
                heapq.heappush(q2, (-w, j))
                prevJ = j
            if M - m > k:
                break
            j += 1
        
    #State of the program after the loop has been executed: `n` is the first integer input, `k` is the second integer input, `h` is a list of `n` integers where each `hi` satisfies 1 ≤ `hi` ≤ 10^6, `hLst` is a list of integers from the input, `i` is the final value of `i` such that the difference between the maximum and minimum values in the subarray `hLst[i:j]` is at most `k`, `j` is the final value of `j` and is either the index where `M - m > k` or `n` if the loop completes without breaking, `m` is the minimum value encountered in `hLst` up to the last processed index `j`, `M` is the maximum value encountered in `hLst` up to the last processed index `j`, `mI` is the index of the minimum value `m` in `hLst` up to the last processed index `j`, `MI` is the index of the maximum value `M` in `hLst` up to the last processed index `j`, `q1` is a list of tuples `(value, index)` for each value in `hLst` up to the last processed index `j` but now missing all elements with indices less than `i`, `q2` is a list of tuples `(-value, index)` for each value in `hLst` up to the last processed index `j` but only contains elements with indices greater than or equal to `i`, `w` is the last value processed, `t` is the index of this value in `hLst` and is equal to `i - 1` if `mI >= MI`, `prevJ` is the last index processed and is now equal to `j`, `a` is the length of the longest subarray found where the difference between the maximum and minimum values is at most `k`, `r` is a list of tuples `(i + 1, j)` representing the starting and ending indices of all subarrays found where the difference between the maximum and minimum values is at most `k` and whose length is equal to `a`.
    if (j - i > a) :
        a = j - i
        r = [(i + 1, j)]
    else :
        if (j - i == a) :
            r.append((i + 1, j))
        #State of the program after the if block has been executed: *`n` is the first integer input, `k` is the second integer input, `h` is a list of `n` integers where each `hi` satisfies 1 ≤ `hi` ≤ 10^6, `hLst` is a list of integers from the input, `i` is the final value of `i` such that the difference between the maximum and minimum values in the subarray `hLst[i:j]` is at most `k`, `j` is the final value of `j` and is either the index where `M - m > k` or `n` if the loop completes without breaking, `m` is the minimum value encountered in `hLst` up to the last processed index `j`, `M` is the maximum value encountered in `hLst` up to the last processed index `j`, `mI` is the index of the minimum value `m` in `hLst` up to the last processed index `j`, `MI` is the index of the maximum value `M` in `hLst` up to the last processed index `j`, `q1` is a list of tuples `(value, index)` for each value in `hLst` up to the last processed index `j` but now missing all elements with indices less than `i`, `q2` is a list of tuples `(-value, index)` for each value in `hLst` up to the last processed index `j` but only contains elements with indices greater than or equal to `i`, `w` is the last value processed, `t` is the index of this value in `hLst` and is equal to `i - 1` if `mI >= MI`, `prevJ` is the last index processed and is now equal to `j`, `a` is the length of the longest subarray found where the difference between the maximum and minimum values is at most `k`, `r` is a list of tuples `(i + 1, j)` representing the starting and ending indices of all subarrays found where the difference between the maximum and minimum values is at most `k` and whose length is equal to `a`, and if `j - i == a`, a new tuple `(i + 1, j)` is appended to the list `r`.
    #State of the program after the if-else block has been executed: *`n` is the first integer input, `k` is the second integer input, `h` is a list of `n` integers where each `hi` satisfies 1 ≤ `hi` ≤ 10^6, `hLst` is a list of integers from the input, `i` is the final value of `i` such that the difference between the maximum and minimum values in the subarray `hLst[i:j]` is at most `k`, `j` is the final value of `j` and is either the index where `M - m > k` or `n` if the loop completes without breaking, `m` is the minimum value encountered in `hLst` up to the last processed index `j`, `M` is the maximum value encountered in `hLst` up to the last processed index `j`, `mI` is the index of the minimum value `m` in `hLst` up to the last processed index `j`, `MI` is the index of the maximum value `M` in `hLst` up to the last processed index `j`, `q1` is a list of tuples `(value, index)` for each value in `hLst` up to the last processed index `j` but now missing all elements with indices less than `i`, `q2` is a list of tuples `(-value, index)` for each value in `hLst` up to the last processed index `j` but only contains elements with indices greater than or equal to `i`, `w` is the last value processed, `t` is the index of this value in `hLst` and is equal to `i - 1` if `mI >= MI`, `prevJ` is the last index processed and is now equal to `j`, `a` is the length of the longest subarray found where the difference between the maximum and minimum values is at most `k`, `r` is a list of tuples `(i + 1, j)` representing the starting and ending indices of all subarrays found where the difference between the maximum and minimum values is at most `k` and whose length is equal to `a`. If `j - i > a`, then `a` is updated to `j - i` and `r` is updated to `[(i + 1, j)]`. If `j - i == a`, a new tuple `(i + 1, j)` is appended to the list `r`.
    print(str(a) + ' ' + str(len(r)))
    for x in r:
        print(str(x[0]) + ' ' + str(x[1]))
        
    #State of the program after the  for loop has been executed: `n` is the first integer input, `k` is the second integer input, `h` is a list of `n` integers where each `hi` satisfies 1 ≤ `hi` ≤ 10^6, `hLst` is a list of integers from the input, `i` is the final value of `i` such that the difference between the maximum and minimum values in the subarray `hLst[i:j]` is at most `k`, `j` is the final value of `j` and is either the index where `M - m > k` or `n` if the loop completes without breaking, `m` is the minimum value encountered in `hLst` up to the last processed index `j`, `M` is the maximum value encountered in `hLst` up to the last processed index `j`, `mI` is the index of the minimum value `m` in `hLst` up to the last processed index `j`, `MI` is the index of the maximum value `M` in `hLst` up to the last processed index `j`, `q1` is a list of tuples `(value, index)` for each value in `hLst` up to the last processed index `j` but now missing all elements with indices less than `i`, `q2` is a list of tuples `(-value, index)` for each value in `hLst` up to the last processed index `j` but only contains elements with indices greater than or equal to `i`, `w` is the last value processed, `t` is the index of this value in `hLst` and is equal to `i - 1` if `mI >= MI`, `prevJ` is the last index processed and is now equal to `j`, `a` is the length of the longest subarray found where the difference between the maximum and minimum values is at most `k`, `r` is a list of tuples `(i + 1, j)` representing the starting and ending indices of all subarrays found where the difference between the maximum and minimum values is at most `k` and whose length is equal to `a`, and all elements in `r` have been printed.
#Overall this is what the function does:The function `func` processes two inputs: `n` and `k`, where `n` is the number of elements in a list `hLst` and `k` is a threshold value. The function reads `n` and `k` from the input, followed by `n` integers which form the list `hLst`. The function aims to find the longest subarray within `hLst` such that the difference between the maximum and minimum values in the subarray is at most `k`. It also identifies all such subarrays of the same maximum length. After processing, the function prints the length of the longest subarray (`a`) and the number of such subarrays found (`len(r)`). For each identified subarray, it prints the starting and ending indices (1-based). The function handles edge cases such as when no valid subarray exists, in which case it will still print the length of the longest subarray found, even if it is zero.

