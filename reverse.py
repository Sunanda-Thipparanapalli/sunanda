Num=int(input("Enter the integer value :"))
Rem=0
Rev=0
while(Num!=0):
    Rem=Num%10
    Rev=Rev*10+Rem
    Num=Num//10
print(Rev)    