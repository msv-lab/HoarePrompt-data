#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^18, and b is an integer such that 2 ≤ b ≤ 10^12.
def func():
    n, b = [int(x) for x in raw_input().split()]
    s = 0
    d_osn = defaultdict(int)
    cur = 2
    while b > 1:
        if b % cur == 0:
            d_osn[cur] += 1
            b /= cur
            continue
        elif cur == 2:
            cur = 3
        else:
            cur += 2
        
        if cur >= b ** 0.5:
            break
        
    #State of the program after the loop has been executed: `b` is reduced to 1 or a prime number greater than 1, `s` is 0, `d_osn` contains the count of the prime factors of the initial value of `b`, and `cur` is an odd integer greater than or equal to the square root of the original value of `b`.
    if (b > 2) :
        d_osn[b] += 1
    #State of the program after the if block has been executed: *`b` is reduced to 1 or a prime number greater than 1. If `b` is greater than 2, `d_osn[b]` is incremented by 1 while `s` remains 0, and `d_osn` still contains the count of the prime factors of the initial value of `b`, with `cur` being an odd integer greater than or equal to the square root of the original value of `b`.
    izv = defaultdict(int)
    res = -1
    for k in d_osn:
        izv = 0
        
        newk = k
        
        newn = n
        
        i = 0
        
        while True and i < 10:
            st = 0
            i += 1
            newizv = 0
            newnewk = newk
            while newnewk <= newn:
                newnewk *= newk
                st += 1
            if st == 0:
                break
            for i in range(st):
                newizv = newizv * 2 + 1
            while newn > newk ** st:
                izv += newizv
                newn = newn - newk ** st
        
        mlt = izv // d_osn[k]
        
        if res == -1:
            res = mlt
        elif mlt < res:
            res = mlt
        
    #State of the program after the  for loop has been executed: `newn` is less than or equal to `newk`, `izv` is the total accumulated value from all iterations, `i` is 10, `newizv` is the last calculated value of `2^st - 1`, `newnewk` is greater than or equal to `newn`, `mlt` is the value of `izv // d_osn[k]`, and `res` is the minimum value among all calculated `mlt` values, or remains as -1 if no valid calculations occurred.
    print(res)
#Overall this is what the function does:The function accepts two integers, `n` (where 1 ≤ n ≤ 10^18) and `b` (where 2 ≤ b ≤ 10^12), and calculates the minimum value of `izv // d_osn[k]` for each prime factor `k` of the initial value of `b`. The function prints this minimum value, which may be -1 if no valid calculations occur. The function does not return any value.

