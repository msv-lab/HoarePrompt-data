(n, k) = map(int, input().split())
marks = list(map(int, input().split()))
current_sum = sum(marks)
current_count = n
while True:
    current_average = current_sum / current_count
    if math.ceil(current_average) >= k:
        print(current_count - n)
        break
    current_sum += k
    current_count += 1