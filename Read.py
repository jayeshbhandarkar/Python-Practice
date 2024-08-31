# 27) WAP to create a file, write data into it and then read it in three different ways.

fname=input("\n\n Enter file name: ")

f=open(fname,"w+")
print("\n\n File Created Successfully")

print("\n\n Enter data to write to the file")
data=input()
f.write(data)
f.seek(0,0)
print("File Contents: ",f.read())
print("File Contents: ",f.readable())
print("File Contents: ",f.readlines())