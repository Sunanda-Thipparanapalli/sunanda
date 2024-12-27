StudentName=input("Enter a Student Name:")
Sub1=int(input("Enter The Subject1 Marks :"))
Sub2=int(input("Enter The Subject2 Marks :"))
Sub3=int(input("Enter The Subject3 Marks :"))
Total=0
Average=0
print("Student Report Card :")
print("---------------")
print("Student Name :",StudentName)
print("Student1 :",Sub1)
print("Student2 :",Sub2)
print("Student3 :",Sub3)  
if(Sub1>=35 and Sub2>=35 and Sub3>=35):
    total=Sub1+Sub2+Sub3
    print("Total :",Total)
    Average=Total/3
    print("Average :",Average)
    if(Average>=90):
         print("congratulations you have qualified in 1st class...!")
    elif(Average>=75):
         print("congratulations you have qualified in 2nd class...!")
    else:
         print("congratulations you have qualified in 3rd class...!")
else:
    print("Better Luck Next Time")
   
