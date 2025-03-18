#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. Each of the t test cases consists of an integer n such that 2 <= n <= 100, followed by n lines where each line contains two integers a and x, where a is an integer in {1, 2, 3} and 1 <= x <= 10^9. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and all pairs (a, x) are distinct.
def func():
    loop = int(input())
    for iterable in range(loop):
        less = []
        
        big = []
        
        no = []
        
        num = 0
        
        innerLoop = int(input())
        
        for iterable2 in range(innerLoop):
            x, a = map(int, input().split())
            if x == 1:
                big.append(a)
            elif x == 2:
                less.append(a)
            else:
                no.append(a)
        
        for i in range(max(big), min(less)):
            if i not in no:
                num = i
                break
        
        print(num)
        
    #State: t is an integer such that 1 <= t <= 500; loop is an integer equal to t; less, big, and no are empty lists; num holds the last computed value but is not used further.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints defined by pairs of integers. For each test case, it identifies and prints an integer that is greater than or equal to the maximum value associated with constraint type 1 and less than or equal to the minimum value associated with constraint type 2, while not being associated with constraint type 3.

