#program for to input name and print its length
str1= input("enter you name")
print(len(str1))
#WAP to find the occurance of the "$" in a string 
str2= " hi suman \n how are you \n hope you are doing well "
count = str2.count('u')
print(count)
###################condition ifelse##################3
light="pink"
if(light == "red"):
    print("stop")     #indentation 
elif(light == "green"):
    print("go")
elif(light  == "yellow"):
    print("look")
else:
    print("light is broken")

print("end of the code")

################### WAP based on grade marks 
marks= int (input("enter the student marks :" )) 
if(marks>=90):
        print("Grade A")
elif(marks>=80 and marks <90):
        print("Grade B")
elif(marks>=70 and marks <80):
        print("grade C")
else:
      print("grade D")
################# Nesting :ek statment k dusri statament ##############
age=int(input("enter your age"))
if(age>=18):
      if(age>=80):
            print("cannot drive")
      else:
            print("can drive")
else:

      print("below 18 also not drive")
    
###### WAP to check if a number is entered by user is whether it is odd or even ##################
number = int(input("enter the number"))
if(number%2==0):
      print("its a even number")
else:
      print("it is an odd number")


########## WAP to find the greatest of 3 number entered by user 
number1 = int(input("enter the first number"))
number2 = int(input("enter the second number"))
number3 = int(input("enter the third number"))
if(number1 > number2 and number1 > number3):
      print("First number is greater")
elif(number2 > number3):
      print("second number is greater")
else:
      print("third number is greater")
      if(number1==number2 and number2 == number3):
            print("all are  equal")
      else:
            ("invalid entries")

############# WAP to check if it is a number of multiple of 7 or not 
X= int(input("enter the number"))
if(X%7==0):
      print("its a multiple of 7")
else:
      print("its not the multiple of 7")

######## WAP to check the greatest number of 4  
a=10
b=20
c=3
d=110  
if(a>b and a>c and a>d):
      print("a is greatest", a)
elif(b>c and b>d):
      print("b is greatest",b)
elif(c>d):
      print("c is greatest",c)
else:
      print("D is greatest",d)

###### WAP a program for a simple ATM program ##############

Balance=int(input("enter the amount you want to enter in your account"))
#print(" \n your  account balance in your account is :", Balance)
Withdraw=int(input("enter the withdrawl amunt from your account "))
if(Balance>=Withdraw):
      print("your money is deducted which is",Withdraw)
else:
      print("your amount is low" ) 
Rem=Balance-Withdraw
print(Rem)  




