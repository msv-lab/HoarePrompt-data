def func_1(number):
    return number % 1000000007

def func_2(arr):
    new_segment = []
    max_segment = [0, 0]
    segments_variants = []
    max_sum = -1
    for i in range(len(arr)):
        if new_segment:
            if arr[i] < 0:
                if max_segment[0] > new_segment[0]:
                    segments_variants.append(max_segment + [i - 1])
                else:
                    segments_variants.append(new_segment + [i - 1])
                    max_segment = new_segment
                new_segment = []
                max_segment[0] += arr[i]
            else:
                max_segment[0] += arr[i]
                new_segment[0] += arr[i]
        else:
            if arr[i] >= 0:
                new_segment = [arr[i], i]
            max_segment[0] += arr[i]
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
    return total_max_segment

def func_3(number, quantity):
    answer = 0
t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    max_segment = func_2(a)
    if max_segment[0] == -1:
        max_segment[0] = 0
    answer = max_segment[0] * 2 ** k + sum(a) - max_segment[0]
    print(func_1(answer))