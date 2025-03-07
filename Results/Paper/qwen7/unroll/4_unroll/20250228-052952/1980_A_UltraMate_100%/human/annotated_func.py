#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5. The string a consists of n characters, each character is a letter from 'A' to 'G'.
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
        
    #State: Output State: t is an integer between 1 and 1000 inclusive. For each iteration of the loop, n and m are integers, s is a string consisting of uppercase letters from A to G, and ans is an integer calculated based on the frequency of characters in s compared to m. After all iterations, ans contains the sum of additional occurrences of each character in p ('ABCDEFG') needed to match m in s, or the difference if there are more occurrences of a character in s than m allows.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads integers \(n\) and \(m\), and a string \(s\) consisting of uppercase letters from 'A' to 'G'. It calculates the total number of additional occurrences of each character in the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'} needed to ensure each character appears at least \(m\) times in the string \(s\). If a character already appears more than \(m\) times, the excess is subtracted. The function outputs the sum of these adjustments for each test case.

