#insertion sort
list_0 = [4,7,3,8,0,2,1,6,5]

for i in range(1,len(list_0)):
    while i>0:
        if list_0[i-1]>list_0[i]:
           list_0[i-1],list_0[i]= list_0[i],list_0[i-1]
        i-=1

print(list_0)
