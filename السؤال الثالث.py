filename="t.txt"
infile=open(filename,'r')
s=infile.readlines()
infile.close()
c=0
for i in s:
    qa=i.rstrip().split(",")
    print(qa[0])
    a=input()
    if a==qa[-1]:
        c+=1
sname=input("enter your username ")
print(sname,'  ',c)
outfile=open("haya.txt",'w')
outfile.write(sname+'  '+str(c))
outfile.close()
