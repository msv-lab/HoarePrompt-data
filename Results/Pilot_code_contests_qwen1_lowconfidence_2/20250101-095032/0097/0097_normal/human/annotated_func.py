#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100. For each pair (p_i, c_i), p_i and c_i are non-negative integers such that 0 <= p_i, c_i <= 1000, and the pairs are given in chronological order.
def func_1():
    INF = float('inf')
    mod = 10 ** 9 + 7
    t = INT()
    while t != 0:
        n = INT()
        
        zz = []
        
        for _ in range(n):
            zz.append(LIST())
        
        prevplay = 0
        
        prevClr = 0
        
        flag = 0
        
        for i in range(n):
            if zz[i][0] < prevplay or zz[i][1] < prevClr or zz[i][0] < zz[i][1]:
                flag = 1
                break
            if zz[i][1] > prevClr:
                temp = zz[i][1] - prevClr
                temp1 = zz[i][0] - prevplay
                if temp > temp1:
                    flag = 1
                    break
            prevplay = zz[i][0]
            prevClr = zz[i][1]
        
        if flag == 1:
            print('NO')
        else:
            print('YES')
        
        t -= 1
        
    #State of the program after the loop has been executed: `t` is 0, `flag` is either 1 or 0 based on the conditions met during the loop iterations, `n` is a non-negative integer, `zz` is a list of `n` elements where each element is a LIST(), `prevplay` is the last value of `zz[i][0]` in the loop, `prevClr` is the last value of `zz[i][1]` in the loop, `INF` is float('inf'), `pairs` (p_i, c_i) are unchanged, `mod` is 1000000007
#Overall this is what the function does:The function processes a series of pairs \((p_i, c_i)\) for a given positive integer \(n\) (where \(1 \leq n \leq 100\)). It checks if the pairs meet certain conditions. Specifically, it verifies that for each pair \((p_i, c_i)\):

1. \(p_i \geq prevplay\) and \(c_i \geq prevClr\).
2. If \(c_i > prevClr\), then \(c_i - prevClr \leq p_i - prevplay\).

If any of these conditions fail for any pair, the function prints 'NO'. Otherwise, it prints 'YES'. After processing all pairs, the function ends.

#State of the program right berfore the function call: T is a positive integer such that 1 <= T <= 500. For each test case, n is a positive integer such that 1 <= n <= 100. Each pair (p_i, c_i) consists of two non-negative integers such that 0 <= p_i, c_i <= 1000, and the pairs are given in chronological order.
def STR():
    return list(input())
    #The program returns a list of strings representing each input pair (p_i, c_i) in chronological order
#Overall this is what the function does:The function `STR()` does not accept any parameters and returns a list of strings. Each string in the list represents a pair `(p_i, c_i)` in chronological order, where `p_i` and `c_i` are non-negative integers. The function reads input from the user using `input()`, which means it expects the user to provide the pairs `(p_i, c_i)` through standard input. The function simply converts the entire input into a list of strings without any further processing or validation.

#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 500. For each test case, n is an integer such that 1 ≤ n ≤ 100. Each pair (p_i, c_i) consists of two non-negative integers such that 0 ≤ p_i, c_i ≤ 1000, and the pairs are given in chronological order.
def INT():
    return int(input())
    #The program returns an integer input from the user, which is within the range of 1 to 500
#Overall this is what the function does:The function `INT()` reads an integer input from the user and ensures that the input is within the range of 1 to 500. If the input is outside this range, the function will repeatedly prompt the user until a valid integer within the specified range is provided. The function accepts no parameters and returns a single integer value that is guaranteed to be between 1 and 500 inclusive.

#State of the program right berfore the function call: T is a positive integer indicating the number of test cases. For each test case, n is a positive integer representing the number of moments Polycarp peeked at the stats. The pairs (p_i, c_i) represent the number of plays and the number of clears at the i-th moment of time, respectively, and they are provided in chronological order. Both p_i and c_i are non-negative integers not exceeding 1000.
def MAP():
    return map(int, input().split())
    #The program returns a map object containing integers parsed from user input, specifically the number of test cases followed by pairs of integers (p_i, c_i) for each test case
#Overall this is what the function does:The function `MAP()` reads input from the user and returns a map object containing integers. Specifically, it first reads the number of test cases, followed by pairs of integers (p_i, c_i) for each test case, where p_i represents the number of plays and c_i represents the number of clears at the i-th moment of time. The function does not perform any calculations or validations on these inputs; it simply parses them into a map object. Potential edge cases include scenarios where the input does not follow the expected format, such as non-integer values or negative numbers. If the input is invalid, the function will still attempt to parse it, which could lead to unexpected behavior or errors downstream.

