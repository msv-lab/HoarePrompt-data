#State of the program right berfore the function call: a is a list of tuples, where each tuple (x, y) consists of integers representing the coordinates of a black token, such that -105 ≤ x, y ≤ 105 and all tuples are distinct.
def func_1(a):
    inf = 1001001001
    C = 400010
    lmn = [inf] * 400010
    lmx = [-inf] * 400010
    for (x, y) in a:
        x = (x - 1) / 2 + 100005
        
        if lmn[x] > y:
            lmn[x] = y
        
        if lmx[x] < y:
            lmx[x] = y
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, where each tuple (x, y) consists of integers representing the coordinates of a black token, such that -105 ≤ x, y ≤ 105 and all tuples are distinct; `inf` is 1001001001; `C` is 400010; `lmn` is a list of 400010 elements, where each element at index `x` (where `x` is transformed from the original x-coordinate using the formula `(x - 1) / 2 + 100005`) is updated to the minimum `y` value among all tuples in `a` that map to the same transformed `x`; `lmx` is a list of 400010 elements, where each element at index `x` (where `x` is transformed from the original x-coordinate using the formula `(x - 1) / 2 + 100005`) is updated to the maximum `y` value among all tuples in `a` that map to the same transformed `x`.
    rmn = lmn[:]
    rmx = lmx[:]
    for i in xrange(200009):
        if lmn[i + 1] > lmn[i]:
            lmn[i + 1] = lmn[i]
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, `inf` is 1001001001, `C` is 400010, `lmn` is a list of 400010 elements where each element at index `x` is the minimum `y` value among all tuples in `a` that map to the same transformed `x`, `lmx` is a list of 400010 elements where each element at index `x` is the maximum `y` value among all tuples in `a` that map to the same transformed `x`, `rmn` is a shallow copy of the original `lmn`, `rmx` is a shallow copy of `lmx`, and `lmn` is modified such that for all indices `i` from 1 to 200009, `lmn[i]` is the minimum value of `lmn` from index 0 to index `i`.
    for i in xrange(200009):
        if lmx[i + 1] < lmx[i]:
            lmx[i + 1] = lmx[i]
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, `inf` is 1001001001, `C` is 400010, `lmn` is a list of 400010 elements where each element at index `x` is the minimum `y` value among all tuples in `a` that map to the same transformed `x`, and `lmn[i]` for all indices `i` from 1 to 200009 is the minimum value of `lmn` from index 0 to index `i`, `lmx` is a list of 400010 elements where each element at index `x` is the maximum `y` value among all tuples in `a` that map to the same transformed `x`, `lmx[i]` for all indices `i` from 1 to 200009 is the maximum value of `lmx` from index 0 to index `i`, `rmn` is a shallow copy of the original `lmn`, `rmx` is a shallow copy of the original `lmx`.
    for i in xrange(200009, 0, -1):
        if rmn[i - 1] > rmn[i]:
            rmn[i - 1] = rmn[i]
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, `inf` is 1001001001, `C` is 400010, `lmn` is a list of 400010 elements where each element at index `x` is the minimum `y` value among all tuples in `a` that map to the same transformed `x`, and `lmn[i]` for all indices `i` from 1 to 200009 is the minimum value of `lmn` from index 0 to index `i`, `lmx` is a list of 400010 elements where each element at index `x` is the maximum `y` value among all tuples in `a` that map to the same transformed `x`, and `lmx[i]` for all indices `i` from 1 to 200009 is the maximum value of `lmx` from index 0 to index `i`, `rmn` is a shallow copy of the original `lmn` with the property that for all indices `i` from 1 to 200009, `rmn[i]` is the minimum value of `rmn` from index 0 to index `i`, `rmx` is a shallow copy of the original `lmx`.
    for i in xrange(200009, 0, -1):
        if rmx[i - 1] < rmx[i]:
            rmx[i - 1] = rmx[i]
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, `inf` is 1001001001, `C` is 400010, `lmn` is a list of 400010 elements where each element at index `x` is the minimum `y` value among all tuples in `a` that map to the same transformed `x`, and `lmn[i]` for all indices `i` from 1 to 200009 is the minimum value of `lmn` from index 0 to index `i`, `lmx` is a list of 400010 elements where each element at index `x` is the maximum `y` value among all tuples in `a` that map to the same transformed `x`, and `lmx[i]` for all indices `i` from 1 to 200009 is the maximum value of `lmx` from index 0 to index `i`, `rmn` is a shallow copy of the original `lmn` with the property that for all indices `i` from 1 to 200009, `rmn[i]` is the minimum value of `rmn` from index 0 to index `i`, `rmx` is a shallow copy of the original `lmx`, and `rmx[i]` for all indices `i` from 1 to 200009 is the maximum value of `rmx` from index 0 to index `i`.
    for i in xrange(200010):
        if lmn[i] < rmn[i]:
            lmn[i] = rmn[i]
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, `inf` is 1001001001, `C` is 400010, `lmn` is a list of 400010 elements where each element at index `x` is the minimum `y` value among all tuples in `a` that map to the same transformed `x`, and for all indices `i` from 0 to 200009, `lmn[i]` is the maximum of the original `lmn[i]` and `rmn[i]`. `lmx` is a list of 400010 elements where each element at index `x` is the maximum `y` value among all tuples in `a` that map to the same transformed `x`, and `lmx[i]` for all indices `i` from 1 to 200009 is the maximum value of `lmx` from index 0 to index `i`. `rmn` is a shallow copy of the original `lmn` with the property that for all indices `i` from 1 to 200009, `rmn[i]` is the minimum value of `rmn` from index 0 to index `i`. `rmx` is a shallow copy of the original `lmx`, and `rmx[i]` for all indices `i` from 1 to 200009 is the maximum value of `rmx` from index 0 to index `i`.
    for i in xrange(200010):
        if lmx[i] > rmx[i]:
            lmx[i] = rmx[i]
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, `inf` is 1001001001, `C` is 400010, `lmn` is a list of 400010 elements where each element at index `x` is the minimum `y` value among all tuples in `a` that map to the same transformed `x`, and for all indices `i` from 0 to 200009, `lmn[i]` is the maximum of the original `lmn[i]` and `rmn[i]`, `lmx` is a list of 400010 elements where each element at index `x` is the minimum of the original maximum `y` value among all tuples in `a` that map to the same transformed `x` and the corresponding value in `rmx`, `rmn` is a shallow copy of the original `lmn` with the property that for all indices `i` from 1 to 200009, `rmn[i]` is the minimum value of `rmn` from index 0 to index `i`, `rmx` is a shallow copy of the original `lmx`, and for all indices `i` from 1 to 200009, `rmx[i]` is the maximum value of `rmx` from index 0 to index `i`.
    ans = 0
    for i in xrange(200009):
        if lmn[i] < lmn[i + 1]:
            lmn[i] = lmn[i + 1]
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, `inf` is 1001001001, `C` is 400010, `lmn` is a list of 400010 elements where each element at index `x` is the maximum `y` value among all tuples in `a` that map to the same transformed `x` and for all indices `i` from 0 to 200008, `lmn[i]` is the maximum of the original `lmn[i]` and `lmn[i + 1]`, `lmx` is a list of 400010 elements, `rmn` is a shallow copy of the original `lmn`, `rmx` is a shallow copy of the original `lmx`, `ans` is 0.
    for i in xrange(200009):
        if lmx[i] > lmx[i + 1]:
            lmx[i] = lmx[i + 1]
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, `inf` is 1001001001, `C` is 400010, `lmn` is a list of 400010 elements where each element at index `x` is the maximum `y` value among all tuples in `a` that map to the same transformed `x`, for all indices `i` from 0 to 200008, `lmn[i]` is the maximum of the original `lmn[i]` and `lmn[i + 1]`, `lmx` is a list of 400010 elements where for all indices `i` from 0 to 200008, `lmx[i]` is the minimum of the original `lmx[i]` and all subsequent elements up to `lmx[200009]`, `rmn` is a shallow copy of the original `lmn`, `rmx` is a shallow copy of the original `lmx`, `ans` is 0.
    for i in xrange(200009):
        if lmn[i] < lmx[i]:
            ans += (lmx[i] - lmn[i]) / 2
        
    #State of the program after the  for loop has been executed: `a` is a list of tuples, `inf` is 1001001001, `C` is 400010, `lmn` is a list of 400010 elements where each element at index `x` is the maximum `y` value among all tuples in `a` that map to the same transformed `x`, for all indices `i` from 0 to 200008, `lmn[i]` is the maximum of the original `lmn[i]` and `lmn[i + 1]`, `lmx` is a list of 400010 elements where for all indices `i` from 0 to 200008, `lmx[i]` is the minimum of the original `lmx[i]` and all subsequent elements up to `lmx[200009]`, `rmn` is a shallow copy of the original `lmn`, `rmx` is a shallow copy of the original `lmx`, `i` is 200009. `ans` is the sum of `(lmx[j] - lmn[j]) / 2` for all `j` from 0 to 200008 where `lmn[j] < lmx[j]`. If no such `j` exists, `ans` remains 0.
    return ans
    #The program returns `ans`, which is the sum of `(lmx[j] - lmn[j]) / 2` for all `j` from 0 to 200008 where `lmn[j] < lmx[j]`. If no such `j` exists, `ans` remains 0.
