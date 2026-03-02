subject1 ={"python","java","c++","python","java","javascript","c++","c","java","javascript","C++"}
print(subject1)
print(len(subject1))
subject2= subject1.copy()
No_of_classroom =subject2
print(len(No_of_classroom))

dict_1= set()
dict_1.add(28)
dict_1.add(56)
dict_1.add(79)
print(dict_1)
print(type(dict_1))
dict2=dict.fromkeys(dict_1,0)
print(type(dict2))
print(dict2)

chemistry=int(input("chemsisry marks :"))
biology=int(input("biology marks:"))
physics=int(input("physics marks:"))

print(chemistry,biology,physics)
marks=(chemistry,biology,physics) 
print(marks)
print(type(marks)) 

dict_3={}
x= int(input("physics:"))
dict_3.update({"physics": x})
y= int(input("chem:"))
dict_3.update({"chem": y})
z= int(input("bio:"))
dict_3.update({"bio": z})
print(dict_3)
print(type(dict_3))



#dict.add(98)
#dict.add(10)
#dict.add(45)
#print(dict)


#print(dict.marks)



