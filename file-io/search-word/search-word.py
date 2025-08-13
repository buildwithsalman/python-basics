word = "python"
with open ("file-io/search-word/practice.txt", "r") as f :
    data = f.read()
    if (word in data):
        print("found")
    else:
        print("not found")
