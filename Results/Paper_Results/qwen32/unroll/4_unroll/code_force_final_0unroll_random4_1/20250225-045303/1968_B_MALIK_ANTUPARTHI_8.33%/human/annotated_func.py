#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 2 * 10^5. a and b are binary strings of lengths n and m, respectively. The sum of all n values across test cases does not exceed 2 * 10^5, and the sum of all m values across test cases does not exceed 2 * 10^5.
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
        
    #State: `a` is the number of test cases processed, `b` and `c` are the last pair of integers read, `d` and `e` are the last pair of strings read, and `k` is the final value printed for the last iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers `n` and `m`, and two binary strings `a` and `b` of lengths `n` and `m`, respectively. It then computes and prints an integer `k` for each test case, which represents the position in string `a` up to which characters can be matched sequentially in string `b`.

