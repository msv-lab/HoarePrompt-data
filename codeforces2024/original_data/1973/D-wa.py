def find_split(a, k):
    left, right = min(a), max(a) * len(a)

    while left < right:
        mid = (left + right) // 2

        l, r = 0, 0
        num_subarrays = 1

        while r < len(a):
            while r < len(a) and a[r] * (r - l + 1) <= mid:
                r += 1

            l = r
            num_subarrays += 1

            if num_subarrays > k:
                break

        if num_subarrays == k:
            right = mid
        else:
            left = mid + 1

    return left if left == right else -1