#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a list of n integers a (a[i] is either 0 or 1) representing the state of each cell, where 0 means the cell is free and 1 means the cell contains a chip. Additionally, in each test case, at least one cell contains a chip.
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
        
    #State: After all iterations, `idx` will be equal to the length of `arrs` minus 1; `cnt1` will be the total number of 1s in the list `arrs`; `cnt0` will be the total number of 0s in the list `arrs` minus 1 if the last element of `arrs` is 0, or it will retain its initial value if the last element is 1; `ans` will be 0 if `cnt1` is either 1 or 0, otherwise `ans` will be `cnt0`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers (0s and 1s). For each test case, it counts the number of 0s that are not adjacent to 1s and returns this count. If there is only one 1 or no 1s in the list, it returns 0.

