def solve():
    t = int(input())
    for _ in range(t):
        n, na, nb, nc = map(int, input().split())
        x = list(map(int, input().split()))

        x.sort(reverse=True)  # Sort in descending order

        group_a = x[:na]
        group_b = x[na:na + nb]
        group_c = x[na + nb:]

        sum_a = sum(group_a)
        sum_b = sum(group_b)
        sum_c = sum(group_c)

        # Check if the triangle inequality holds
        if sum_a + sum_b > sum_c and sum_b + sum_c > sum_a and sum_c + sum_a > sum_b:
            print("YES")
            print(" ".join(map(str, group_a)))
            print(" ".join(map(str, group_b)))
            print(" ".join(map(str, group_c)))
        else:
            print("NO")

if __name__ == "__main__":
    solve()