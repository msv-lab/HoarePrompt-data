def func_1(n, ticket):

    def segment_sum(start, end):
        return sum((int(ticket[i]) for i in range(start, end + 1)))
    for segment_length in range(1, n):
        target_sum = segment_sum(0, segment_length - 1)
        current_sum = 0
        segment_count = 0
        for i in range(n):
            current_sum += int(ticket[i])
            if current_sum == target_sum:
                current_sum = 0
                segment_count += 1
        if current_sum == 0 and segment_count > 1:
            return 'YES'
    return 'NO'
n = int(input())
ticket = input()
print(func_1(n, ticket))