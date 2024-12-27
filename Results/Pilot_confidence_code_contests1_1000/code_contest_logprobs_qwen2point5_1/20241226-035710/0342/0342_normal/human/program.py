import numpy as np

H, W = map(int, raw_input().split())
arr=np.array([])
s=0
while s != H:
  li=list(raw_input())
  li=np.array(li)
  arr=np.hstack((arr,li))

  s+=1
arr=arr.reshape((H,W))
count=0
def check(x,y):
    global count
    if arr[x,y] == "#":
        count+=1

for x in range(H):
    stri=""
    for y in range(W):
        if arr[x,y] == ".":
            count=0
            top= None
            right =None
            left=None
            if y != 0:
                top=True
                check(x,(y-1))
            if x != 0:
                if top:
                    check((x-1),(y-1))
                check((x-1),y)
                left=True
            if x != (W-1):
                if top:
                    check((x+1),(y-1))
                right=True
                check((x+1),y)
            if y != (H-1):
                if left:
                    check(x-1,y+1)
                if right:
                    check(x+1,y+1)
                check(x,(y+1))
            stri=stri+str(count)
        else:
            stri=stri+"#"
    print(stri)
