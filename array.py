

names=["hanzalah","shaquib","raghib","moazzam","munazzah"]
temp=[]
for name in names:
    x=name.startswith("m")
    if x==True:
        temp.append(name)
print(temp)
