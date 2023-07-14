import os
import json

choice=int(input("Welcome to file handler.\n1. Add Student.\n2. Show Student.\n3. Delete Student.\n4. Edit Student.\n Enter Your Choice: "))

if choice==1:
    name=input("Enter student name ")
    phone=int(input("Enter phone number "))
    age=int(input("Enter your age "))
    city=input("Enter your city name ")
    student={"Name":name,"Phone":phone,"Age":age,"City":city}
    f = open("students/"+name.lower()+".json", "w")
    json.dump(student, f, indent=4)

elif choice==2:
    files = os.listdir("students")
    print(files)   
    for filename in files:
        file = open("students/"+filename, "r",)
        student = json.load(file)
        print(f"Name: {student['Name']}\nPhone: {student['Phone']}\nage:{student['Age']}\ncity:{student['City']}\n")

elif choice==3:
    try:
        filename=input("Enter the file name ")
        f=open("students/"+filename+".json","r")
        load = json.load(f)
        print(load)
        print(f"Data deleted sucessfully.\n\nName: {load['Name']}\nPhone:{load['Phone']}\nAge:{load['Age']}\nCity:{load['City']}")
        os.remove("students/"+filename+".json")
    except:
        print("Name does't exist")

elif choice==4:
    filename=input("Enter your file name to edit ")

    if filename+".json" not in os.listdir('students'):
        print("file doesn't exist")
    else:
        f=open("students/"+filename+".json","r")
        load = json.load(f)
        print(load)
        print(f"You're editing.\n\nName: {load['Name']}\nPhone:{load['Phone']}\nAge:{load['Age']}\nCity:{load['City']}")
        f=open("students/"+filename+".json","w")

        phone=int(input("Enter phone number "))
        age=int(input("Enter your age "))
        city=input("Enter your city name ")
        load.update({"Phone":phone,"Age":age,"City":city})
        json.dump(load,f,indent=4)
    
    