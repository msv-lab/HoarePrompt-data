#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n integers where 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9, m is an integer such that 1 ≤ m ≤ 10^5, and for each of the m queries, x_i and y_i are integers such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. Additionally, for each city, the closest city is determined uniquely.
def func():
    for i in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        d1 = defaultdict(int)
        
        d2 = defaultdict(int)
        
        d1[2] = 1
        
        for i in range(1, n - 1):
            if l[i + 1] - l[i] < l[i] - l[i - 1]:
                d1[i + 2] = 1 + d1[i + 1]
            else:
                d1[i + 2] = l[i + 1] - l[i] + d1[i + 1]
        
        d2[n - 1] = 1
        
        for i in range(n - 2, 0, -1):
            if l[i] - l[i - 1] < l[i + 1] - l[i]:
                d2[i] = 1 + d2[i + 1]
            else:
                d2[i] = l[i] - l[i - 1] + d2[i + 1]
        
        m = int(input())
        
        for j in range(m):
            x, y = map(int, input().split())
            if y > x:
                print(d1[y] - d1[x])
            else:
                print(d2[y] - d2[x])
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, i is equal to t (indicating all test cases have been processed), n is undefined (as it changes with each iteration), l is undefined (as it changes with each iteration), d1 is undefined (as it changes with each iteration), d2 is undefined (as it changes with each iteration), m is undefined (as it changes with each iteration), and j is undefined (as it changes with each iteration).
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of city positions and a set of queries. For each query, it calculates and prints the cumulative distance to the closest city from the midpoint between two specified cities.

