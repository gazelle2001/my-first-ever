x=input("enter text")
y=""
for i in x:
    y=i+int(y)
if x==y:
   print("yes,it is paalindrome")
else:
   print("not a palindrome")