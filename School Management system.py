arr1=[]
arr2=[]
arr3=[]
arr4=[]
arr5=[]
total=0
def enter():
    global total
    choice=int(input("How many students data do you want to enter : "))
    total=total+choice
    for i in range(choice):
        print("Enter data of student : ",i+1)
        arr1.append(input("Enter name : "))
        arr2.append(input("Enter Roll no : "))
        arr3.append(input("Enter course : "))
        arr4.append(input("Enter class : "))
        arr5.append(input("Enter contact : "))

def show():
    for i in range(total):
        print("\nData of Student ",i+1)
        print("Name : ",arr1[i])
        print("Roll no : ",arr2[i])
        print("Course : ",arr3[i])
        print("Class : ",arr4[i])
        print("Contact : ",arr5[i])

def search():
    rollno=input("Enter the roll no of student :")
    for i in range(total):
        if rollno==arr2[i]:
            print("Name : ",arr1[i])
            print("Roll no : ",arr2[i])
            print("Course : ",arr3[i])
            print("Class : ",arr4[i])
            print("Contact : ",arr5[i])
        else:
            print("Enter a valid roll number")


while(True):
    print("Press 1 to enter data")
    print("Press 2 to show data")
    print("Press 3 to search data")
    value=int(input())
    if value==1:
        enter()
    elif value==2:
        show()
    elif value==3:
        search()