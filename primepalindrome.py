Num=int(input("Enter a number:"))
count=0
rem=0
rev=0
temp=Num
for i in range(1,Num+1):
    if(Num%i==0):
        count=count+1
if(count==2):
        while(Num!=0)
        rem=Num%10
        rev=rev*10+rem
        Num=Num//10
if(temp==rev):
    print("integer is palindrome")
else:
    print("integer is not a palindrome")