#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^5, and k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m). a is a list of n integers where each integer is in the range [1, 10^6], and b is a list of m integers where each integer is in the range [1, 10^6]. The sum of n and m over all test cases in a test does not exceed 4⋅10^5.
def func():
    for t in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        aOnes = 0
        
        bOnes = 0
        
        newk = k // 2
        
        i = 1
        
        while i <= k:
            if i in a and i in b:
                if aOnes < bOnes:
                    aOnes += 1
                else:
                    bOnes += 1
            elif i in a and aOnes <= newk:
                aOnes += 1
            elif i in b and bOnes <= newk:
                bOnes += 1
            else:
                break
            i += 1
        
        if aOnes == newk and bOnes == newk:
            print('yes')
        else:
            print('no')
        
    #State: Output State: After all iterations of the loop have finished, `i` will be the first integer greater than `k`, `aOnes` will be the total count of elements in `a` that are also in the range from 1 to `k` (inclusive) and satisfy the conditions within the loop, `bOnes` will be the total count of elements in `b` that are also in the range from 1 to `k` (inclusive) and satisfy the conditions within the loop. `n` will be the last `n` value inputted, `m` will be the last `m` value inputted, and `k` will be the last `k` value set before the loop exited. If `aOnes` equals `newk` and `bOnes` equals `newk`, the loop would have printed 'yes' for that test case. Otherwise, it would have printed 'no'.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads values for \( n \), \( m \), and \( k \), along with two lists of integers \( a \) and \( b \). It then counts how many elements in \( a \) and \( b \) are within the range from 1 to \( k/2 \) (inclusive) and satisfy certain conditions. If both counts equal \( k/2 \), it prints 'yes'; otherwise, it prints 'no'. After processing all test cases, it outputs the results for each case.

