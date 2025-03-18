#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). a is a list of n integers where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). a is a list of n integers where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. After the loop executes all the iterations, s, c, and t are integers where s is always 0, c is the sum of s * (l[i] + t) for all i from 0 to n-1, and t is the sum of s for all i from 0 to n-1.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( m \), and \( k \), along with a list \( a \) of \( n \) integers. For each test case, it sorts the list \( a \), calculates a cumulative sum based on the sorted values and the current value of \( t \), and updates \( t \) accordingly. Finally, it prints the total calculated sum for each test case.

