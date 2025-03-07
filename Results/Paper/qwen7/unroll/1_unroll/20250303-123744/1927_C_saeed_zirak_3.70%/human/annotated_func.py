#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n, m ≤ 2⋅10^5, 2 ≤ k ≤ 2⋅min(n, m), and k is even. a is a list of n integers where each integer is in the range [1, 10^6], and b is a list of m integers where each integer is in the range [1, 10^6]. It is guaranteed that the sum of values n and m over all test cases in a test does not exceed 4⋅10^5.
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
        
    #State: Output State: t test cases are processed. For each test case, it is checked whether it's possible to select elements from lists a and b such that the number of selected elements from each list equals k//2 (newk). If both counts are equal to newk at the end of the loop, the output is 'yes', otherwise 'no'. The final state includes the result ('yes' or 'no') for each test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( n \), \( m \), and \( k \), along with two lists \( a \) and \( b \). For each test case, it checks whether it is possible to select exactly \( \frac{k}{2} \) elements from list \( a \) and \( \frac{k}{2} \) elements from list \( b \) such that the selected elements are the same in both lists. If such a selection is possible, it prints 'yes'; otherwise, it prints 'no'. After processing all test cases, the function outputs the result for each test case.

