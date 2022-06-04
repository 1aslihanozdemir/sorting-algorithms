#insertion sort
my_list = [4,7,3,8,0,2,1,6,5]

for i in range(1,len(my_list)):
    while i>0:
        if my_list[i-1]>my_list[i]:
           my_list[i-1],my_list[i]= my_list[i],my_list[i-1]
        i-=1

print(my_list)
