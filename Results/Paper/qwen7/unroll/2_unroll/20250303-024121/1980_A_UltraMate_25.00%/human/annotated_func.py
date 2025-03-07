#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5. The string a consists of n characters, each character is a letter from 'A' to 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEF'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: The value of `ans` after all iterations of the loop, which is calculated based on the input strings `s` provided in each iteration.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer t (1 ≤ t ≤ 1000), integers n and m (1 ≤ n ≤ 50 and 1 ≤ m ≤ 5), and a string a consisting of n characters from 'A' to 'G'. For each test case, it calculates and prints the value of `ans`, which represents the total number of additional occurrences of characters 'A' to 'F' needed in the string `a` to meet the requirement of having at least m occurrences of each character, across all iterations.

