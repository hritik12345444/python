# search if the word "learning" exists in the file or not

def check_for_word():
    word = "python"
    with open ("practice.txt",'r') as f:
        data = f.read()
        if(data.find(word) != -1):
            print("yes found")
        else:
            print("Not found")


check_for_word()