file = open("myfile.txt", "w")
file.write("Hello! My name is Sriram")
file.close()
#read
file=open("myfile.txt","r")
content=file.read()
file.close()
print(content)
#append
file=open("myfile.txt","a")
file.write( "iam from town ")
file.close()
#read
file=open("myfile.txt","r")
content=file.read()
file.close()
print(content)