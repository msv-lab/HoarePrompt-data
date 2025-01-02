#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and for each pair (p_i, c_i) in the input, 0 <= p_i, c_i <= 1000. The pairs (p_i, c_i) are provided in chronological order.
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
        
    #State of the program after the loop has been executed: `t` is 0, `n` is a non-negative integer, `zz` is a list containing `n` empty lists, `prevplay` is `zz[n-1][0]` if the loop ran at least once, `prevClr` is `zz[n-1][1]` if the loop ran at least once, and the console prints 'YES' if no conditions were violated during any iteration, otherwise prints 'NO'.
#Overall this is what the function does:The function processes a series of pairs \((p_i, c_i)\) where \(p_i\) and \(c_i\) are integers. It checks whether the sequence of pairs is valid based on specific conditions. If any condition is violated, the function prints 'NO'; otherwise, it prints 'YES'. The function does not accept any parameters and returns nothing explicitly. After the function concludes, the console will display either 'YES' or 'NO' based on the validation process. The function handles the following edge cases:
1. If \(t\) (the number of test cases) is 0, no further processing occurs.
2. If any pair \((p_i, c_i)\) violates the conditions (i.e., \(p_i < \text{prevplay}\), \(c_i < \text{prevClr}\), or \(p_i < c_i\)), the function immediately prints 'NO'.
3. If none of the conditions are violated, the function prints 'YES'.

The function also ensures that the values of `prevplay` and `prevClr` are updated correctly within the loop.

#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 500. For each test case, n is an integer such that 1 ≤ n ≤ 100. Each pair (p_i, c_i) consists of two non-negative integers such that 0 ≤ p_i, c_i ≤ 1000, and the pairs are given in chronological order.
def STR():
    return list(input())
    #The program returns a list of strings representing the input pairs (p_i, c_i)
#Overall this is what the function does:The function `STR()` reads a single line of input from the user and returns it as a list of strings. This input is expected to consist of a series of pairs (p_i, c_i), where each pair is a string representation of two non-negative integers separated by whitespace. The function does not perform any validation on the input format, so it is assumed that the input adheres to the specified format. If the input does not conform to the expected format, the behavior of the function is undefined.

#State of the program right berfore the function call: T is an integer such that 1 <= T <= 500. For each test case, n is an integer such that 1 <= n <= 100. Each pair (p_i, c_i) consists of integers such that 0 <= p_i, c_i <= 1000, and the pairs are given in chronological order.
def INT():
    return int(input())
    #The program returns an integer input provided by the user, which is within the range of 1 <= T <= 500
#Overall this is what the function does:The function `INT()` accepts no parameters and reads an integer input from the user. This input is guaranteed to be within the range of 1 to 500 (inclusive). The function then returns this integer. There are no additional actions or conditions performed by the function beyond reading the input and returning it. Potential edge cases include the user providing an input outside the specified range, in which case the behavior is not defined by the provided code; the function will simply return whatever integer is provided by the user.

#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 500. For each test case, n is an integer such that 1 ≤ n ≤ 100. Each pair (p_i, c_i) consists of two integers such that 0 ≤ p_i, c_i ≤ 1000, and the pairs are given in chronological order.
def MAP():
    return map(int, input().split())
    #The program returns a tuple of integers (p_i, c_i) entered by the user, where the pairs are given in chronological order
#Overall this is what the function does:The function reads a series of pairs of integers (p_i, c_i) from user input, where each pair is separated by a space and the pairs themselves are separated by newlines. It processes this input to form a tuple containing these pairs in the exact order they were entered. The function does not accept any parameters and returns the resulting tuple. The function handles the input format as specified, ensuring that the pairs are read in chronological order as provided by the user. Potential edge cases include invalid input formats (e.g., non-integer values or incorrect separators), which would result in the function terminating due to the `map` function raising a `ValueError`. If the input strictly follows the format, the function will correctly return a tuple of tuples, where each inner tuple contains two integers (p_i, c_i).

