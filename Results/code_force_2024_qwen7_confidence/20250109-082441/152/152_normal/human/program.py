t = int(input())  # 读取测试用例数量
for i in range(t):
    k, q = map(int, input().split())  # 读取k和q
    list_a = list(map(int, input().split()))  # 读取list_a
    list_n = list(map(int, input().split()))  # 读取list_n
    min_a = min(list_a)  # 找到list_a中的最小值

    # 使用列表推导式生成结果
    list_result = [n if n < min_a else min_a - 1 for n in list_n]
    
    # 对结果进行排序
    list_result.sort()

    # 输出结果
    print(" ".join(map(str, list_result)))