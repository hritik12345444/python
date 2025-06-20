# WAF that replace all occurrencews of "java" with "python" in above file

def replace_con():
    with open("practice.txt",'r') as f:
        data = f.read()
        new_data = data.replace("Java","python")  # string new string return krta hai original string me kuch change nahi krta hai
    print(new_data)


    with open("practice.txt",'w') as f:   
        f.write(new_data)    




replace_con()