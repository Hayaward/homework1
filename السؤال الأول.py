print("السؤال الأول")
print("الطلب A")
graduatedstudents=['haya','ali','karam','sara','sam']
sname=input('input a student name')
if sname in graduatedstudents:
    print(sname,"is graduated")
else:
    print(sname,"is not graduated")


print("الطلب B")

oddsnumb=[x for x in range(1,1000) if x%2!=0]
print(oddsnumb)



print("الطلب C")

L=['Network','Math','Programming','Physics','Music']
for i in range(len(L)):
    if L[i][0]=='P':
        print(L[i])

print("الطلب D")

d={x:x**2 for x in range(1,11)}
print(d)
