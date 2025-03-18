#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 2 ≤ n ≤ 50; the second line of each test case contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1, indicating whether the i-th cell is free (0) or contains a chip (1); in each test case, at least one cell contains a chip.
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
        
    #State: After all iterations, `t` is 0, `idx` is the length of the last `arrs`, `cnt1` is the total count of 1s in the last `arrs`, the first element of `arrs` is 0, the last element of `arrs` is 0, `cnt0` is decreased by 1 if the last element of `arrs` is 0, and `ans` is either 0 (if `cnt1` equals 1 or 0) or `cnt0` (if `cnt1` is neither 1 nor 0).
#Overall this is what the function does:The function processes multiple test cases, each containing an integer n and a sequence of n binary values (0 or 1). For each test case, it counts the number of consecutive 0s between the first and last 1s in the sequence. If there is only one 1 or no 1s, it returns 0. Otherwise, it returns the count of consecutive 0s. The function outputs the result for each test case.

