#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, representing the number of test cases. For each test case, n is an integer such that 2 <= n <= 50, representing the number of cells. a is a list of n integers where each integer a_i is either 0 or 1, representing whether the i-th cell is free (0) or contains a chip (1). At least one cell contains a chip in each test case.
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
        
    #State: After all iterations, `t` is 0, `length` has been an input integer for each iteration, `arrs` has been a list of integers with at least `length` elements for each iteration, `idx` has been `len(arrs) - 1` for each iteration, `cnt0` and `cnt1` have been calculated for each iteration based on the initial conditions: if `arrs[0] == 0` and the last element of `arrs` is not 0, `cnt0` and `cnt1` remain unchanged; if `arrs[0] == 0` and the last element of `arrs` is 0, `cnt0` is the count of zeros in `arrs` starting from index 1 minus 1, and `cnt1` is the total number of 1s in `arrs`; if `arrs[0] == 1`, `cnt0` is the count of zeros in `arrs` starting from index 1, and `cnt1` is the total number of 1s in `arrs`. If `cnt1` is 0 or 1, `ans` remains 0. Otherwise, if `cnt1` is neither 0 nor 1, `ans` is set to `cnt0`.
#Overall this is what the function does:The function processes a series of test cases, where each test case involves a list of integers (0s and 1s) representing cells, with 1s indicating cells containing chips and 0s indicating free cells. The function calculates the minimum number of moves required to group all 1s together into a single contiguous block by moving 1s to the left. The result for each test case is printed to the console. The function does not return any value; it only outputs the results directly.

