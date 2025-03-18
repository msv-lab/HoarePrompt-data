#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 * 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across test cases does not exceed 2 * 10^5, and the sum of all m values across test cases does not exceed 2 * 10^5.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e.index(d[j]) + 1
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; n and m are integers such that 1 ≤ n, m ≤ 2 * 10^5; a is the integer value provided by the user input; b, c, d, and e are the values from the last iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`, and two binary strings `a` and `b` of lengths `n` and `m` respectively. It then processes these strings and prints an integer result for each test case. The result is determined by finding the position in string `b` up to which characters from string `a` can be matched sequentially, with specific conditions on the index `k`.

