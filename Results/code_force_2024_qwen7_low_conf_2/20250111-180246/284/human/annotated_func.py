#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, and a list of n integers a_1, \ldots, a_n is given where each a_i is an even integer between 0 and n inclusive.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))
    if any(ai > 2 * (n - 1) for ai in a) :
        print('NO')
        return
        #The program returns 'NO'
    #State of the program after the if block has been executed: `n` is an integer within the range \(2 \leq n \leq 2 \times 10^5\); `data` is a list of strings representing the input; `a` is a list of integers obtained by converting the elements of `data[1:]` to integers. Any element in `a` is less than or equal to \(2 \times (n - 1)\)
    houses = []
    for i in range(n):
        x = i + 1
        
        y = i % n + 1
        
        houses.append((x, y))
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range \(2 \leq n \leq 2 \times 10^5\), `data` is a list of strings representing the input, `a` is a list of integers obtained by converting the elements of `data[1:]` to integers, any element in `a` is less than or equal to \(2 \times (n - 1)\), `houses` is a list containing tuples \((i+1, i \% n + 1)\) for all \(i\) in the range \(0\) to \(n-1\), `i` is \(n-1\), `x` is \(n\), `y` is `n \% n + 1`.
    visits = [-1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses
                    [j][1])
                if dist == a[i]:
                    visits[i] = j + 1
                    break
        
    #State of the program after the  for loop has been executed: `visits` is a list of length `n` where each element `visits[i]` is set to a value from `1` to `n` (inclusive), ensuring that for each `i` from `0` to `n-1`, there exists a `j` such that the distance between `houses[i]` and `houses[j]` is equal to `a[i]`. If no such `j` exists, then `visits[i]` remains `-1`.
    if (-1 in visits) :
        print('NO')
    else :
        print('YES')
        for (x, y) in houses:
            print(x, y)
            
        #State of the program after the  for loop has been executed: `visits` is a list of length `n` where each element `visits[i]` is set to a value from `1` to `n` (inclusive), `houses` is a non-empty iterable, `x` is the last element of the last pair processed in `houses`, `y` is the second element of the last pair processed in `houses`, the values of `x` and `y` are printed.
        print(' '.join(map(str, visits)))
    #State of the program after the if-else block has been executed: `visits` is a list of length `n` where each element `visits[i]` is set to a value from `1` to `n` (inclusive). For each `i` from `0` to `n-1`, there exists a `j` such that the distance between `houses[i]` and `houses[j]` is equal to `a[i]`. If no such `j` exists, then `visits[i]` remains `-1`. If there is at least one element in `visits` that is equal to `-1`, then nothing is printed to the console. Otherwise, the values of `x` and `y` are printed, where `x` is the last element of the last pair processed in `houses` and `y` is the second element of the last pair processed in `houses`.
#Overall this is what the function does:The function takes an integer \( n \) and a list of \( n \) even integers \( a \) as input. It first checks if any element in \( a \) exceeds \( 2 \times (n - 1) \). If any element does, it prints 'NO' and returns. Otherwise, it constructs a list of house coordinates based on the indices. Then, it attempts to find a valid visiting sequence for each house such that the distance between consecutive houses matches the corresponding element in \( a \). If a valid sequence can be found for all houses, it prints 'YES' followed by the house coordinates and the visiting sequence. If any house cannot be visited according to the conditions, it prints 'NO'. However, due to missing logic, the function might incorrectly print 'YES' even if not all houses can be visited correctly, as the condition check at the end only ensures the absence of -1 in visits, which is insufficient to guarantee a valid visiting sequence for all houses.

