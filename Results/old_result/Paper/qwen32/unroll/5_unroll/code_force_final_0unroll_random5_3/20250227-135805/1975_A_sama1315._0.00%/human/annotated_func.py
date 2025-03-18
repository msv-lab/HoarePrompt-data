#State of the program right berfore the function call: arr is a list of positive integers with length n such that 2 <= n <= 50.
def func_1(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) :
        return 'Yes'
        #The program returns 'Yes'
    #State: `arr` is a list of positive integers with length `n` such that 2 <= `n` <= 50, and there exists at least one pair of consecutive elements in `arr` where the first element is greater than the second element.
    return 'No' if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else 'Yes'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list of positive integers `arr` with a length between 2 and 50. It returns 'Yes' if the list is sorted in non-decreasing order, and 'No' otherwise.

#State of the program right berfore the function call: arr is a list of n positive integers where n is an integer such that 2 <= n <= 50, and each element in arr is an integer such that 1 <= a_i <= 10^6.
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
        
    #State: `arr` is the last list of integers obtained from `data` in the last iteration; `index` is the position right after the last list of integers in `data`; `results` is a list of results from `func_1(arr)` for each iteration; `t` and `data` remain unchanged.
    print('\n'.join(results))
    #This is printed: result1\nresult2\n...\nresultN (where result1, result2, ..., resultN are the elements of the results list, each separated by a newline character)
#Overall this is what the function does:The function `func_2` reads multiple test cases from standard input, where each test case consists of an integer `n` followed by a list of `n` positive integers. It processes each test case by calling `func_1` with the list of integers and collects the results. Finally, it prints the results, each on a new line.

