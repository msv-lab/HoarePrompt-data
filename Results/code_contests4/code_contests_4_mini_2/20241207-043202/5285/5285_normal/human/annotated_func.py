#State of the program right berfore the function call: n is a positive integer within the range 1 ≤ n ≤ 10^18, and b is an integer within the range 2 ≤ b ≤ 10^12.
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
        
    #State of the program after the loop has been executed: `b` is a prime number or 1, `d_osn` contains the count of prime factors of `b`, where each key is a prime factor and its value is the number of times it divides `b`; `cur` is at least the square root of the original value of `b`; `s` remains 0.
    if (b > 2) :
        d_osn[b] += 1
    #State of the program after the if block has been executed: *`b` is a prime number or 1. If `b` > 2, then `d_osn` contains the count of prime factors of `b`, where `d_osn[b]` is incremented by 1, `cur` remains at least the square root of the original value of `b`, and `s` remains 0.
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
        
    #State of the program after the  for loop has been executed: `newn` is less than or equal to 0, `izv` is the total sum of all increments based on `newizv` multiplied by the number of iterations of the inner loop, `i` is 10, `newk` is equal to the last value of `k`, `mlt` is equal to `izv // d_osn[k]`, and `res` is the minimum value between the computed `mlt` and any previous values of `res`, which could be -1 if the loop did not execute. `b` is a prime number greater than 2, `d_osn` contains at least one key, `cur` remains at least the square root of the original value of `b`, and `s` remains 0.
    print(res)
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 10^18) and an integer `b` (2 ≤ b ≤ 10^12). It calculates the prime factorization of `b` and then computes the minimum value of a certain derived metric based on the prime factors of `b` and the integer `n`. The function prints this minimum value, which represents a count of certain combinations based on the prime factors and their powers. The function does not handle any edge cases related to invalid input or constraints, and the variable `s` remains unused throughout the code.

