#State of the program right berfore the function call: arr is a list of n positive integers, where n is an integer such that 2 <= n <= 50. Each element a_i in arr satisfies 1 <= a_i <= 10^6.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of `n` positive integers, where `n` is an integer such that 2 <= `n` <= 50. Each element `a_i` in `arr` satisfies 1 <= `a_i` <= 10^6. The list `arr` is not sorted in non-decreasing order, meaning there exists at least one index `i` such that `arr[i]` > `arr[i + 1]`.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` checks if the input list `arr` of positive integers is sorted in non-decreasing order. If the list is sorted, it returns 'Yes'; otherwise, it returns 'No'.

#State of the program right berfore the function call: arr is a list of n positive integers where n is an integer such that 2 <= n <= 50, and each element in arr satisfies 1 <= a_i <= 10^6.
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        arr = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(arr)
        
        results.append(result)
        
    #State: `arr` is the last list of integers processed, `data` is unchanged, `index` is `1 + 2 * t + sum(n_1, n_2, ..., n_t)`, `t` is `0`, `results` is a list containing the results of `func_1(arr)` for each of the `t` iterations.
    print('\n'.join(results))
    #This is printed: (an empty string)
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a list of `n` positive integers. For each test case, it computes a result using the `func_1` function and prints the results for all test cases, each on a new line.

