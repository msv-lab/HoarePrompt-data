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
        
    #State of the program after the  for loop has been executed: `w` contains all the values of `num` appended in each iteration, `maxW` is the maximum value of all `num` inputs, `sumW` is the sum of all `num` inputs, `i` is equal to `n-1`, where `n` is the total number of iterations, `num` is an integer value obtained from user input in each iteration. If `n` is 0, then `maxW` remains 0, `sumW` remains 0, and `w` remains empty.
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
                
            #State of the program after the loop has been executed: After the loop has executed, `w` contains all the values of `num`, `maxW` is the maximum value of all `num` inputs, `sumW` is the sum of all `num` inputs, `i` is equal to `n`, `minP` contains the final value calculated in the loop, `k` remains not equal to 1, `n` remains not equal to `k`, `left` is updated to the final value after the loop, `right` is updated to the final value after the loop, `middle` contains the final value calculated in the loop, `truckCnt` contains the final count of trucks required, `loadings` contains the final sum of all values of `w`.
        #State of the program after the if-else block has been executed: *At the end of the execution, `w` contains all the values of `num`, `maxW` is the maximum value of all `num` inputs, `sumW` is the sum of all `num` inputs, `i` is equal to `n`, `minP` contains the final value calculated in the loop, `k` remains not equal to 1, `n` remains not equal to `k`, `left` is updated to the final value after the loop, `right` is updated to the final value after the loop, `middle` contains the final value calculated in the loop, `truckCnt` contains the final count of trucks required, and `loadings` contains the final sum of all values of `w`.
    #State of the program after the if-else block has been executed: *At the end of the execution, `w` contains all the values of `num`, `maxW` is the maximum value of all `num` inputs, `sumW` is the sum of all `num` inputs, `i` is equal to `n`, `minP` contains the final value calculated in the loop, `k` remains not equal to 1, `n` remains not equal to `k`, `left` is updated to the final value after the loop, `right` is updated to the final value after the loop, `middle` contains the final value calculated in the loop, `truckCnt` contains the final count of trucks required, and `loadings` contains the final sum of all values of `w`. If 1 is equal to `k`, the program state remains the same as the precondition.
#Overall this is what the function does:The function takes input values for `n` and `k`, and then calculates the maximum total weight that can be carried by a team of k people based on the weights each person can carry. It does this by iteratively updating the minimum possible weight that can be carried until it finds the optimal weight that satisfies the conditions. The function considers various scenarios based on the values of `n` and `k`, such as when `k` is equal to 1 or when `n` is equal to `k`. It uses binary search to efficiently find the minimum weight. Additionally, it handles cases where the input constraints are violated.

