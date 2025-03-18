#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 50, representing the number of cells on the ribbon. a is a list of n integers, each being 0 or 1, where 0 represents a free cell and 1 represents a cell containing a chip. At least one cell in each test case contains a chip.
def func():
    """
     
    0 과 1로 이루어진 배열을 받고 난 후 
    0으로만 연속되고 1으로만 연속된 하나의 블록으로 만드는 것이 목표임
    오른쪽에 있는 1을 가장 가까운 왼쪽으로 옮겨서 독립된 0, 1 블록으로 만들어야 함
     
    그냥 중간에 비어있는 0의 갯수가 정답일 듯
     
    """
    t = int(input())
    for _ in range(t):
        length = int(input())
        
        arrs = list(map(int, input().split()))
        
        cnt0 = 0
        
        for idx in range(len(arrs)):
            if arrs[0] == 0 and idx != 0:
                if arrs[idx] == 0:
                    cnt0 += 1
            elif arrs[0] == 1:
                if arrs[idx] == 0:
                    cnt0 += 1
        
        cnt1 = 0
        
        for idx in range(len(arrs)):
            if arrs[idx] == 1:
                cnt1 += 1
        
        if arrs[0] == 0:
            if arrs[len(arrs) - 1] == 0:
                cnt0 -= 1
        
        ans = 0
        
        if cnt1 == 1 or cnt1 == 0:
            ans = 0
        else:
            ans = cnt0
        
        print(ans)
        
    #State: After all iterations, `t` is an input integer between 1 and 1000, `n` is an integer such that 2 ≤ n ≤ 50, `a` is a list of `n` integers, each being 0 or 1, and at least one cell in each test case contains a chip. For each iteration, `length` is an input integer, `arrs` is a list of integers obtained from the input and must have at least as many elements as the number of iterations, `idx` is `len(arrs) - 1`, `cnt0` is the count of zeros in `arrs` minus 1 if the first and last elements of `arrs` are 0, otherwise `cnt0` remains unchanged, `cnt1` is the total number of 1s in `arrs`. If `cnt1` is 0 or 1, `ans` remains 0. If `cnt1` is greater than 1, `ans` is set to `cnt0`. The loop will have executed `t` times, and the final output will be the value of `ans` for each iteration.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of an integer `n` indicating the number of cells on a ribbon, followed by a list of `n` integers (0s and 1s) representing the state of each cell. The function calculates the minimum number of moves required to rearrange the chips (1s) so that all 1s are grouped together, with all 0s either before or after them. The result for each test case is printed to the standard output. After processing all test cases, the function completes without returning any value.

