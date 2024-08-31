# 28) WAP to open a file, write data into it and then read it in three different ways.

fname = input("Enter file name:")

with open(fname,"a+")as f:
    print("File Created Successfully")
    
    print("Enter data to write to the file")
    data = input()
    f.write(data)
    f.seek(0,0)
    print("File contents:",f.read())