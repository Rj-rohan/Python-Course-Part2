#  File I/O in Python

#  Used to perform some operations on Files
# Create demo.txt file and then do.......

# 1) To read the entire file
# f=open("demo.txt","r")       #demo.txt is a file name AND "r" be the "mode"
# data=f.read()                # Also pass any value like data=f.read(6), give output by printing 1st 6 characters.....  
# print(data)
# f.close()



# 2) To read the single line

# f=open("demo.txt","r")
# data=f.readline()          # By default read 1st line of file
# print(data)
# f.close()


#  3) Writing in file
#  Create hi.txt file then do.......
#   When you are writing some text in file is "w"=mode 
#   When you are append (Add text at end) some text in file is "a"=mode 
#   when you are in append mode or in writing mode if you are not creating file it automatically create 

# f=open("hi.txt","w")      
# f.write("Hii You are very smart \n You are looking very happy\t How are you")
# f.close()

#    4)  "r+" mode for overwrite the existing data i.e file text replaces

# f=open("demo.txt","r+")   
# f.write("it is very nice")
# print(f.read())
# f.close()

#  "w+" == open for reading and writing. The file is created if it does not exist
#     ,Otherwise it is truncated. The strean is positioned at the beginning of the life.abs

# f=open("demo.txt","w+")   
# print(f.read())
# f.write("tyr")
# f.close()

#  with syntax 

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("Tesla is amazing car")


