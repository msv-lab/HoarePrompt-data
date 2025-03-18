#State of the program right berfore the function call: t is a positive integer, n is a positive integer not exceeding 2 * 10^5, k is a positive integer not exceeding 10^15, and a is a list of positive integers where each integer a_i is not exceeding 10^9.
def func_1(n, k, a):
    l, r = 0, n - 1
    sunks = 0
    while l <= r:
        if k == 0:
            break
        
        if l == r:
            if k >= a[r]:
                sunks += 1
                break
            break
        
        if a[l] <= a[r]:
            if k >= a[l] * 2:
                k -= a[l] * 2
                a[r] -= a[l]
                if a[r] == 0:
                    sunks += 1
                    r -= 1
                sunks += 1
                l += 1
                continue
            elif a[l] * 2 - 1 == k:
                sunks += 1
                break
            else:
                break
        
        if k == 0:
            break
        
        if a[r] < a[l]:
            if k >= a[r] * 2:
                k -= a[r] * 2
                a[l] -= a[r]
                if a[l] == 0:
                    sunks += 1
                    l += 1
                sunks += 1
                r -= 1
                continue
            elif a[r] * 2 == k:
                sunks += 1
                break
            else:
                break
        
    #State: Output State: `t` is a positive integer, `n` is a positive integer not exceeding 2 * 10^5, `k` is a positive integer not exceeding 10^15, `a` is a list of positive integers where each integer `a_i` is not exceeding 10^9, `l` is n, `r` is -1, `sunks` is an integer representing the total number of times the condition `sunks += 1` was executed during the loop.
    #
    #Explanation: After the loop finishes executing, the value of `l` will be set to `n` because `l` is incremented until it exceeds `r`, which is initially `n-1`. Similarly, `r` will be set to `-1` because `r` is decremented until it is less than `l`, which is eventually set to `n`. The variable `sunks` will hold the total count of successful operations where either `a[l]` or `a[r]` is completely consumed (reduced to 0) and `sunks` is incremented.
    return sunks
    #The program returns the total number of times the condition `sunks += 1` was executed during the loop, where `l` is set to `n` and `r` is set to `-1` after the loop finishes executing.
#Overall this is what the function does:The function accepts three parameters: `n`, `k`, and `a`. `n` is a positive integer, `k` is a positive integer not exceeding \(10^{15}\), and `a` is a list of positive integers each not exceeding \(10^9\). It processes the list `a` by comparing elements at indices `l` and `r`, reducing their values based on the value of `k`, and increments a counter `sunks` each time a reduction operation is successfully completed. After the loop terminates, the function returns the total count of successful reduction operations stored in `sunks`. At the end of the function, the indices `l` and `r` are set to `n` and `-1`, respectively.

