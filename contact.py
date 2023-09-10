import json
try:
    with open("dict.json", "r") as file:
        d = json.load(file)
except FileNotFoundError:
    d = {}
    print("Error!")
n=int(input("1:Add Number\n2:Search Number\n3:Delete Number\n"))
if n==1:
    n=int(input("how many contact do you want to add:"))
    for i in range(n):
        nmbr=int(input("Enter Number:"))
        name=input("Enter name:")
        d[name]=nmbr
    with open("dict.json","w") as file:
        json.dump(d,file)
elif n==2:
    n=int(input("1:Search with Name\n2:Search with Number\n"))
    if n==1:
        name=input("Enter Name:")
        if name in d:
            print(d[name])
        else:
            print("NotFound!")
    elif n==2:
        nmbr=int(input("Enter Number:"))
        for na,nm in d.items():
            if nm==nmbr:
                print(f"Name:{na}\tNumber:{nm}")
elif n==3:
    n=int(input("1:Delete with Name\n2:Delete with Number:"))
    if n==1:
        name=input("Enter Name:")
        with open("dict.json",'r') as file:
            data=json.load(file)
        if name in data.keys():
            del data[name]
            print("deleted")
        with open("dict.json","w+")as f:
            json.dump(data,f)
    elif n==2:
        nmbr=int(input("Enter Number:"))
        with open("dict.json","r")as file:
            data=json.load(file)
        for na,nm in data.items():
            if nm==nmbr:
                del data[nm]
        with open("dict.json","w+")as f:
            json.dump(data,f)
    else:
        print("Wrong Input!")