#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where each integer is between 1 and 10^9 inclusive; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    ones = [(0) for i in range(n + 1)]
    sum = [(0) for i in range(n + 1)]
    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if nums[i - 1] == 1 else 0)
        
        sum[i] = sum[i - 1] + nums[i - 1] - 1
        
    #State: Output State: After the loop executes all its iterations, `ones[i]` will contain the cumulative count of 1s in the `nums` list up to each index `i`, and `sum[i]` will contain the cumulative sum of the elements in `nums` up to each index `i`, adjusted by subtracting 1 at each step.
    #
    #In more detail:
    #- `ones[i]` will be the total number of 1s in the `nums` list from index 0 to index `i`.
    #- `sum[i]` will be the cumulative sum of the elements in `nums` from index 0 to index `i`, but each element is decremented by 1 before adding to the cumulative sum.
    #
    #This means that after the loop completes, `ones[n]` will give the total count of 1s in `nums`, and `sum[n]` will give the adjusted cumulative sum of the elements in `nums`.
    for _ in range(q):
        l, r = map(int, input().split(' '))
        
        if l == r:
            print('NO')
            continue
        
        onesInRange = ones[r] - ones[l - 1]
        
        sumInRange = sum[r] - sum[l - 1]
        
        if 2 * onesInRange + (r - l + 1) - onesInRange <= sumInRange:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: After the loop executes all its iterations, `ones[i]` will contain the cumulative count of 1s in the `nums` list up to each index `i`, and `sum[i]` will contain the cumulative sum of the elements in `nums` up to each index `i`, adjusted by subtracting 1 at each step. This means that `ones[n]` will give the total count of 1s in `nums`, and `sum[n]` will give the adjusted cumulative sum of the elements in `nums`.
    #
    #In more detail, after the loop completes, for every index `i` from 0 to `n`:
    #- `ones[i]` will store the total number of 1s in the `nums` list from index 0 to index `i`.
    #- `sum[i]` will store the cumulative sum of the elements in `nums` from index 0 to index `i`, with each element decremented by 1 before adding to the cumulative sum.
    #
    #The values of `q`, `l`, and `r` will reflect the final state after all iterations of the loop have been executed, with `q` being decremented by 1 for each iteration where `l` is not equal to `r`. The conditions checked within the loop will be evaluated based on the updated values of `ones` and `sum` arrays.
#Overall this is what the function does:The function processes a list of positive integers and handles multiple queries. It calculates the cumulative count of 1s and the adjusted cumulative sum of elements up to each index in the list. For each query, it checks if a specific condition is met based on the range of indices provided and prints 'YES' or 'NO' accordingly. After processing all queries, the function does not return any value but modifies the internal state of the `ones` and `sum` lists to reflect the cumulative counts and sums.

