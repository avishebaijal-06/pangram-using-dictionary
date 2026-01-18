import random, string
a={}
students={
 "Alex":{   
"name":"Alex",
"age":12,
"Total Marks":87,
"favorite color":"green"
 }
}

print (students)
if "name" in students.keys():
    print ("yes")
if "green" in students.values():
    print ("yes")
for i in students:
    print (i,students[i])

for i in students.values():
    print (i)    