# From a file containing numbers separated by comma, print the count of even numbers.

with open ("number.txt",'r') as f:
    data = f.read()
    print(data)
    print(len(data))
    i = 0      
    num = ""   
    count = 0
    while(i < len(data)):
        if(data[i] == ','):
            # print(num)
            if(int(num) % 2 == 0):   # here only num is a string we have to convernt into integer
                count +=1
            num = ""
        else:
            num += data[i]
        i+=1   

print(count)