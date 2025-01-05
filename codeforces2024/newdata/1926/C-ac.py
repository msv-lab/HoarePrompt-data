nums=[0]*(200001)
for i in range(1,200001):
    nums[i]=nums[i-1]
    x=i
    while x>0:
        nums[i]+=x%10
        x//=10
def main():
    t=int(input())
    for j in range(t):
        n=int(input())
        print(nums[n])
main()