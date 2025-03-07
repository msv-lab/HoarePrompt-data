t=int(input(""))
for _ in range(t):
    n=int(input(""))
    arr="".join(input("").split())
    x=arr.find("1")
    y=(arr[::-1]).find("1")
    z=arr[x:n-y]
    print(z.count("0"))