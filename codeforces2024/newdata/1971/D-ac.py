t = int(input())
for _ in range(t):
    s=input()
    print(s.count('10')+max(s.count('01'),1))