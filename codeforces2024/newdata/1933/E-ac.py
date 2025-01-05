def evaluate(array, l, u, r):
    left = array[l - 1] if l != 0 else 0
    sections = array[r] - left
    performance = (u + 1 - sections)
    return performance > 0

t = int(input())
for _ in range(t):
    n = int(input())
    sections = list(map(int, input().split()))
    for i in range(1, n):
       sections[i] += sections[i - 1]
    q = int(input())
    answers = []
    for _ in range(q):
        l, u = map(int, input().split())
        left, right = l - 1, n
        while left + 1 < right:
            mid = (left + right)//2
            if evaluate(sections, l - 1, u, mid):
                left = mid
            else:
                right = mid
        if left == -1:
            left += 1

        if left != n - 1:
            lb = l - 1
            count_1 = sections[left] - (sections[lb - 1] if lb != 0 else 0)
            count_2 = sections[left + 1] - (sections[lb - 1] if lb != 0 else 0)
            sum_1 = (u + u - count_1 + 1) * count_1 / 2
            sum_2 = (u + u - count_2 + 1) * count_2 / 2
            if sum_2 > sum_1:
                left += 1
        answers.append(left + 1)
    print(*answers)
