#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^5, and k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m). Arrays a and b are lists of integers where 1 ≤ a_i, b_j ≤ 10^6 for all i and j. The sum of values n and m over all test cases in a test does not exceed 4⋅10^5.
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
        
    #State: Output State: The output state consists of 'yes' or 'no' printed for each test case based on whether `aOnes` and `bOnes` both equal `newk` (which is `k // 2`) after the loop executes. If both `aOnes` and `bOnes` equal `newk`, it prints 'yes', otherwise it prints 'no'.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes integers n, m, and k, along with two arrays a and b as inputs. It counts the occurrences of integers up to k in both arrays, ensuring that the counts do not exceed k//2. If the counts of integers in both arrays up to k//2 are equal, it prints 'yes'; otherwise, it prints 'no'.