#State of the program right berfore the function call: T is a positive integer such that 1 <= T <= 500. For each test case, n is a positive integer such that 1 <= n <= 100. Each pair (p_i, c_i) consists of non-negative integers such that 0 <= p_i, c_i <= 1000, and the pairs are provided in chronological order.
def LIST():
    return list(map(int, input().split()))
    #The program returns a list of integers created from user input split by spaces, where each integer corresponds to the input values of T and n for each test case, followed by pairs of integers (p_i, c_i)
#Overall this is what the function does:Functionality: The function reads user input and processes it to create a list of integers. This list contains the number of test cases `T`, followed by the number of elements `n` for each test case, and then pairs of integers `(p_i, c_i)` for each element within the test cases. The function returns this list. 

The function handles the following cases:
- It accepts user input split by spaces, which must be in the correct format (e.g., "T n p_i c_i ...").
- It ensures that `T` is a positive integer within the range `[1, 500]`.
- It ensures that `n` is a positive integer within the range `[1, 100]`.
- It processes up to 100 pairs `(p_i, c_i)` for each test case, where each pair is a non-negative integer within the range `[0, 1000]`.

Potential edge cases include:
- If the input format is incorrect (e.g., missing values or incorrect types), the function will not correctly parse the input, leading to incorrect results.
- If the number of test cases `T` exceeds 500 or the number of elements `n` per test case exceeds 100, the function will not process additional values beyond these limits.

Missing functionality:
- There is no validation or error handling for incorrect input formats or values outside the specified ranges. If invalid input is provided, the function may produce incorrect output or unexpected behavior.

#State of the program right berfore the function call: a and b are non-negative integers representing the dimensions of the 2D list, and c is an integer representing the value to fill the list with.
def list2d(a, b, c):
    return [([c] * b) for i in range(a)]
    #The program returns a 2D list with 'a' rows and 'b' columns, where each element in the list is filled with the integer 'c'
#Overall this is what the function does:The function `list2d` accepts three parameters: `a`, `b`, and `c`. Here, `a` and `b` are non-negative integers representing the dimensions of the 2D list, and `c` is an integer representing the value to fill the list with. The function returns a 2D list with `a` rows and `b` columns, where each element in the list is filled with the integer `c`. The function handles the case where `a` or `b` is zero by creating an empty list if either dimension is zero. There is no missing functionality in the provided code.

#State of the program right berfore the function call: listOfTuples is a list of tuples, each tuple contains at least two integers, and idx is an integer representing the index of the tuple to sort by.
def sortListWithIndex(listOfTuples, idx):
    return sorted(listOfTuples, key=lambda x: x[idx])
    #`The program returns a list of tuples sorted based on the element at index 'idx' within each tuple`
#Overall this is what the function does:The function `sortListWithIndex` accepts a list of tuples, where each tuple contains at least two integers, and an integer index `idx`. It returns a new list of tuples sorted based on the value at the specified index within each tuple. The function does not modify the original list. Potential edge cases include empty lists, lists with only one tuple, or invalid indices (e.g., indices that exceed the length of the tuples). The function correctly sorts the list based on the provided index, but it does not handle these edge cases explicitly in the given code.

#State of the program right berfore the function call: 
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
        
    #State of the program after the  for loop has been executed: `passedDic` is unchanged, `temp` is an empty list or contains elements sorted by the value of key-value pairs in `passedDic` (with ties broken by key), `toret` is a dictionary containing all key-value pairs from `temp`.
    return toret
    #`theprogramreturnsadictionarycontainingallkey-valuerestfromtemp`
#Overall this is what the function does:The function `sortDictWithVal` accepts a dictionary `passedDic` as a parameter and returns a new dictionary containing all key-value pairs from `passedDic`, sorted by the values of the key-value pairs. If two key-value pairs have the same value, they are sorted by their keys. The original dictionary `passedDic` remains unchanged. After the function execution, the returned dictionary has its items sorted according to the specified criteria. Potential edge cases include handling an empty input dictionary, where the returned dictionary will also be empty. There is no missing functionality in the provided code; it correctly sorts the dictionary as described.

