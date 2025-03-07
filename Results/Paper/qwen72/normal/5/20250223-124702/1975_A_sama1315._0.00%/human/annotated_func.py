#State of the program right berfore the function call: arr is a list of positive integers such that 2 <= len(arr) <= 50.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of positive integers such that 2 <= len(arr) <= 50, and there exists at least one pair of consecutive elements in `arr` where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list `arr` of positive integers with a length between 2 and 50. It returns 'Yes' if the list is sorted in non-decreasing order (i.e., each element is less than or equal to the next element). Otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 2 <= n <= 50, and arr is a list of n integers such that 1 <= arr[i] <= 10^6.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n` is the integer value of `data[index - 1]`, `arr` is a list of `n` integers such that 1 <= arr[i] <= 10^6, `data` is a list of strings obtained by splitting the input read from `sys.stdin`, `index` is equal to the length of `data`, `results` is a list containing `t` elements, each element is the result of calling `func_1` on a list of integers.
    print('\n'.join(results))
    #This is printed: [result_1]
    #[result_2]
    #...
    #[result_t] (where each [result_i] is the result of calling `func_1` on a list of integers, and there are `t` such results)
#Overall this is what the function does:The function reads input from `sys.stdin`, processes it to extract multiple sets of integers, and applies a function `func_1` to each set. It then prints the results of these function calls, one per line. The function does not return any value. After the function concludes, `t` is an integer between 1 and 1000, `n` is the last integer value read from the input, `arr` is the last list of integers read from the input, `data` is a list of strings obtained by splitting the input, `index` is equal to the length of `data`, and `results` is a list containing `t` elements, each being the result of calling `func_1` on a list of integers.