#Overall this is what the function does:The function `func_1` takes a list `a` of distinct tuples `(x, y)` where each coordinate is an integer within the range -105 to 105. It processes these coordinates to compute the minimum and maximum `y` values for each transformed `x` coordinate (using the formula `(x - 1) / 2 + 100005`). The function then adjusts these minimum and maximum values to ensure they are non-decreasing and non-increasing, respectively, across the range of transformed `x` values. Finally, it calculates and returns the sum of `(lmx[j] - lmn[j]) / 2` for all `j` from 0 to 200008 where `lmn[j] < lmx[j]`. If no such `j` exists, the function returns 0. The input list `a` remains unchanged throughout the execution of the function.

#State of the program right berfore the function call: The function does not take any parameters directly. However, it reads input from stdin where the first line is an integer n (1 ≤ n ≤ 105) representing the number of black points, followed by n lines each containing two integers x and y (-105 ≤ x, y ≤ 105) representing the coordinates of the black tokens. The coordinates are read into a list `dat` and processed to populate the list `s` which contains two sublists. Each sublist in `s` corresponds to the parity of the sum of the coordinates (x + y), and stores tuples (-x + y, x + y) for each black token.
def func_2():
    n = int(stdin.readline())
    dat = map(int, stdin.read().split(), repeat(10, 2 * n))
    s = [[], []]
    for i in xrange(n):
        x, y = dat[i * 2:i * 2 + 2]
        
        s[x + y & 1].append((-x + y, x + y))
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 105 (inclusive), `i` is `n - 1`, `dat` is a map object converting input from `stdin` into integers, `s` is a list where `s[0]` contains tuples `(-x + y, x + y)` for all pairs `(x, y)` where `x + y` is even, and `s[1]` contains tuples `(-x + y, x + y)` for all pairs `(x, y)` where `x + y` is odd.
    print(func_1(s[0]) + func_1(s[1]))
#Overall this is what the function does:The function `func_2` reads input from standard input (`stdin`) to process coordinates of black tokens. It expects the first line to contain an integer `n` (1 ≤ n ≤ 105) representing the number of black tokens, followed by `n` lines, each containing two integers `x` and `y` (-105 ≤ x, y ≤ 105) representing the coordinates of each token. The function populates a list `s` with two sublists based on the parity of the sum of the coordinates (`x + y`). Each sublist in `s` contains tuples `(-x + y, x + y)` for the respective parity (even or odd). After processing the coordinates, the function calls `func_1` on both sublists and prints the sum of the results. The final state of the program is that the input has been fully consumed, and the sum of the results from `func_1` for both sublists has been printed to the standard output. Edge cases and potential issues include handling invalid input (e.g., non-integer values, incorrect number of coordinates) and ensuring that `func_1` is defined and behaves correctly.

