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
                #State of the program after the if-else block has been executed: *`n` is an integer, `m` is an integer, `k` is an integer, `area` is an integer and equals `n * m / k`, `area` is not equal to 0, 'YES' has been printed, '0 0' has been printed, 2 * `area` is greater than `n`. If 2 * `area` is less than or equal to `m`, then '1 ' and the value of `2 * area` have been printed, and '1 0' has been printed. Otherwise, `n` and `m // 2` have been printed, and `f'0 {m // 2}'` has been printed.
            #State of the program after the if-else block has been executed: `n` is an integer, `m` is an integer, `k` is an integer, `area` is an integer and equals `n * m / k`, `area` is not equal to 0, 'YES' has been printed, '0 0' has been printed. If `2 * area` is less than or equal to `n`, then `f'{2 * area} 1'` has been printed and '0 1' has been printed. If `2 * area` is greater than `n`, then either '1 ' and the value of `2 * area` have been printed, and '1 0' has been printed if `2 * area` is less than or equal to `m`, or `n` and `m // 2` have been printed, and `f'0 {m // 2}'` has been printed if `2 * area` is greater than `m`.
        #State of the program after the if-else block has been executed: *`n` is an integer, `m` is an integer, `k` is an integer, `area` is an integer and equals `n * m / k`. If `area` is 0, 'NO' has been printed to the console. If `area` is not equal to 0, 'YES' and '0 0' have been printed. Furthermore, if `2 * area` is less than or equal to `n`, then `f'{2 * area} 1'` and '0 1' have been printed. If `2 * area` is greater than `n`, then either '1 ' and the value of `2 * area` have been printed, and '1 0' has been printed if `2 * area` is less than or equal to `m`, or `n` and `m // 2` have been printed, and `f'0 {m // 2}'` has been printed if `2 * area` is greater than `m`.
    #State of the program after the if-else block has been executed: `n` is an integer, `m` is an integer, `k` is an integer, `area` is `n * m / k`. If `area` is not an integer, 'NO' has been printed. If `area` is an integer, then 'YES' and '0 0' have been printed. Additionally, if `area` is 0, 'NO' has been printed. If `area` is not equal to 0 and `2 * area` is less than or equal to `n`, then `f'{2 * area} 1'` and '0 1' have been printed. If `2 * area` is greater than `n`, then either '1 ' and the value of `2 * area` have been printed, and '1 0' has been printed if `2 * area` is less than or equal to `m`, or `n` and `m // 2` have been printed, and `f'0 {m // 2}'` has been printed if `2 * area` is greater than `m`.
#Overall this is what the function does:The function reads three integers `n`, `m`, and `k` from the user, where `1 <= n, m <= 10^9` and `2 <= k <= 10^9`. It calculates the area as `n * m / k`. If the area is not an integer, it prints 'NO'. If the area is an integer and equal to 0, it prints 'NO'. If the area is a non-zero integer, it prints 'YES' and '0 0', followed by additional output based on the value of `2 * area` relative to `n` and `m`. If `2 * area` is less than or equal to `n`, it prints `2 * area` and `1`, then `0` and `1`. If `2 * area` is greater than `n`, it checks if `2 * area` is less than or equal to `m`. If it is, it prints `1` and `2 * area`, then `1` and `0`. If `2 * area` is greater than `m`, it prints `n` and `m // 2`, then `0` and `m // 2`. The function does not return any value. The state of the program after execution will be that the input variables `n`, `m`, and `k` will have been used to calculate and print the specified output, and the calculated area will have been evaluated to determine whether 'YES' or 'NO' is printed.

