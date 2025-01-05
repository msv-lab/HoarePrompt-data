#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18, and b is an integer such that 2 ≤ b ≤ 10^12.
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
        
    #State of the program after the loop has been executed: `b` is 1, `s` is the number of prime factors of the original value of `n`, `d_osn` contains the counts of all prime factors of the original value of `n`, and `cur` is greater than or equal to the square root of the initial value of `b`.
    if (b > 2) :
        d_osn[b] += 1
    #State of the program after the if block has been executed: *`b` is 1, `s` is the number of prime factors of the original value of `n`, `d_osn` contains the counts of all prime factors of the original value of `n`, and `cur` is greater than or equal to the square root of the initial value of `b`. If `b` is greater than 2, `d_osn[1]` is increased by 1.
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
        
    #State of the program after the  for loop has been executed: `res` is the minimum value of `mlt` calculated during the iterations of the loop, `izv` is the total contributions from all iterations, `newn` is less than or equal to the last value of `newk`, and `i` is 10 after all iterations complete.
    print(res)
#Overall this is what the function does:The function accepts two integers, `n` (where 1 ≤ n ≤ 10^18) and `b` (where 2 ≤ b ≤ 10^12), and calculates the minimum value of `mlt`, which is derived from the prime factorization of `b` and the powers of these factors that fit into `n`. It does this by counting the occurrences of each prime factor of `b`, determining how many times each factor can contribute to the powers of `n`, and outputs this minimum value. If `b` ends up being greater than 2 after factorization, it also counts that factor. The function does not return a value explicitly; instead, it prints the result.

