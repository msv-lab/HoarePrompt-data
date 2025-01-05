import sys

# 更新数组b的元素
def update_b(b, index, value):
    b[index] = value

# 检查区间是否是好的，并返回最大值
def check_good_interval(a, b, v, l, r):
    current_or = 0
    max_beauty = -1
    for i in range(l, r+1):
        current_or |= b[i]
        max_beauty = max(max_beauty, a[i])
        if current_or >= v:
            return max_beauty
    return -1

# 处理查询
def process_queries(n, a, b, v, queries):
    for query in queries:
        query_type = int(query[0])
        if query_type == 1:
            index, value = int(query[1]), int(query[2])
            update_b(b, index - 1, value)  # 数组索引从0开始
        elif query_type == 2:
            l, r = int(query[1]), int(query[2])
            print(check_good_interval(a, b, v, l - 1, r - 1), end=' ')  # 数组索引从0开始
        
# 主程序
def main():
    t = int(input().strip())  # 读取测试案例数量
    results = []
    for _ in range(t):
        n, v = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        q = int(input().strip())
        queries = []
        for _ in range(q):
            queries.append(input().strip().split())
        process_queries(n, a, b, v, queries)
        print()  # 每个测试用例之间打印换行

if __name__ == "__main__":
    main()
