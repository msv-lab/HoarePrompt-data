#State of the program right berfore the function call: a is a list of tuples, where each tuple contains two integers representing the coordinates (x, y) of a black token's initial position. All coordinates are distinct and within the range [-100000, 100000].
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
        
    #State of the program after the  for loop has been executed: `a` must contain at least one tuple, `x` is equal to \((x - 1) / 2 + 100005\), `lmn[x]` is the maximum value of `y` among all tuples in `a` such that \(lmx[x] < y\), and `lmx[x]` is the minimum value of `y` among all tuples in `a` such that \(lmn[x] > y\).
    rmn = lmn[:]
    rmx = lmx[:]
    for i in xrange(200009):
        if lmn[i + 1] > lmn[i]:
            lmn[i + 1] = lmn[i]
        
    #State of the program after the  for loop has been executed: `a` must contain at least one tuple, `lmn` and `lmx` must be initialized with valid values based on the tuples in `a`, `rmn` is a shallow copy of `lmn`, `rmx` is a shallow copy of `lmx`. After all iterations of the loop, `lmn[200009]` is the minimum value of `y` among all tuples in `a`, `lmx` remains unchanged, and `i` is 200009.
    for i in xrange(200009):
        if lmx[i + 1] < lmx[i]:
            lmx[i + 1] = lmx[i]
        
    #State of the program after the  for loop has been executed: `a` must contain at least one tuple, `lmn` and `lmx` remain unchanged, `rmn` is a shallow copy of `lmn`, `rmx` is a shallow copy of `lmx`, `i` is 200009. If `lmx[i + 1]` is equal to `lmx[i]` for all `i` from 0 to 200008, then `lmn[200009]` is the minimum value of `y` among all tuples in `a`, `lmx` remains unchanged, and `i` is 200009.
    for i in xrange(200009, 0, -1):
        if rmn[i - 1] > rmn[i]:
            rmn[i - 1] = rmn[i]
        
    #State of the program after the  for loop has been executed: `a` must contain at least one tuple, `lmn` and `lmx` remain unchanged, `rmn` is a shallow copy of `lmn`, `rmx` is a shallow copy of `lmx`, `i` is 1. `rmn` is adjusted such that for all `i` from 0 to 200008, `rmn[i]` is the maximum of `rmn[i]` and `rmn[i + 1]`. If the condition `rmn[i - 1] > rmn[i]` holds for any `i` from 200008 to 1, then `rmn` maintains the relationship; otherwise, no changes are made to `rmn` and `rmx`, and `i` is 1.
    for i in xrange(200009, 0, -1):
        if rmx[i - 1] < rmx[i]:
            rmx[i - 1] = rmx[i]
        
    #State of the program after the  for loop has been executed: `a` must contain at least one tuple, `lmn` and `lmx` remain unchanged, `rmn` is a shallow copy of `lmn`, `rmx[0]` is the maximum value in `rmx`, and all other elements in `rmx` (from `1` to `200008`) are also `rmx[0]`, `i` is 1.
    for i in xrange(200010):
        if lmn[i] < rmn[i]:
            lmn[i] = rmn[i]
        
    #State of the program after the  for loop has been executed: `a` must contain at least one tuple, `lmn` and `lmx` remain unchanged, `rmn` is a shallow copy of `lmn`, `rmx[0]` is the maximum value in `rmx`, and all other elements in `rmx` (from `1` to `200008`) are also `rmx[0]`, `i` is `200010` and must be within the range `[0, 200009]`, and for every index `j` in the range `[0, 200008]`, `lmn[j]` is equal to `rmn[j]`.
    for i in xrange(200010):
        if lmx[i] > rmx[i]:
            lmx[i] = rmx[i]
        
    #State of the program after the  for loop has been executed: `a` contains at least one tuple, `lmn` and `lmx` remain unchanged, `rmn` is a shallow copy of `lmn`, `rmx[0]` is the maximum value in `rmx`, and all other elements in `rmx` (from 1 to 200008) are also `rmx[0]`, and `i` is 200010. For every index `j` in the range [0, 200008], if `lmx[j] > rmx[j]` at any point during the loop execution, then `lmx[j]` is set to `rmx[j]`. Otherwise, `lmx[j]` remains unchanged and equals `rmx[0]`.
    ans = 0
    for i in xrange(200009):
        if lmn[i] < lmn[i + 1]:
            lmn[i] = lmn[i + 1]
        
    #State of the program after the  for loop has been executed: `lmn` is an array where all elements from 0 to 200007 are equal to `lmn[200008]`, `i` is 0, and `ans` is 0.
    for i in xrange(200009):
        if lmx[i] > lmx[i + 1]:
            lmx[i] = lmx[i + 1]
        
    #State of the program after the  for loop has been executed: `lmn` is an array where all elements from 0 to 200007 are equal to `lmn[200008]`, `i` is 200009, and `ans` is 0. `lmx` is a non-increasing sequence starting from `lmn[200008]` and ending at `lmx[0]`.
    for i in xrange(200009):
        if lmn[i] < lmx[i]:
            ans += (lmx[i] - lmn[i]) / 2
        
    #State of the program after the  for loop has been executed: `i` is 200008, `ans` is the sum of `(lmx[j] - lmn[j]) / 2` for all j from 0 to 200007 where `lmn[j] < lmx[j]`, and `lmn[j]` is less than `lmx[j]` for all j from 0 to 200007.
    return ans
    #The program returns ans which is the sum of (lmx[j] - lmn[j]) / 2 for all j from 0 to 200007 where lmn[j] < lmx[j]
