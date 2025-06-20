# WAF to find in which line of the file does the word "learnig" occur first.
# Print -1 if word not found


def check_for_word():
    word = "python"
    with open ("practice.txt",'r') as f:
        data = f.read()
        if(data.find(word) != -1):
            print("yes found")
        else:
            print("Not found")


check_for_word()