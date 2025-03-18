#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^5, and k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m). Each test case consists of two arrays a and b, where a has n integers and b has m integers, and each integer in both arrays is a positive integer not exceeding 10^6. Additionally, the sum of n and m over all test cases in a test does not exceed 4⋅10^5.
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
        
    #State: Output State: After the loop executes all iterations, `i` is `k + 1`, `aOnes` is the total count of elements from list `a` that were found in the loop up to `newk`, `bOnes` is the total count of elements from list `b` that were found in the loop up to `newk`, `t` is the total number of test cases processed, `n`, `m`, and `k` retain their initial values after all test cases, `newk` is equal to `k // 2`, and the final output will be 'yes' if both `aOnes` and `bOnes` are equal to `newk`, otherwise it will be 'no'.
    #
    #This means that after processing all test cases, the loop will have iterated through all possible values of `i` up to `k` for each test case, counting the occurrences of `i` in lists `a` and `b` as per the given conditions. The final decision ('yes' or 'no') will be based on whether both `aOnes` and `bOnes` meet the condition of being equal to `newk` after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( n \) and \( m \), an even integer \( k \), and two arrays \( a \) and \( b \). For each test case, it counts the occurrences of integers from 1 to \( k/2 \) in arrays \( a \) and \( b \) under specific conditions. If the counts of these integers in both arrays are equal to \( k/2 \) after processing all test cases, it prints 'yes'; otherwise, it prints 'no'.

