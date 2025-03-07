#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is an integer such that 1 <= t <= 1000. For each iteration, the function receives three integers a, b, and c, each ranging from 0 to 9.
def func():
    q = int(input())
    mn = 100
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        
        if a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The loop will execute `q` times, and for each iteration, it will read three integers `a`, `b`, and `c` from the input. Depending on the values of `a`, `b`, and `c`, it will print 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The variable `mn` remains unchanged at 100.
#Overall this is what the function does:The function `func` reads an integer `q` from the input, which specifies the number of iterations to perform. For each of the `q` iterations, it reads three integers `a`, `b`, and `c` from the input. Depending on the values of `a`, `b`, and `c`, it prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The variable `mn` is initialized to 100 but remains unchanged throughout the function. The function does not return any value.

