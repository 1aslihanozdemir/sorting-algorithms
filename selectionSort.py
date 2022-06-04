my_list =[4,7,3,8,0,2,1,6,5]

print("unsorted list: ",my_list)

for i in range(len(my_list)-1):
    min_index = i
    for j in range(i+1,len(my_list)):
        if my_list[min_index]>my_list[j]:
            min_index = j
    my_list[i],my_list[min_index]=my_list[min_index],my_list[i]

print("sorted list: " , my_list)








