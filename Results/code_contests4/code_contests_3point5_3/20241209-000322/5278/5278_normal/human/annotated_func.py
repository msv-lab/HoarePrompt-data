#State of the program right berfore the function call: n and k are positive integers such that 1 <= n <= 100,000 and 1 <= k <= 100,000. Each w_i is a positive integer such that 1 <= w_i <= 10,000.**
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
        
    #State of the program after the  for loop has been executed: `n` and `k` are positive integers, `w` is a list with `n` elements, `maxW` is the maximum value in the list `w`, `sumW` is the sum of all elements in `w`, `i` is equal to `n-1`, `num` is the last input value entered
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
                
            #State of the program after the loop has been executed: `truckCnt`, `i`, `loadings`, `n`, `middle`, `k`, `minP` are positive integers. If `k` is less than `truckCnt + 1`, then `left` is assigned `middle + 1`. If `k` is greater than or equal to `truckCnt + 1`, then `right` is assigned `middle - 1`.
        #State of the program after the if-else block has been executed: *`n` and `k` are positive integers, `w` is a list with `n` elements, `maxW` is the maximum value in the list `w`, `sumW` is the sum of all elements in `w`, `i` is equal to `n-1`, `num` is the last input value entered, `minP` is 0. If `n` is not equal to `k`, `minP` is assigned the maximum value in the list `w`. If `k` is less than `truckCnt + 1`, then `left` is assigned `middle + 1`. If `k` is greater than or equal to `truckCnt + 1`, then `right` is assigned `middle - 1`.
    #State of the program after the if-else block has been executed: *`n` and `k` are positive integers, `w` is a list with `n` elements, `maxW` is the maximum value in the list `w`, `sumW` is the sum of all elements in `w`, `i` is equal to `n-1`, `num` is the last input value entered, `minP` will be equal to `sumW` if `k` is equal to 1. Otherwise, if `n` is not equal to `k`, `minP` is assigned the maximum value in the list `w`. If `k` is less than `truckCnt + 1`, then `left` is assigned `middle + 1`. If `k` is greater than or equal to `truckCnt + 1`, then `right` is assigned `middle - 1`.
#Overall this is what the function does:The function `func` reads input values for `n` and `k`, then reads `n` integers into a list `w`. It calculates the minimum possible value `minP` based on certain conditions depending on the values of `n` and `k`. The function uses binary search to determine `minP` in specific scenarios. The function does not explicitly accept any parameters but operates on predefined or global variables.