#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 500. For each test case, n is an integer such that 1 ≤ n ≤ 100. Each line contains two integers p_i and c_i such that 0 ≤ p_i, c_i ≤ 1000, representing the number of plays and the number of clears at the i-th moment of time, respectively, and the pairs are given in chronological order.
def LIST():
    return list(map(int, input().split()))
    #The program returns a list of integers [p_i, c_i] for each line of input, where 0 ≤ p_i, c_i ≤ 1000, representing the number of plays and the number of clears at the i-th moment of time, respectively, and the pairs are given in chronological order
#Overall this is what the function does:The function processes input from the standard input, which consists of multiple lines, each containing two integers \( p_i \) and \( c_i \) separated by a space, where \( 0 \leq p_i, c_i \leq 1000 \). The function returns a list of lists, where each inner list contains the integers \( p_i \) and \( c_i \) from each line of input, maintaining the chronological order of the input. The function accepts no explicit parameters and operates on the standard input. It handles cases where the input format might be incorrect by converting the input into integers using `map(int, input().split())`, ensuring that the values are within the specified range. If the input cannot be converted to integers, the function will raise a `ValueError`.

#State of the program right berfore the function call: a and b are non-negative integers representing the dimensions of the 2D list, and c is the value to fill in every cell of the 2D list.
def list2d(a, b, c):
    return [([c] * b) for i in range(a)]
    #The program returns a 2D list with 'a' rows and 'b' columns, where every cell contains the value 'c'
#Overall this is what the function does:The function `list2d` accepts three parameters: `a`, `b`, and `c`. It returns a 2D list with `a` rows and `b` columns, where every cell contains the value `c`. This is achieved by using a list comprehension that creates `a` rows, each containing a list of `b` elements, all initialized to `c`. The function handles the case where `a` and `b` are non-negative integers. If `a` or `b` were negative, the function would raise an error since the loop in the list comprehension would not execute. However, the function does not explicitly handle non-integer inputs for `a` and `b`, which could lead to unexpected behavior if non-integers are passed. Additionally, the function does not validate that `c` is a valid data type for the cells, although typically `c` would be an integer, float, or string. The final state of the program after the function concludes is that it returns a 2D list with `a` rows and `b` columns, where every cell is filled with the value `c`.

#State of the program right berfore the function call: `listOfTuples` is a list of tuples, where each tuple contains two non-negative integers representing the number of plays and clears at a certain moment. `idx` is an integer that specifies the index (0 or 1) to sort the list of tuples.
def sortListWithIndex(listOfTuples, idx):
    return sorted(listOfTuples, key=lambda x: x[idx])
    #`listOfTuples` sorted based on the idx-th element of each tuple, where each tuple contains two non-negative integers representing the number of plays and clears at a certain moment
#Overall this is what the function does:The function `sortListWithIndex` takes a list of tuples, where each tuple contains two non-negative integers representing the number of plays and clears at a certain moment, and an integer `idx` specifying the index (0 or 1) to sort the list of tuples. It returns a new list that is sorted based on the `idx`-th element of each tuple. If `idx` is 0, the list will be sorted based on the number of plays; if `idx` is 1, the list will be sorted based on the number of clears. The original `listOfTuples` remains unchanged. Edge cases include when `idx` is neither 0 nor 1, in which case the function will still return a sorted list based on the first element of each tuple due to the default behavior of the `sorted` function.

#State of the program right berfore the function call: passedDic is a dictionary where keys are integers representing timestamps (or any monotonically increasing values) and values are tuples (p, c) where p is an integer representing the number of plays and c is an integer representing the number of clears at the corresponding timestamp. The dictionary is not necessarily sorted, but the input pairs (p, c) for each timestamp are valid (i.e., 0 ≤ p, c ≤ 1000) and the timestamps are unique.
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
        
    #State of the program after the  for loop has been executed: `passedDic` is a dictionary where keys are integers representing timestamps and values are tuples (p, c); `temp` is a list of tuples that may be empty; `toret` is a dictionary containing all key-value pairs where the key is the timestamp and the value is the tuple (p, c) from `passedDic` corresponding to that timestamp.
    return toret
    #The program returns `toret` which is a dictionary containing all key-value pairs where the key is the timestamp and the value is the tuple (p, c) from `passedDic` corresponding to that timestamp
