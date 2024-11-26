r=lambda:map(int,raw_input().split())
a,b=r()

print -sum(sorted(r())[ :b])
