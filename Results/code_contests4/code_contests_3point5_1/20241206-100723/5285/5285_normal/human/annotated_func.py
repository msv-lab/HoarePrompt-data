#State of the program right berfore the function call: **Precondition**: **n and b are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ b ≤ 10^12.**
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
        
    #State of the program after the loop has been executed: `n` is an integer between 1 and 10^18, `b` is 1, `s` is 0, `d_osn` is a defaultdict with integer values, `cur` is greater than or equal to the square root of the original value of `b`
    if (b > 2) :
        d_osn[b] += 1
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 10^18, `b` is greater than 2, `s` is 0, `d_osn` is a defaultdict with integer values where the value for key `b` is incremented by 1, `cur` is greater than or equal to the square root of the original value of `b`.
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
        
    #State of the program after the  for loop has been executed: `res` is the minimum value of the floor division of the sum of all calculated `izv` values by their respective `d_osn[k]` for all `k` in `d_osn`.
    print(res)
#Overall this is what the function does:The function `func` reads two integers `n` and `b`, then calculates and outputs a result based on the provided constraints: 1 ≤ n ≤ 10^18 and 2 ≤ b ≤ 10^12. It iterates through prime factors of `b`, performs calculations, and finally prints the minimum value obtained from the calculations.

