vp = int(raw_input())
vd = int(raw_input())
t_read = int(raw_input())
f = int(raw_input())
c = int(raw_input())


pl = 0
dl = 0
t = 1
count = 0

# print(vp, vd, t_read, f, c)


while (pl + vp <= c):
    
    pl += vp


    if (t > t_read):
        dl += vd
        if (dl >= pl and pl + vp <= c):
            count += 1
            dl = pl
            pl += ((2 * (dl / vd)) + f) * vp
            # print((str(t), str(count), str(dl), str(pl)))  

            # while (dl > 0 and pl + vp <= c):
            #     dl = max(dl - vd, 0)
            #     print((str(t), str(count), str(dl), str(pl)))
            #     pl += vp
            # pl += f * vp
            # if (pl + vp >= c):
            #     break
            
            
            


    
    t += 1

print(count)

    



















# while (pl < c - vp):

#     # if (t == 0):
#     #     t += 1
#     #     print((str(t), str(count), str(dl), str(pl), 'BBE'))
#     #     continue

#     pl += vp
    

#     if (t > t_read - 1):
#         dl += vd
    
#     lc = 0
#     if (pl <= dl):
#         count+=1
#         lc+=1
#         t = (t_read) - dl/vd - f
#         print((str(t), str(count), str(dl), str(pl), 'CC'))
#         # pl = pl + vp
#         # if ()
#         dl = 0
#         # continue
#     if (lc == 1):
#         t_read -=1
#     # print((str(t), str(count), str(dl), str(pl), 'BB'))
#     t += 1
   

# print(count)

# 1
# 2
# 1
# 1
# 8


    