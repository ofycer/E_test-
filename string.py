str1="this is my name suman"
str2= 'suman'
str3=''' hi suman'''
print(str1)
str4= "this is a string .\t we are working on python"
print(str4)
#Basic Operation : concatination **********************
str5 ="hi suman \n"
str6 ="how are you"
print(str5+str6)
print(len(str5))
print(len(str6))
str7= int (input("enter you name")) 
print(type(str7)) 
#############Indexing : jab b koi character store hota h to particular character ki apni ek position hoti hai ################33
str8 = "this is my vs code"
#str8[3] = "n"
#code =str8[3]
print(str8[3]) 
######## slicing ################
##strl[starting_inx:ending_inx]
str = "suman apna college"
print(str[1:4])   
print(str[:3]) #same as str[0:4]
print(str[1:])  #same as str[1:len(str)]
print(str[-3:-1])
print(str[-2:])
print(str[:-4])  
str="i a stydying pythan in apna college"
str90= str.capitalize()
str91= "pagal"
print(str90)
print(str.endswith("ge"))
print(str.capitalize())
print(str.replace("p","s"))
print(str.find("s"))