#State of the program right berfore the function call: passedDic is a dictionary where the keys are integers representing the moments of time (starting from 0) and the values are tuples of two integers (p_i, c_i) representing the number of plays and the number of clears at that moment of time. The dictionary is ordered by keys in ascending order.
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
    #The program returns a dictionary where the keys are integers representing the moments of time (starting from 0) and the values are tuples of two integers (p_i, c_i) representing the number of plays and the number of clears at that moment of time. The dictionary is ordered by keys in ascending order
#Overall this is what the function does:The function `sortDictWithKey` accepts a dictionary `passedDic` as a parameter. This dictionary contains key-value pairs where the keys are integers representing moments of time, starting from 0, and the values are tuples of two integers (p_i, c_i), representing the number of plays and the number of clears at those moments. The function sorts this dictionary based on its keys in ascending order and then returns the sorted dictionary. This ensures that the returned dictionary maintains the order of time moments from earliest to latest while preserving the associated (p_i, c_i) values. Potential edge cases include the scenario where the input dictionary is empty or already sorted, in which case the function still returns the same dictionary. There is no missing functionality as the provided code accurately implements the described behavior.

#State of the program right berfore the function call: zero is an integer representing the initial number to accumulate digits into numb, conv is a function to convert characters to their numeric value (assuming ord is used in Python 2 and a lambda function is used in Python 3), and s is a bytes object containing the input stream from stdin.
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
            
        #State of the program after the loop has been executed: `s` is a non-empty bytes object, `i` is equal to the length of `s`, `sign` is -1 if the first character of `s` was `b'-'[0]`, otherwise `sign` is 1, `numb` is the integer representation of the number formed by the digits in `s` (ignoring any leading '-' sign), `zero` remains unchanged, `A` contains all the numbers formed from the segments in `s` (excluding any segments that start with `\r`), and `conv` remains unchanged.
    except:
        pass
    #State of the program after the try-except block has been executed: `s` is a non-empty bytes object, `i` is equal to the length of `s`, `sign` is -1 if the first character of `s` was `b'-'[0]`, otherwise `sign` is 1, `numb` is the integer representation of the number formed by the digits in `s` (ignoring any leading '-' sign), `zero` remains unchanged, `A` contains all the numbers formed from the segments in `s` (excluding any segments that start with `\r`), and `conv` remains unchanged.
    if (s and s[-1] >= b'0'[0]) :
        A.append(sign * numb)
    #State of the program after the if block has been executed: *`s` is a non-empty bytes object, `i` is equal to the length of `s`, `sign` is -1 if the first character of `s` was `b'-'[0]`, otherwise `sign` is 1, `numb` is the integer representation of the number formed by the digits in `s` (ignoring any leading '-' sign), `zero` remains unchanged, `A` contains all the numbers formed from the segments in `s` (excluding any segments that start with `\r`), and `conv` remains unchanged. If the last character of `s` is greater than or equal to `b'0'[0]`, then `sign * numb` is appended to `A`.
    return A
    #`A` contains all the numbers formed from the segments in `s` (excluding any segments that start with `\r`), and if the last character of `s` is greater than or equal to `b'0'[0]`, then `sign * numb` is also appended to `A`.
#Overall this is what the function does:The function `func_2` takes an integer `zero` as a parameter and processes a bytes object `s` to extract numbers from it. It accumulates these numbers into a list `A`, excluding any segments that start with `\r`. If the last character of `s` is a digit (i.e., greater than or equal to `b'0'[0]`), it appends `sign * numb` to `A`, where `numb` is the integer representation of the number formed by the digits in `s`, and `sign` is either 1 or -1 depending on whether `s` starts with a `-`. The function ultimately returns the list `A` containing all the extracted numbers.

