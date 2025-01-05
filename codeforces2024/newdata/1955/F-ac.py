t = int(input())
for i in range(0, t):
    ones, twos, threes, fours = map(int, input().split())
    tot = ones // 2 + twos // 2 + threes // 2 + fours // 2
    if ones % 2 == 1 and twos % 2 == 1 and threes % 2 == 1:
        tot += 1
    print(tot)