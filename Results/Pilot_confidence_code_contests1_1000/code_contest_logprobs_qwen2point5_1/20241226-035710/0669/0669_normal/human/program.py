def vali(a):
    b=int(a**0.5)
    flag=False
    for i in range(1,b+1):
        if a%i==0:
            j=a/i
            delta=12*j-3*i**2
            if delta<0:
                continue
            #x1=(3*i+delta**0.5)/6
            x2=(3*i-delta**0.5)/6
            if x2-int(x2)==0 and x2>=1:
                flag=True
                break
    return flag
if __name__ == "__main__":
    N=input()
    results=[]
    for k in range(1,N+1):
        results.append(vali(input()))
    for result in results:
        print(result)