#Overall this is what the function does:The function `func_1` accepts a parameter `a`, which is a list of tuples, where each tuple contains two integers representing the coordinates (x, y) of a black token's initial position. The coordinates are distinct and within the range [-100000, 100000]. The function processes these coordinates to determine the maximum and minimum y-values for each x-coordinate, stored in arrays `lmn` and `lmx` respectively. It then iterates through these arrays to adjust their values based on specific conditions, ensuring that `lmn` is non-decreasing and `lmx` is non-increasing. Finally, it calculates and returns `ans`, which is the sum of \((\text{lmx}[j] - \text{lmn}[j]) / 2\) for all valid indices \(j\) from 0 to 200007 where \(\text{lmn}[j] < \text{lmx}[j]\).

#State of the program right berfore the function call: `n` is an integer representing the number of black tokens, and `stdin` is an object providing input data access. For each black token, `dat` contains pairs of integers `(x, y)` representing the x and y coordinates of the token's initial position, with the constraint that `1 <= n <= 10^5` and `-10^5 <= x, y <= 10^5`. The initial positions of black tokens are distinct.
def func_2():
    n = int(stdin.readline())
    dat = map(int, stdin.read().split(), repeat(10, 2 * n))
    s = [[], []]
    for i in xrange(n):
        x, y = dat[i * 2:i * 2 + 2]
        
        s[x + y & 1].append((-x + y, x + y))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer; `dat` is a map object containing exactly `2 * n` elements; `s` is a list where each sublist `s[0]` and `s[1]` contains exactly `n` elements. Each element in `s[x + y & 1]` is of the form `(-x + y, x + y)` where `x` is the value at key `i * 2` in `dat` and `y` is the value at key `i * 2 + 1` in `dat`, and `i` ranges from `0` to `n - 1`.
    print(func_1(s[0]) + func_1(s[1]))
#Overall this is what the function does:The function `func_2` accepts two parameters: `n`, an integer representing the number of black tokens, and `stdin`, an input data access object providing coordinate data for the tokens. The function reads the coordinates of `n` black tokens from `stdin`, processes these coordinates by categorizing them into two lists based on the parity of the sum of their coordinates, and then calls another function `func_1` on each list, summing the results and printing the total. If `n` is less than 1 or greater than \(10^5\), or if the coordinate values exceed \([-10^5, 10^5]\), the function will still read the data and proceed. However, it does not handle invalid inputs explicitly.

