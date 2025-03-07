#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2⋅10^5, and the sum of all m values across all test cases does not exceed 2⋅10^5.
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
        
    #State: i is equal to a, j is equal to b, k is either k_final or j + 1, where k_final is the final value of k after the last successful search for d[j] in e[k:] for each iteration, and d and e are the same as the initial input strings.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it accepts integers \(t\), \(n\), and \(m\) along with two binary strings \(a\) and \(b\). It then finds the smallest index \(k\) in string \(e\) (which is initially assigned the value of string \(d\)) such that the substring of \(e\) starting from index \(k\) contains all characters of \(d\) in the same order as they appear in \(d\). If no such \(k\) exists, it returns the length of \(d\). The function prints the value of \(k\) for each test case.

