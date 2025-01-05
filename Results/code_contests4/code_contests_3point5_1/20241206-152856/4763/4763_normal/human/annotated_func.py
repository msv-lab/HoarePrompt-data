#State of the program right berfore the function call: n is an integer representing the number of test cases. Each test case consists of two integers n and k where 2 ≤ k ≤ n ≤ 3 ⋅ 10^5 and k is even. The string s of length n consists of only 0, 1, and ?.**
def func_1(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5
    ) + 1) if n % i == 0)))
    #The program returns the set of divisors of 'n' that are factors of 'n'
#Overall this is what the function does:The function `func_1` accepts an integer `n`, representing the number of test cases. Each test case consists of two integers n and k where 2 ≤ k ≤ n ≤ 3 ⋅ 10^5 and k is even. The string s of length n consists of only 0, 1, and ?. The function then returns the set of divisors of 'n' that are factors of 'n'.

#State of the program right berfore the function call: n is a positive integer.**
def func_2(n):
    arr = [1] * n
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i] == 1:
            for j in range(i, n, i):
                arr[j] = i
        
    #State of the program after the  for loop has been executed: `n` is at least 5, `arr` is an array of length at least 5 with values [1, 1, 2, 3, 2, 5, 2, ..., 2], `i` is `n
    return arr
    #The program returns the array 'arr' of length at least 5 with values [1, 1, 2, 3, 2, 5, 2, ..., 2]
#Overall this is what the function does:The function `func_2` accepts a positive integer `n` and generates an array `arr` of length at least 5 filled with specific values. The function populates the array based on a certain pattern, where each element represents a factor of its index. The pattern is implemented using nested loops, assigning factors to corresponding elements in the array. The function then returns the generated array `arr`. It is important to note that the pattern generation logic is not explicitly defined in the annotations, so the specific pattern followed by the array values is not detailed.

#State of the program right berfore the function call: arr is a list of tuples where each tuple contains two integers n and k (2 ≤ k ≤ n ≤ 3 ⋅ 10^5, k is even) and a string s of length n composed only of characters 0, 1, and ?.**
def func_3(arr, k):
    for i in range(len(arr)):
        if arr[i] != '?':
            for j in range(i, len(arr), k):
                if arr[j] != arr[i] and arr[j] != '?':
                    return False
                if arr[j] == '?':
                    arr[j] = arr[i]
        else:
            vis = set([])
            for j in range(i, len(arr), k):
                if arr[j] != '?':
                    vis.add(arr[j])
            if len(vis) == 2:
                return False
            if len(vis) == 1:
                put = list(vis)[0]
                for j in range(i, len(arr), k):
                    arr[j] = put
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, the values of the variables will depend on the initial state of the input list arr. If the loop does not execute, the values of n, k, and s will remain the same as the initial state. If the loop executes, the elements of arr will be updated according to the conditions outlined in the loop code. All elements in arr between index i and len(arr) will either be equal to arr[i] or '?'. If arr[i] is not equal to '?', then all elements in arr will be updated to be the same as arr[i]. If arr[i] is '?', then all elements in arr will be updated to be the same as the last unique non-'?' value in arr. Additionally, if len(vis) is equal to 1, all elements in arr will be updated to be the same as the only element in vis. If len(vis) is equal to 2, the program will return False.
    dic = {'1': 0, '0': 0, '?': 0}
    for i in range(k):
        dic[arr[i]] += 1
        
    #State of the program after the  for loop has been executed: `dic` is {'1': k, '0': 0, '?': 0}, `i` is k-1, `k` is a non-negative integer
    if (dic['1'] != dic['0'] and dic['?'] != abs(dic['1'] - dic['0'])) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *`dic` is {'1': k, '0': 0, '?': 0}, `i` is k-1, `k` is a non-negative integer. The condition (dic['1'] != dic['0'] and dic['?'] != abs(dic['1'] - dic['0'])) is false
    return True
    #The program returns True
#Overall this is what the function does:The function `func_3` takes two parameters: `arr`, a list of tuples where each tuple contains two integers n and k, and a string s of length n composed of 0, 1, and ?, and `k`, an even integer. The function iterates through the elements of arr and updates them based on certain conditions. It returns False in multiple cases specified by the annotations, and finally returns True if none of the previous conditions are met. The function has multiple return points based on the input parameters and the conditions checked during execution.

#State of the program right berfore the function call: **
def func_4():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        arr = list(input())
        
        if not func_3(arr, k):
            func_5('NO')
        else:
            func_5('YES')
        
    #State of the program after the  for loop has been executed: At the end of the loop, `n` and `k` will hold the values of the last input split, `arr` will contain the list of characters from the last input, and the function `func_5` will be called with either 'NO' or 'YES' based on the return value of `func_3(arr, k)` for the last input.
#Overall this is what the function does:The function `func_4` iterates over a range of inputs, where for each iteration, it reads input values for `n`, `k`, and a list of characters `arr`. It then calls `func_3` with `arr` and `k`, and based on the return value, calls `func_5` with either 'NO' or 'YES'. The function does not have specific input constraints or return values.

#State of the program right berfore the function call: **
def func_5():
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `sep` is ' ', `file` is updated with the string representations of all elements in `args` separated by `sep`, `at_start` is False, `args` is not empty
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`sep` is ' ', `file` is updated with the string representations of all elements in `args` separated by `sep`, `at_start` is False, `args` is not empty. If the 'flush' key is present in `kwargs` and its value is True, then it is removed from `kwargs`.
#Overall this is what the function does:The function func_5 does not accept any parameters and iterates over elements in `args`, writing their string representations to the output `file` separated by the value of `sep`. It then writes the value of 'end' from `kwargs` to `file` and flushes the file if the 'flush' key is present and set to True in `kwargs`.

#State of the program right berfore the function call: x is an integer representing the number of test cases, y is a list of tuples where each tuple contains two integers n and k (2 ≤ k ≤ n ≤ 3 ⋅ 10^5, k is even) and a string s of length n composed only of characters 0, 1, and ?.**
def func_6(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` is the greatest common divisor (GCD) of the initial `x` and `y`, `y` is 0
    return x
    #The program returns the greatest common divisor (GCD) of the initial values of 'x' and 'y', where 'y' is 0
#Overall this is what the function does:The function func_6 accepts two parameters, x and y, where x is an integer representing the number of test cases and y is a list of tuples. It calculates the greatest common divisor (GCD) of the initial values of 'x' and 'y' iteratively until 'y' becomes 0, and then returns the GCD.

