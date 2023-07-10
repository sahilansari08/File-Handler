import os
def write_file():
    filename=input("Enter the filename: ")
    content = input("give message for add in your file: ")
    file=open(filename+".txt","w")
    file.write(content)

def read_file():
    filename=input("Enter the filename: ")
    try:
        f=open(filename+".txt","r")
        print(f.read())
    except:
        print("404 - File not found")

def delete_file():
    filename=input("Enter the file name ")
    try:
        os.remove(filename+".txt")
    except:
        print("file not exist")

user=int(input("\nWelcome to File Handler :)\n\n1. Write a file.\n2. Read a File.\n3. Delete a file.\nEnter your choice: "))
if user==1:
    write_file()
elif user==2:
    read_file()
elif user==3:
    delete_file()
else:
    print("Wrong choice")

