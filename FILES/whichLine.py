# WAF to find in which line of the file does the word "learnig" occur first.
# Print -1 if word not found


def check_for_line():
    word = "python"
    with open ("practice.txt",'r') as f :
        count = 1
        data = True  # data false tbb hoga jabb usme empty string na aa jaye
        while(data) :
            data = f.readline()
            if(word in data):  # same as data.find(word) != -1
                print(count)
                break  # jaisse hi mill jaye uske aage code run na hona chahiye
            else :
                count+=1


check_for_line()