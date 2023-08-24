def can_achieve_array(t: int, arr: list):
    results = []
    for i in range(t):
        n, k = arr[i * 2]
        a = arr[i * 2 + 1]
        v = [0] * n
        for j in range(n):
            while v[j] < a[j]:
                if v[j] + k ** (j + 1) > a[j]:
                    break
                v[j] += k ** (j + 1)
        if all(v[j] == a[j] for j in range(n)):
            results.append("YES")
        else:
            results.append("NO")
    return results


# Read the number of test cases
t = int(input())

# Read the test cases
arr = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    arr.append([n, k])
    arr.append(a)

# Call the function and print the results
results = can_achieve_array(t, arr)
for res in results:
    print(res)