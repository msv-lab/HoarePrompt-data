#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^18) and b is a positive integer representing the base (2 ≤ b ≤ 10^12).
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
        
    #State of the program after the loop has been executed: `b` is 1, `cur` is greater than or equal to the square root of the initial value of `b`, `d_osn` contains the prime factorization counts of the original value of `b` with respect to its prime factors.
    if (b > 2) :
        d_osn[b] += 1
    #State of the program after the if block has been executed: *`b` is 1, `cur` is greater than or equal to the square root of the initial value of `b`, and `d_osn` contains the prime factorization counts of the original value of `b` with respect to its prime factors. If `b` is greater than 2, then `d_osn[b]` is incremented by 1.
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
        
    #State of the program after the  for loop has been executed: `newn` is less than or equal to `newk`, `izv` is the accumulated value based on the prime factorization involving all prime factors of `b`, `i` is 10, and `res` is the minimum value calculated from `mlt` for all iterations or remains -1 if no valid calculations were made.
    print(res)
#Overall this is what the function does:The function accepts two positive integers, `n` (1 ≤ n ≤ 10^18) and `b` (2 ≤ b ≤ 10^12). It calculates the prime factorization of `b`, counts the factors, and uses these counts to derive a result based on the powers of the prime factors compared to `n`. The function outputs the minimum value of a calculated variable derived from these factors or -1 if no valid calculations were made. Edge cases include the possibility of `b` being reduced to 1 and the handling of the prime factors in relation to `n`.

