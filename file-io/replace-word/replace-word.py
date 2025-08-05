with open ("file-io/replace-word/practice.txt","r") as f :
    data = f.read()      #read

new_data = data.replace("java","python")   #replace(overwrite)
print(new_data)          

with open ("practice.txt","w") as f :
    f.write(new_data)        #save new data 