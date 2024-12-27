Num=int(input("enter a integer:"))
count=0
for i in range(1,Num+1):
    if(Num%i==0):
       count+=1
if(count==2):
    print("prime Number")
else:
    print("Not a prime Number")
print("------------------------------------------")
for i in range(2,Num):
    if(Num%i==0):
        print("Not a prime Number")
        break
    else:
        print("prime Number")
        break