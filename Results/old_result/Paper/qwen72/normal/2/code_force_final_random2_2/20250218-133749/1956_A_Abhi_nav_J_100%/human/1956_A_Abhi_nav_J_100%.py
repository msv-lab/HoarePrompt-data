n=int(input())
def checker(a,b):
    if a<=b:
        return a-1
    else:
        return b
    
for i in range(n):
    og=str(input())
    og_list=og.split()
    k=int(og_list[0])
    q=int(og_list[1])
 
    k_wali=str(input())
    k_wali_list=k_wali.split()
    q_wali=str(input())
    q_wali_list=q_wali.split()
 
    for j in range(len(q_wali_list)):
        print(checker(int(k_wali_list[0]),int(q_wali_list[j])) , end=' ')
    print('\n')