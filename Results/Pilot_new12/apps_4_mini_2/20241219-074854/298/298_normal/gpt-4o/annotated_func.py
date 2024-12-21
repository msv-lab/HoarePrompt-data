#State of the program right berfore the function call: n, m, and k are integers such that 1 <= n, m <= 10^9 and 2 <= k <= 10^9.
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
                #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers such that 1 <= n, m <= 10^9 and 2 <= k <= 10^9; `area` is equal to `n * m / k` and is a non-zero integer, with the value of `area` greater than `n / 2`. If `2 * area` is less than or equal to `m`, then '1 0' is printed. Otherwise, `m` is halved, and '0' followed by the value of `m // 4` is printed.
            #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers such that 1 <= n, m <= 10^9 and 2 <= k <= 10^9. If `2 * area` is less than or equal to `n`, `2 * area` is 0 and the output is '0 1'. Otherwise, if `area` is greater than `n / 2`, and `2 * area` is less than or equal to `m`, the output is '1 0'. If `2 * area` is greater than `m`, `m` is halved and the output is '0' followed by the value of `m // 4`.
        #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers such that 1 <= n, m <= 10^9 and 2 <= k <= 10^9. If `area` is equal to 0, the output is 'NO'. Otherwise, if `2 * area` is less than or equal to `n`, then `2 * area` is 0 and the output is '0 1'. If `area` is greater than `n / 2` and `2 * area` is less than or equal to `m`, the output is '1 0'. If `2 * area` is greater than `m`, `m` is halved and the output is '0' followed by the value of `m // 4`.
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers such that 1 <= n, m <= 10^9 and 2 <= k <= 10^9; if `area` is not an integer, the output is 'NO'. Otherwise, if `area` is equal to 0, the output is 'NO'. If `2 * area` is less than or equal to `n`, then `2 * area` is 0 and the output is '0 1'. If `area` is greater than `n / 2` and `2 * area` is less than or equal to `m`, the output is '1 0'. If `2 * area` is greater than `m`, `m` is halved and the output is '0' followed by the value of `m // 4`.
#Overall this is what the function does:The function accepts three integer parameters `n`, `m`, and `k`, which represent dimensions and a divisor, respectively. It calculates the area as `n * m / k`. If the computed `area` is not an integer or is zero, the function outputs 'NO'. If `area` is a positive integer, it outputs 'YES' and attempts to provide coordinates based on the values of `n`, `m`, and `area`. If `2 * area` is less than or equal to `n`, it prints the coordinates '0 1'. If `2 * area` is less than or equal to `m`, it prints '1 0'. If `2 * area` exceeds both `n` and `m`, it halves `m` and then prints '0' followed by the value of `m // 2`. There are no return values; the function relies solely on print outputs to convey its findings. The code lacks functionality for input validation beyond area checks and does not handle cases explicitly where the area could lead to negative outputs in an unaccounted manner.

