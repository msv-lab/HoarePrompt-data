#State of the program right berfore the function call: n, m, and k are integers such that 1 ≤ n, m ≤ 10^9 and 2 ≤ k ≤ 10^9.
def func():
    n, m, k = map(int, input().split())
    area = n * m / k
    if (area != int(area)) :
        print('NO')
    else :
        area = int(area)
        if (area == 0) :
            print('NO')
        else :
            print('YES')
            print('0 0')
            if (2 * area <= n) :
                print(f'{2 * area} 1')
                print(f'0 1')
            else :
                if (2 * area <= m) :
                    print(f'1 {2 * area}')
                    print(f'1 0')
                else :
                    print(f'{n} {m // 2}')
                    print(f'0 {m // 2}')
                #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers, `area` is defined as `n * m / k`. If `2 * area <= m`, the output is `'1 2 * (n * m / k)'`. Otherwise, `m` is halved (`m // 2`), and the output is `'0 0'`. Both conditions `2 * area > n` and `2 * area > m` must still hold true after the execution of the if-else block.
            #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers, `area` is defined as `n * m / k`. The output depends on the following conditions:
            #- If `2 * area <= n`, the output is `'0 1'`.
            #- If `2 * area > n` and `2 * area <= m`, the output is `'1 2 * (n * m / k)'`.
            #- If `2 * area > m`, `m` is halved (`m // 2`), and the output is `'0 0'`.
        #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers, `area` is defined as `n * m / k`. The final state of the program is as follows:
        #- If `area` equals 0, the output is determined by the initial values of `n`, `m`, and `k`.
        #- If `area` is not 0, the output is:
        #  - `'0 1'` if `2 * area <= n`.
        #  - `'1 2 * (n * m / k)'` if `2 * area > n` and `2 * area <= m`.
        #  - `'0 0'` if `2 * area > m` and `m` is halved (`m // 2`).
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers, and `area` is defined as `n * m / k`. The overall state of the program is as follows:
    #- If `area` is not an integer, the console prints 'NO'.
    #- If `area` equals 0, the output is determined by the initial values of `n`, `m`, and `k`.
    #- If `area` is not 0:
    #  - `'0 1'` if `2 * area <= n`.
    #  - `'1 2 * (n * m / k)'` if `2 * area > n` and `2 * area <= m`.
    #  - `'0 0'` if `2 * area > m` and `m` is halved (`m // 2`).
#Overall this is what the function does:The function reads three integers `n`, `m`, and `k` from the standard input. It calculates the area as `n * m / k` and checks if this area is an integer. If the area is not an integer, it prints 'NO'. If the area is zero, it also prints 'NO'. Depending on the values of `n`, `m`, and `k`, it prints one of the following outputs:

