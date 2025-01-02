#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, d and k are integers where 1 ≤ d ≤ 10^5 and 1 ≤ k ≤ d.
def func():
    le = sys.__stdin__.read().split('\n')[::-1]
    af = []
    for i in range(int(le.pop())):
        d, k = list(map(int, le.pop().split()))
        
        a = floor(d / (k * 2 ** 0.5))
        
        if (a * k) ** 2 + (k * (a + 1)) ** 2 > d ** 2:
            af.append('Utkarsh')
        else:
            while (a * k) ** 2 + (k * (a + 2)) ** 2 > d ** 2 and a > 0:
                a -= 1
            if ((a + 1) * k) ** 2 + (k * (a + 2)) ** 2 > d ** 2:
                af.append('Utkarsh')
            else:
                af.append('Ashish')
        
    #State of the program after the  for loop has been executed: `t` is an integer where 1 ≤ t ≤ 100, `le` is a list with `t` fewer elements than it had initially, `af` is a list of length `t` containing either 'Utkarsh' or 'Ashish', `d` and `k` are the last integers read from `le`, `a` is the last calculated value of `floor(d / (k * 2
    print('\n'.join(map(str, af)))
#Overall this is what the function does:The function reads input from standard input, processes a series of test cases, and prints a list of results. Each test case involves two integers, `d` and `k`, where `1 ≤ d ≤ 10^5` and `1 ≤ k ≤ d`. For each test case, the function calculates a value `a` and determines whether a certain condition involving `a`, `d`, and `k` is met. If the condition is met, the result for that test case is 'Utkarsh'; otherwise, it is 'Ashish'. The function then prints the results for all test cases, one per line. After the function executes, the state of the program includes the following: `t` is an integer where `1 ≤ t ≤ 100`, `le` is a list with `t` fewer elements than it had initially, and `af` is a list of length `t` containing either 'Utkarsh' or 'Ashish'. The variables `d` and `k` hold the values of the last test case processed, and `a` holds the last calculated value of `floor(d / (k * 2

