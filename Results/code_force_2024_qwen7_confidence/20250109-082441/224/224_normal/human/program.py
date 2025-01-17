def is_intersect(a, b, c, d):
    # 按照顺时针顺序排列
    points = sorted([a, b, c, d])
    # 获取两条线段的位置
    i1, i2, i3, i4 = points
    # 判断是否相交：一条线段的端点在另一条线段的两侧
    # 判断条件：i1-i2 是一条线段，i3-i4 是另一条线段，如果它们交错，则返回 True
    return (i1 < i3 < i2 < i4)

# 输入处理
t = int(input())  # 测试用例数量
results = []

for _ in range(t):
    a, b, c, d = map(int, input().split())
    if is_intersect(a, b, c, d):
        results.append("YES")
    else:
        results.append("NO")

# 输出结果
print("\n".join(results))