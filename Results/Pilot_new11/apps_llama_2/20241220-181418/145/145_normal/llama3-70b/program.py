n = int(input())
ticket = list(map(int, input()))

def can_divide(ticket):
    total_sum = sum(ticket)
    if total_sum % 2 != 0:
        return False
    target_sum = total_sum // 2
    curr_sum = 0
    segments = 0
    for digit in ticket:
        curr_sum += digit
        if curr_sum == target_sum:
            segments += 1
            curr_sum = 0
    return segments >= 2

if can_divide(ticket):
    print("YES")
else:
    print("NO")
