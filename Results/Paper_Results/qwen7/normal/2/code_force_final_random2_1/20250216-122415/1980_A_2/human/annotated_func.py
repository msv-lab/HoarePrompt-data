#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5; a is a string of length n consisting of characters from 'A' to 'G'.
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
        
    #State: After all iterations of the loop, i will be 'F', p is 'ABCDEF', ans will be 0, hmp will be a dictionary with keys 'A', 'B', 'C', 'D', 'E', 'F' each mapped to the total count of these characters in the input string s across all iterations, n will be the input integer from the first iteration, m will be the input integer from the first iteration, and s will be the input string from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer t (number of cases), integers n and m, and a string s of length n consisting of characters from 'A' to 'G'. For each test case, it calculates and prints the minimum number of operations required to ensure that each character in the set 'ABCDEF' appears at least m times in the string s.

