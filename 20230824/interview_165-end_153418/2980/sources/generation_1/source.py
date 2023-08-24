def winning_or_losing(k, S, m, positions):
    results = []
    for pos in positions:
        xor_sum = 0
        for num in pos:
            xor_sum ^= num
        if xor_sum == 0:
            results.append('L')
        else:
            losing = True
            for s in S:
                if xor_sum ^ s < xor_sum:
                    losing = False
                    break
            if losing:
                results.append('L')
            else:
                results.append('W')
    return ''.join(results)

k, *S = map(int, input().split())
m = int(input())
positions = []
for _ in range(m):
    l, *h = map(int, input().split())
    positions.append(h)

print(winning_or_losing(k, S, m, positions))