def membaca(file):
    with open(file, "r") as file.txt:
        file_content = file.txt.read()
        print(file_content)

def menulis(file):
    
    membaca("file.txt")

    Hobi = input("Hobi: ")
    text = "\n {}".format(Hobi)


    with open(file, "a") as file_hobi:
        file_hobi.write(text)

menulis("file.txt")