# search if the word "learning" exists in the file or not

with open("practice.txt",'r') as f:
    data = f.read()
    if(data.find("Hi") != -1):   # stirn return -1 while data is not present 
        print("yes")
    else:
        print("no")    