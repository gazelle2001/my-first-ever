
list=[1,7,9,5.8,4,3]
size=len(list)
temp=list[0]
list[0]=list[len(list)-1]
list[size-1]=temp
print(list)