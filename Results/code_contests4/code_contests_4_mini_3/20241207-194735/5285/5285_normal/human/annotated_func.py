#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18, and b is a positive integer such that 2 ≤ b ≤ 10^12.
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
        
    #State of the program after the loop has been executed: `b` is reduced to its smallest prime factorization if it was divisible by prime numbers less than or equal to the square root of its original value; `d_osn` contains counts of these prime factors, `cur` is a prime number greater than or equal to the square root of the original `b`, and `s` remains 0.
    if (b > 2) :
        d_osn[b] += 1
    #State of the program after the if block has been executed: *`b` is reduced to its smallest prime factorization if it was divisible by prime numbers less than or equal to the square root of its original value. If `b` is greater than 2, then `d_osn[b]` is increased by 1, `cur` is a prime number greater than or equal to the square root of the original `b`, and `s` remains 0. If `b` is not greater than 2, the postcondition does not change as there is no else part.
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
        
    #State of the program after the  for loop has been executed: `i` is 10, `izv` is the total accumulation based on all calculations during iterations, `newn` is less than or equal to `newk`, `newnewk` is equal to `newk` raised to the maximum power computed, `mlt` is the last calculated value of `izv // d_osn[k]`, and `res` is the minimum of all `mlt` values computed or the last assigned value.
    print(res)
#Overall this is what the function does:The function accepts two positive integers, `n` (between 1 and 10^18) and `b` (between 2 and 10^12), and computes the minimum value of `izv // d_osn[k]` for all prime factors `k` of `b`. The function prints this minimum value as the result. If `b` is not divisible by any prime factors less than or equal to its square root, it considers `b` itself as a prime factor if it is greater than 2. The output is the minimum calculated value or potentially an error due to the nature of the calculations if no valid factors are found.

