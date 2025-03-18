#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers such that 1 ≤ n, m ≤ 2·10^5, k is an even integer such that 2 ≤ k ≤ 2·min(n, m), a is a list of n integers where 1 ≤ a_i ≤ 10^6, and b is a list of m integers where 1 ≤ b_j ≤ 10^6.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers such that 1 ≤ n, m ≤ 2·10^5, k is an even integer such that 2 ≤ k ≤ 2·min(n, m), a is a list of n integers where 1 ≤ a_i ≤ 10^6, and b is a list of m integers where 1 ≤ b_j ≤ 10^6. For each iteration of the loop, the variables aOnes and bOnes are updated based on the presence of integers from 1 to k in the lists a and b, respectively. After the loop, aOnes and bOnes are either equal to newk (k // 2) or not, and the output is 'yes' if both are equal to newk, otherwise 'no'.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads three integers `n`, `m`, and `k` and two lists `a` and `b` of integers. It then checks if it is possible to select exactly `k // 2` unique integers from the first `k` integers (1 to `k`) that are present in both lists `a` and `b`. If such a selection is possible, it prints 'yes'; otherwise, it prints 'no'. After processing all test cases, the function concludes, and the state of the program is unchanged except for the output produced.

