def can_reach_destination(t, test_cases):
    results = []
    for test_case in test_cases:
        n, (row1, row2) = test_case
        
        # 可达性标志
        reachable_first_row = True  # 当前是否可以在第一行向右移动
        reachable_second_row = False  # 当前是否可以在第二行向右移动
 
        # 遍历每一列，模拟机器人移动
        for j in range(n):
            # 在第一行的情况下
            if reachable_first_row:
                if row1[j] == '>':
                    # 向右移动
                    if j == n - 1:
                        reachable_second_row = True  # 到达 (1, n)，准备切换到第二行
                else:
                    # 如果箭头指向左
                    reachable_first_row = False  # 第一行无法继续向右
                    if j < n - 1 and row2[j] == '>':
                        reachable_second_row = True  # 下移到第二行并向右移动
 
            # 在第二行的情况下
            if reachable_second_row:
                if row2[j] == '>':
                    # 继续向右
                    if j == n - 1:
                        reachable_second_row = True  # 到达 (2, n)
 
        # 判断结果
        if reachable_second_row:
            results.append("YES")
        else:
            results.append("NO")
 
    return results
 
# 主函数处理输入和输出
if __name__ == "__main__":
    t = int(input())  # 输入测试用例数量
    test_cases = []
    
    for _ in range(t):
        n = int(input())  # 输入每个测试用例的列数
        row1 = input().strip()  # 输入第一行的箭头
        row2 = input().strip()  # 输入第二行的箭头
        test_cases.append((n, (row1, row2)))  # 将测试用例添加到列表中
 
    results = can_reach_destination(t, test_cases)  # 处理测试用例
    for result in results:
        print(result)  # 输出结果