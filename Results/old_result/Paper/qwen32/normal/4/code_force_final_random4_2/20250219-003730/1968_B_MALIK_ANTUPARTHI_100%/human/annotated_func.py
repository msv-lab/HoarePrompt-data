#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 2 * 10^5. a and b are binary strings of length n and m, respectively. The sum of all n values across test cases does not exceed 2 * 10^5, and the sum of all m values across test cases does not exceed 2 * 10^5.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e[k:].index(d[j]) + 1 + k
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: i is a, b, c, d, and e are the values from the last iteration, k is the final value from the last iteration of the nested loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings and their respective lengths. For each test case, it calculates and prints an integer value `k` which represents the position in the first binary string up to which characters can be matched with the second binary string following a specific pattern.

