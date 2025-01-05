#State of the program right berfore the function call: n and b are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ b ≤ 10^12.**
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
        
    #State of the program after the loop has been executed: `n` and `b` are integers within the specified ranges, `s` is 0, `d_osn[cur]` is updated based on divisibility of `b` by `cur`, `cur` is either 3 or a value greater than 3 after the execution of the if else block, the current value of `cur` is greater than or equal to the square root of `b`, for the loop to execute again `b` is 1.
    if (b > 2) :
        d_osn[b] += 1
    #State of the program after the if block has been executed: *`n` and `b` are integers within the specified ranges, `s` is 0, `d_osn[cur]` is updated based on divisibility of `b` by `cur`, `cur` is either 3 or a value greater than 3 after the execution of the if else block, the current value of `cur` is greater than or equal to the square root of `b`, for the loop to execute again `b` is 1. Additionally, `b` is greater than 2.
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
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, `res` will contain the minimum value of the integer division result of `izv` divided by `d_osn[k]` for all `k` in `d_osn`. All other variables will return to their initial states.
    print(res)
#Overall this is what the function does:The function reads two integers `n` and `b` from the input, calculates the minimum number of times `n` can be divided by a prime factor of `b`, and prints the result.

