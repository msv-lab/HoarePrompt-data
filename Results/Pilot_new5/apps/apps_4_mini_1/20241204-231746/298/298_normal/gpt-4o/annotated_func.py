#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 10^9, and k is an integer such that 2 ≤ k ≤ 10^9.
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
                #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers between 1 and 10^9, and `area` is equal to `n * m / k`, confirmed to be an integer and not equal to 0. If `2 * area` is less than or equal to `m`, then `2 * area` is greater than `n`. Otherwise, the output is '0 {m // 2}'.
            #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers between 1 and 10^9, and `area` is equal to `n * m / k`, confirmed to be an integer and not equal to 0. If `2 * area` is less than or equal to `n`, then the output printed is '0 1'. Otherwise, if `2 * area` is less than or equal to `m`, then `2 * area` is greater than `n`, and the output printed is '0 {m // 2}'. Otherwise, the output is '0 {m // 2}'.
        #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers between 1 and 10^9, and `area` is equal to `n * m / k`, confirmed to be an integer. If `area` is 0, 'NO' is printed. If `area` is not equal to 0, then if `2 * area` is less than or equal to `n`, the output printed is '0 1'. Otherwise, if `2 * area` is less than or equal to `m`, the output printed is '0 {m // 2}'. If neither condition is satisfied, the output is also '0 {m // 2}'.
    #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers between 1 and 10^9, and `area` is equal to `n * m / k`. If `area` is not an integer, 'NO' is printed. If `area` is an integer and equals 0, 'NO' is printed. If `area` is not equal to 0, then if `2 * area` is less than or equal to `n`, the output printed is '0 1'. Otherwise, if `2 * area` is less than or equal to `m`, the output printed is '0 {m // 2}'. If neither condition is satisfied, the output is also '0 {m // 2}'.
#Overall this is what the function does:The function accepts input values for integers `n`, `m`, and `k`. It calculates the area as `n * m / k` and checks if the area is an integer greater than zero. If the area is not an integer or equals zero, it prints "NO". If the area is a valid integer greater than zero, it prints "YES" and coordinates based on comparisons between `2 * area`, `n`, and `m`, determining specific coordinates to print. It handles cases where the area might not be achievable with the given dimensions and outputs accordingly.