#Overall this is what the function does:The function `sortDictWithVal` accepts a dictionary `passedDic` where keys are integers representing timestamps and values are tuples `(p, c)` representing the number of plays and clears at those timestamps. The function first sorts the items of `passedDic` based on the values of the tuples `(p, c)` in ascending order, and if two tuples have the same value, it sorts them based on their keys in ascending order. It then constructs a new dictionary `toret` from the sorted items. The function returns `toret`, which contains all key-value pairs from `passedDic` where the keys are timestamps and the values are tuples `(p, c)` corresponding to those timestamps. The function handles the case where `passedDic` is empty by returning an empty dictionary. No edge cases are explicitly mentioned, but the function correctly handles dictionaries with duplicate values by sorting based on both the value and key.

#State of the program right berfore the function call: passedDic is a dictionary where the keys are non-negative integers representing moments of time and the values are tuples (p, c) where p is the number of plays and c is the number of clears at that moment. The dictionary is assumed to be sorted in ascending order by default.
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
    #The program returns a dictionary where the items are sorted in ascending order by their keys, which are non-negative integers representing moments of time, and the values are tuples (p, c) where p is the number of plays and c is the number of clears at those moments.
#Overall this is what the function does:The function `sortDictWithKey` takes a dictionary `passedDic` as input, where the keys are non-negative integers representing moments of time and the values are tuples `(p, c)` indicating the number of plays `p` and clears `c` at those moments. The function returns a new dictionary where the items are sorted in ascending order by their keys. This means the keys (moments of time) in the returned dictionary are in increasing order, and the values remain tuples `(p, c)` representing the number of plays and clears at those moments. No changes are made to the original dictionary; a new sorted dictionary is created and returned.

#State of the program right berfore the function call: zero is an integer representing the initial value of numb, s is a bytes object containing the input data, and py2 is a boolean indicating whether the code is running in Python 2 (which is assumed to be False in this context).
def func_2(zero):
    conv = ord if py2 else lambda x: x
    A = []
    numb = zero
    sign = 1
    i = 0
    s = sys.stdin.buffer.read()
    try:
        while True:
            if s[i] >= b'0'[0]:
                numb = 10 * numb + conv(s[i]) - 48
            elif s[i] == b'-'[0]:
                sign = -1
            elif s[i] != b'\r'[0]:
                A.append(sign * numb)
                numb = zero
                sign = 1
            
            i += 1
            
        #State of the program after the loop has been executed: `zero` is an integer, `s` is a bytes object containing the input data read from standard input, `py2` is `False`, `conv` is a lambda function that returns its input, `A` is a list containing the accumulated integers based on the input string `s`, `numb` is `zero`, `sign` is `1`, and `i` is the index of the next character in `s` to be processed.
    except:
        pass
    #State of the program after the try-except block has been executed: `zero` is an integer, `s` is a bytes object containing the input data read from standard input, `py2` is `False`, `conv` is a lambda function that returns its input, `A` is a list containing the accumulated integers based on the input string `s`, `numb` is `zero`, `sign` is `1`, and `i` is the index of the next character in `s` to be processed.
    if (s and s[-1] >= b'0'[0]) :
        A.append(sign * numb)
    #State of the program after the if block has been executed: *`zero` is an integer, `s` is a bytes object containing the input data read from standard input, `py2` is `False`, `conv` is a lambda function that returns its input, `A` is a list containing the accumulated integers based on the input string `s` with an additional element `zero`, `numb` is `zero`, `sign` is `1`, and `i` is the index of the next character in `s` to be processed. If the last character of `s` is greater than or equal to the ASCII value of '0', `A` includes an additional element `zero`. Otherwise, the state remains unchanged.
    return A
    #`A` is a list containing the accumulated integers based on the input string `s` with an additional element `zero`. If the last character of `s` is greater than or equal to the ASCII value of '0', `A` includes an additional element `zero`. Otherwise, the state remains unchanged.
#Overall this is what the function does:The function `func_2` accepts an integer `zero` and reads a bytes object `s` from standard input. It processes the bytes object `s` character by character to accumulate integers into a list `A`. During processing, it handles the sign of the number (positive or negative) and ensures that each integer is appended to the list `A`. After the loop, it checks if the last character of `s` is a digit; if so, it appends `zero` to `A`. Finally, it returns the list `A`. Potential edge cases include reading non-digit characters and ensuring that the loop correctly handles the termination condition. The function assumes that the code is running in Python 3, where `py2` is set to `False`.

