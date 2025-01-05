#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5
    ) + 1) if n % i == 0)))
    #The program returns a set containing all the factors of the non-negative integer 'n'
#Overall this is what the function does:The function func_1 accepts a non-negative integer n and returns a set containing all the factors of n. The function uses a set comprehension with a conditional statement to generate the set of factors. However, it is important to note that the current implementation does not handle the case when n is 0, which should ideally return an empty set since 0 has no factors.

#State of the program right berfore the function call: n is a positive integer.**
def func_2(n):
    arr = [1] * n
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i] == 1:
            for j in range(i, n, i):
                arr[j] = i
        
    #State of the program after the  for loop has been executed: `n` is a positive integer greater than or equal to 5, `arr` is an array of length at least `n` with each element being a prime number, `i` is the largest prime number less than or equal to n. If `arr[i] == 1`, then for all valid `j` in the range `i` to `n` with step `i`, `arr[j]` is updated with the value of `i`.
    return arr
    #The program returns the updated array `arr` after the specified updates have been made based on the conditions described.
#Overall this is what the function does:The function accepts a positive integer n and updates an array arr based on prime number calculations. It initializes the array with 1s, then iterates through a range of numbers to find prime numbers and updates the array accordingly. The function returns the updated array arr.

#State of the program right berfore the function call: **Precondition**: **arr is a list of tuples where each tuple contains two integers n and k (2 <= k <= n <= 3 * 10^5, k is even), and a string s of length n composed of characters 0, 1, and ?.**
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
        
    #State of the program after the  for loop has been executed: All elements in the array `arr` will be either equal to a non-'?' element or '?'. The loop will update the array `arr` such that each group of `k` consecutive elements will either contain the same non-'?' element or be filled with '?' characters. If the loop does not execute, the initial state will remain unchanged.
    dic = {'1': 0, '0': 0, '?': 0}
    for i in range(k):
        dic[arr[i]] += 1
        
    #State of the program after the  for loop has been executed: `dic` is {'1': x, '0': y, '?': z} where x is the number of occurrences of '1' in arr, y is the number of occurrences of '0' in arr, z is the number of occurrences of '?' in arr
    if (dic['1'] != dic['0'] and dic['?'] != abs(dic['1'] - dic['0'])) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *`dic` is {'1': x, '0': y, '?': z} where x is the number of occurrences of '1' in arr, y is the number of occurrences of '0' in arr, z is the number of occurrences of '?' in arr. Either dic['1'] is equal to dic['0'] or dic['?'] is equal to abs(dic['1'] - dic['0'])
    return True
    #The program returns True
#Overall this is what the function does:Functionality: The function `func_3` takes two parameters, `arr` and `k`, where `arr` is a list of tuples containing integers and a string with specific constraints, and `k` is an even integer. The function iterates through `arr` and modifies it based on certain conditions. After the execution, the function returns True if specific conditions are met, otherwise, it returns False. The functionality includes updating `arr` so that groups of `k` consecutive elements contain the same non-'?' element or are filled with '?' characters. However, the actual code does not cover all potential cases described in the annotations, so additional edge cases and missing functionality need to be considered for a complete summary.

#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n <= 3*10^5 and k is even. s is a string of length n consisting of characters 0, 1, and ?.**
def func_4():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        arr = list(input())
        
        if not func_3(arr, k):
            func_5('NO')
        else:
            func_5('YES')
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers in the range [2, 3*10^5] and `k` is even. `s` is a string of length `n` consisting of characters 0, 1, and ?. `arr` is a list containing the characters input by the user. The values of `n`, `k`, `s`, and `arr` remain unchanged after the loop executes for any number of times.
#Overall this is what the function does:The function `func_4` reads inputs for `n`, `k`, and a string `s`, then iterates through a loop based on the number of test cases. Within each iteration, it checks if the function `func_3` applied to the input string `arr` and integer `k` returns True or False. Depending on the result, it calls the function `func_5` with either 'NO' or 'YES'. The function does not have a specific return value, but it operates within the constraints provided for `n`, `k`, and `s`.

#State of the program right berfore the function call: 
def func_5():
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `sep` is assigned the value popped from kwargs with a default of ' ', `file` is assigned the value popped from kwargs with a default of `sys.stdout`, `args` contains elements, all elements in `args` are written to the `file` separated by `sep`, `at_start` is False
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`sep` is assigned the value popped from kwargs with a default of ' ', `file` is assigned the value popped from kwargs with a default of `sys.stdout`, `args` contains elements, all elements in `args` are written to the `file` separated by `sep`, `at_start` is False, kwargs has a value popped with a default of '\n', and the condition kwargs.pop('flush', False) is True.
#Overall this is what the function does:The function `func_5` does not accept any parameters and does not return any value. It executes a sequence of operations where elements in `args` are written to a file separated by `sep`. It also writes an end character specified in the `kwargs`. Additionally, if the `flush` key is set to True in `kwargs`, it flushes the file.

#State of the program right berfore the function call: x is an integer representing the number of test cases, y is a list of tuples where each tuple contains two integers n and k (2 ≤ k ≤ n ≤ 3 ⋅ 10^5, k is even) and a string s of length n composed only of characters 0, 1, and ?.**
def func_6(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` and `y` have been swapped multiple times until `y` reaches 0, at which point the loop terminates. The final values of `x` and `y` depend on the initial values of the list of tuples `y` and the remainders of the division operations.
    return x
    #The program returns the final value of variable x after swapping x and y multiple times until y reaches 0. The final values of x and y depend on the initial values of the list of tuples y and the remainders of the division operations.
#Overall this is what the function does:The function `func_6` accepts two parameters: an integer `x` representing the number of test cases, and a list `y` of tuples. Each tuple in the list contains two integers `n` and `k` (where 2 ≤ k ≤ n ≤ 3 ⋅ 10^5, and k is even) and a string `s` of length `n` composed only of characters 0, 1, and ?. 

After executing the function body, the program swaps the values of `x` and `y` multiple times until `y` reaches 0. The final values of `x` and `y` depend on the initial values of the list of tuples `y` and the remainders of the division operations. The function then returns the final value of variable `x`.

Therefore, the functionality of the function `func_6` is to perform multiple swaps between `x` and `y` until `y` reaches 0 based on the initial values and remainders of division operations, and finally return the resulting value of `x`.

