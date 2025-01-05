#State of the program right berfore the function call: n is a positive integer, and each company description consists of an integer m_i followed by m_i salaries that are positive integers not exceeding 10^9.**
def func():
    n = int(raw_input())
    arr = []
    maxval = 0
    arr2 = []
    for i in xrange(n):
        arr1 = list(map(int, raw_input().split()))
        
        temp = 0
        
        for j in xrange(1, arr1[0]):
            temp = max(temp, arr1[j])
        
        arr.append(temp)
        
        arr2.append(arr1[0])
        
        maxval = max(arr[i], maxval)
        
    #State of the program after the  for loop has been executed: Output State: `n` is a positive integer, `arr` contains the maximum values from each `arr1`, `arr2` contains the number of salaries in each `arr1`, `maxval` is the maximum value among all the maximum values in `arr`, `i` is equal to `n`, `arr1` is a list of integers obtained by mapping input split by spaces to integers where `arr1[0]` is greater than 1, `temp` is the maximum value in `arr1` after all iterations of the loop have finished.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: Output State: `n` is a positive integer, `arr` contains the maximum values from each `arr1`, `arr2` contains the number of salaries in each `arr1`, `maxval` is the maximum value among all the maximum values in `arr`, `i` is equal to `n`, `arr1` is a list of integers obtained by mapping input split by spaces to integers where `arr1[0]` is greater than 1, `temp` is the maximum value in `arr1` after all iterations of the loop have finished, `ans` is equal to the sum of `(maxval - arr[i]) * arr2[i]` for all elements in `arr` after the loop finishes.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` as input, then iterates `n` times to process company descriptions. Each company description consists of an integer `m_i` followed by `m_i` salaries. The function calculates the maximum salary for each company description and the total cost difference between the maximum salary and the maximum salary across all companies. The final result is printed as the output. The function does not accept any parameters explicitly but relies on user input during execution.

