n = int(input())
exercises = list(map(int, input().split()))

chest = sum(exercises[i] for i in range(0, n, 3))
biceps = sum(exercises[i] for i in range(1, n, 3))
back = sum(exercises[i] for i in range(2, n, 3))

if chest >= biceps and chest >= back:
    print("chest")
elif biceps >= chest and biceps >= back:
    print("biceps")
else:
    print("back")
