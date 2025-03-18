#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5, and a is a string of n characters where each character is one of 'A', 'B', 'C', 'D', 'E', 'F', or 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEFG'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: Output State: t is an integer between 1 and 1000. For each iteration of the loop, n and m are integers, s is a string consisting of characters from 'A' to 'G', hmp is a counter object containing the count of each character in s, and ans is an integer calculated based on the counts of characters in s and the value of m. After all iterations, ans is the sum of additional occurrences of each character required to make the count of each character in s equal to m.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \( n \) and \( m \), and a string \( s \) consisting of \( n \) characters from 'A' to 'G'. It calculates the number of additional occurrences of each character required to make the count of each character in \( s \) equal to \( m \). Finally, it prints the total count of these additional occurrences for each test case.

