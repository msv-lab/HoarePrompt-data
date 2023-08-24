import itertools

N, P = map(int, input().split())
S = input()

count = 0
prefix_sum = 0
digits_mod = [0] * P

for i in range(N-1, -1, -1):
    prefix_sum = (prefix_sum + int(S[i]) * pow(10, N-i-1, P)) % P
    count += digits_mod[prefix_sum]
    digits_mod[prefix_sum] += 1

count += digits_mod[0]

print(count)