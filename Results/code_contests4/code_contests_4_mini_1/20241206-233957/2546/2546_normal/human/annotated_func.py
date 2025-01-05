#State of the program right berfore the function call: A, B, and C are integers such that 1 <= A, B, C <= 10.
def func():
    a, b, c = map(int, raw_input().split())
    if (a == 5 and b == 5 and c == 7) :
        print('YES')
    else :
        if (a == 5 and b == 7 and c == 5) :
            print('YES')
        else :
            if (a == 7 and b == 5 and c == 5) :
                print('YES')
            else :
                print('NO')
            #State of the program after the if-else block has been executed: *`A`, `B`, and `C` are integers such that 1 <= `A`, `B`, `C` <= 10. If `a` is equal to 7, `b` is equal to 5, and `c` is equal to 5, then "YES" is printed. Otherwise, "NO" is printed.
        #State of the program after the if-else block has been executed: *`A`, `B`, and `C` are integers such that 1 <= `A`, `B`, `C` <= 10. If `a` is 5, `b` is 7, and `c` is 5, then the output is 'YES'. If `a` is equal to 7, `b` is equal to 5, and `c` is equal to 5, then 'YES' is printed. Otherwise, the output is 'NO'.
    #State of the program after the if-else block has been executed: *`A`, `B`, and `C` are integers such that 1 <= `A`, `B`, `C` <= 10. If `a` is 5, `b` is 5, and `c` is 7, then 'YES' is printed. If `a` is 5, `b` is 7, and `c` is 5, then 'YES' is printed. If `a` is 7, `b` is 5, and `c` is 5, then 'YES' is printed. In all other cases, 'NO' is printed.
#Overall this is what the function does:The function accepts three integers, `a`, `b`, and `c`, entered by the user. It checks if the integers match the specific combinations of (5, 5, 7), (5, 7, 5), or (7, 5, 5) and prints 'YES' if any of these combinations are met. If none of the combinations match, it prints 'NO'. The function does not return any value and can handle inputs within the range of 1 to 10 for each integer.

