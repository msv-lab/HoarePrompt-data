#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: Output State: t is assigned the value of the number of test cases, n and m are updated after each iteration based on user input, and ans is the sum calculated for each test case after the completion of the loop. The final value of ans for each test case is printed.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads two integers \( n \) and \( m \). It calculates a value \( ans \) based on these inputs using a specific algorithm involving a loop that updates \( ans \) iteratively. Finally, it prints the computed value \( ans \) for each test case.

