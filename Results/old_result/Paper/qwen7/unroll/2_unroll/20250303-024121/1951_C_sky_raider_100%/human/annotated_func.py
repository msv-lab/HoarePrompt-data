#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9). a is a list of n integers where 1 ≤ a_i ≤ 10^9 for each 1 ≤ i ≤ n.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        t = 0
        
        s = 0
        
        c = 0
        
        for i in range(n):
            s = min(m, k)
            c += s * (l[i] + t)
            t += s
            k -= s
        
        print(int(c))
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9). a is a list of n integers where 1 ≤ a_i ≤ 10^9 for each 1 ≤ i ≤ n. After the loop executes all the iterations, c is an integer representing the sum of the products of the sorted list elements with their respective accumulated values of t, adjusted by the minimum of m and k for each element.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \), \( m \), and \( k \), along with a list of \( n \) integers. For each test case, it sorts the list of integers, then iterates through the list, calculating a cumulative sum based on the minimum of \( m \) and \( k \) for each element. This cumulative sum is adjusted by adding the current value of \( t \) and multiplied by the sorted list element. Finally, it prints the total sum for each test case.

