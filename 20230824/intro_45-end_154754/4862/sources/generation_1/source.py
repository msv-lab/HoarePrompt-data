N = int(input())

if N == 0 or N == 1:
    print(0)
else:
    relationships = (2 ** N) - N - 1
    print(relationships)