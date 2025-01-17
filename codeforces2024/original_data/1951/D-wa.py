num_cases = int(input())
for i in range(num_cases):
    n, k = map(int, input().split())
    if n % k == 0:
        print("YES")
        print(1)
        print(n // k)
    else:
        first_store = n // (k - 1)
        second_store = n - ((k - 1) * first_store)
        if second_store > 0:
            print("YES")
            print(2)
            print(f"{first_store} {second_store}")
        else:
            print("NO")
