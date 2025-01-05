#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 100,000 and 1 <= k <= 100,000. Each w_i is an integer such that 1 <= w_i <= 10,000.**
def func():
    n, k = [int(val) for val in raw_input().split(' ')]
    w = []
    maxW = sumW = 0
    for i in range(n):
        num = int(raw_input())
        
        sumW += num
        
        w.append(num)
        
        if maxW < num:
            maxW = num
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `k` is an integer such that 1 <= k <= 100,000, `maxW` is equal to the maximum value of all input integers, `sumW` is the sum of all input integers, `w` contains all input integers, `i` is equal to n-1
    minP = 0
    if (1 == k) :
        minP = sumW
    else :
        if (n == k) :
            minP = maxW
        else :
            left = maxW
            right = 100000 * 10000
            while left <= right:
                middle = (left + right) // 2
                
                truckCnt = i = loadings = 0
                
                while i < n:
                    loadings += w[i]
                    if middle < loadings:
                        truckCnt += 1
                        if k < truckCnt + 1:
                            break
                        loadings = w[i]
                    i += 1
                
                if truckCnt + 1 <= k:
                    minP = middle
                
                if k < truckCnt + 1:
                    left = middle + 1
                else:
                    right = middle - 1
                
            #State of the program after the loop has been executed: 'loadings' is the sum of all input integers, 'middle' is the value where 'truckCnt' plus 1 is equal to 'k', 'truckCnt' is the number of times 'middle < loadings' was true, 'n' remains the same, 'i' is equal to n, 'minP' is equal to the 'middle' value where 'truckCnt' plus 1 is equal to k, 'left' is assigned the value of 'middle' plus 1, 'right' is assigned the value of 'middle' minus 1
        #State of the program after the if-else block has been executed: *`n` is greater than 0, `k` is an integer such that 1 <= k <= 100,000, `maxW` is equal to the maximum value of all input integers, `sumW` is the sum of all input integers, `w` contains all input integers, `i` is equal to n-1, `minP` is 0. If n == k, then `minP` is equal to the maximum value of all input integers. Otherwise, 'loadings' is the sum of all input integers, 'middle' is the value where 'truckCnt' plus 1 is equal to 'k', 'truckCnt' is the number of times 'middle < loadings' was true, 'n' remains the same, 'i' is equal to n, 'minP' is equal to the 'middle' value where 'truckCnt' plus 1 is equal to k, 'left' is assigned the value of 'middle' plus 1, 'right' is assigned the value of 'middle' minus 1.
    #State of the program after the if-else block has been executed: *n is greater than 0, k is an integer such that 1 <= k <= 100,000, maxW is equal to the maximum value of all input integers, sumW is the sum of all input integers, w contains all input integers, i is equal to n-1. If n == k, then minP is equal to the maximum value of all input integers. Otherwise, minP is updated based on the conditions mentioned in the else part.
#Overall this is what the function does:The function `func` reads input integers `n` and `k`. It then reads `n` more integers and calculates the sum `sumW`, the maximum value `maxW` among the inputs, and constructs a list `w` with the input integers. Based on specific conditions, it either updates the value of `minP` or performs a binary search algorithm to determine the value of `minP`. The function does not explicitly return any value.

