#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^5; k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m); a is a list of n integers such that 1 ≤ a_i ≤ 10^6; b is a list of m integers such that 1 ≤ b_j ≤ 10^6; the sum of values n and m over all test cases in a test does not exceed 4⋅10^5.
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
        
    #State: Output State: t test cases are processed, for each test case, the program checks if it's possible to select k//2 elements from both lists a and b such that the number of selected elements from a and b are equal. If it's possible, the program prints 'yes', otherwise it prints 'no'.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it checks if it's possible to select k/2 elements from two lists (a and b) such that the number of selected elements from each list is equal. If it's possible, the function prints 'yes'; otherwise, it prints 'no'.

