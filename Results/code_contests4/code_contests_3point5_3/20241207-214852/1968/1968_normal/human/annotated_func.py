#State of the program right berfore the function call: **
def func():
    rstr = lambda : stdin.readline().strip()
    rstrs = lambda : [str(x) for x in stdin.readline().split()]
    rstr_2d = lambda n: [rstr() for _ in range(n)]
    rint = lambda : int(stdin.readline())
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rint_2d = lambda n: [rint() for _ in range(n)]
    rints_2d = lambda n: [rints() for _ in range(n)]
    pr = lambda args, sep: stdout.write(sep.join(map(str, args)) + '\n')
    ceil1, out = lambda a, b: (a + b - 1) // b, []
    for _ in range(int(input())):
        n, a = rint(), sorted(rints())
        
        be, en, ans = 0, n - 1, n
        
        while be <= en:
            md = be + en >> 1
            su = sum(a[:md + 1])
            for i in range(md + 1, n):
                if su < a[i]:
                    su = -1
                    break
                su += a[i]
            if su == -1:
                be = md + 1
            else:
                en = md - 1
                ans = md + 1
        
        out.append(n - ans + 1)
        
        out.append(' '.join(map(str, [x for x in range(ans, n + 1)])))
        
    #State of the program after the  for loop has been executed: At the end of the loop, `ceil1` remains a lambda function, `out` contains all the values appended during the loop execution, `n`, `a`, `be`, `en`, `ans`, `md`, `su`, `i` have their final updated values based on the loop execution
    pr(out, '\n')
#Overall this is what the function does:The function does not accept any parameters and reads input from stdin to calculate and output specific values based on the input. It performs a binary search algorithm on a sorted list and calculates the sum of elements, determining a specific subset based on certain conditions. Finally, it prints the results using a predefined lambda function. The code does not return a predefined string message as indicated in the annotations.

