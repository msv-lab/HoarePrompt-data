n = int(input())
a = list(map(int, input().split()))
total_sum = sum(a)
if total_sum % 2 != 0:
    print("NO")
else:
    half_sum = total_sum // 2
    prefix_sum = 0
    for i in range(n):
        prefix_sum += a[i]
        if prefix_sum == half_sum:
            print("YES")
            break
        if prefix_sum > half_sum:
            for j in range(i):
                prefix_sum -= a[j]
                if prefix_sum == half_sum:
                    print("YES")
                    exit()
            prefix_sum += a[i]
            break
    else:
        print("NO")
