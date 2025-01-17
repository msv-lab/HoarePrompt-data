#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, \ldots, a_n is given, where 0 ≤ a_i ≤ n and all a_i are even.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))
    if any(ai > 2 * (n - 1) for ai in a) :
        print('NO')
        return
        #The program does not return any value and prints 'NO'
    #State of the program after the if block has been executed: `data` is a list of strings, where the first element is the integer value of the original string `n` and the remaining elements are the even integers `a_1, \ldots, a_n` as strings; `a` is a list of integers, where each element is an integer converted from the corresponding string in `data[1:]`; all elements `ai` in `a` are less than or equal to 2 * (n - 1)
    houses = []
    for i in range(n):
        x = i + 1
        
        y = i % n + 1
        
        houses.append((x, y))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `data` is a list of strings with at least `n + 1` elements, the first element of `data` is the integer value of `n`, and the remaining elements are even integers as strings; `a` is a list of integers where each element is an integer converted from the corresponding string in `data[1:]` and each element in `a` is less than or equal to `2 * (n - 1)`; `houses` is a list of length `n` containing the tuples `(x, y)` where `x` is `i + 1` and `y` is `i % n + 1` for each iteration `i` from `0` to `n-1`.
    visits = [-1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses
                    [j][1])
                if dist == a[i]:
                    visits[i] = j + 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `data` is a list of strings with at least `n + 1` elements, the first element of `data` is the integer value of `n`, and the remaining elements are even integers as strings; `a` is a list of integers where each element is an integer converted from the corresponding string in `data[1:]` and each element in `a` is less than or equal to `2 * (n - 1)`, `houses` is a list of length `n` containing the tuples `(x, y)` where `x` is `i + 1` and `y` is `i % n + 1` for each iteration `i` from `0` to `n-1`; `visits` is a list of length `n` where each element `visits[i]` is set to `j + 1` if there exists a `j` such that the Manhattan distance between `houses[i]` and `houses[j]` equals `a[i]`, otherwise, `visits[i]` remains `-1`.
    if (-1 in visits) :
        print('NO')
    else :
        print('YES')
        for (x, y) in houses:
            print(x, y)
            
        #State of the program after the  for loop has been executed: `n` is a positive integer, `data` is a list of strings with at least `n + 1` elements, the first element of `data` is the integer value of `n`, and the remaining elements are even integers as strings, `a` is a list of integers where each element is less than or equal to `2 * (n - 1)`, `houses` is a list of length `n` containing the tuples `(x, y)` where `x = i + 1` and `y = i % n + 1` for each iteration `i` from `0` to `n-1`, `visits` is a list of length `n` where each element `visits[i]` is a positive integer if there exists a `j` such that the Manhattan distance between `houses[i]` and `houses[j]` equals `a[i]`, otherwise, `visits[i]` is `-1`. The values of `x` and `y` for all tuples in `houses` are printed.
        print(' '.join(map(str, visits)))
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `data` is a list of strings with at least `n + 1` elements, the first element of `data` is the integer value of `n`, and the remaining elements are even integers as strings; `a` is a list of integers where each element is an integer converted from the corresponding string in `data[1:]` and each element in `a` is less than or equal to `2 * (n - 1)`, `houses` is a list of length `n` containing the tuples `(x, y)` where `x` is `i + 1` and `y` is `i % n + 1` for each iteration `i` from `0` to `n-1`; `visits` is a list of length `n` where each element `visits[i]` is a positive integer if there exists a `j` such that the Manhattan distance between `houses[i]` and `houses[j]` equals `a[i]`, otherwise, `visits[i]` is `-1`. If `-1` is found in `visits`, the program prints 'NO'. Otherwise, the program prints the string representation of the list `visits` separated by spaces.
#Overall this is what the function does:The function processes a list of integers representing distances and checks if these distances can be satisfied by placing `n` houses in a circular manner such that the Manhattan distance between certain pairs of houses matches the given distances. If it is possible to satisfy all distances, the function prints 'YES' followed by the coordinates of the houses and the indices of the houses they visit. If it is not possible, the function prints 'NO'. The function does not return any value.

