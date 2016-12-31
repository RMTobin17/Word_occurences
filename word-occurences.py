filename = input('Please type in the document you want to result ')
def load_content(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content

def load_dictionary(content):
    my_list = content.split()
    strip_duplicates(my_list)

def strip_duplicates(my_list):
    count = len(my_list)
    while count > 0:
        count = count -1
        word = my_list[count]
        print (word)

def analyze_content(content):
    load_dictionary(content)
    
content = load_content(filename)
analyze_content(content)
