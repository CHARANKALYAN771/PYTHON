import os

print(dir(os))                       #--> prints all directories
print(os.getcwd())                   # --> gives the present location of dir
os.chdir("c:\\")                     # --> we can change the dir 
print(os.getcwd())     
print(os.listdir())                  #--> lists out all directories
os.mkdir("this")                     # --> makes a single directory
os.makedirs("that/that")             # --> makes multiple directories
os.rename("intro.txt","intro.txt")   # --> we can rename
print(os.environ.get("path"))        # --> we get evnironment location
print(os.path.join("c:\\","t.xls"))  #--> joins 2 paths
print(os.path.exists("test1.xls"))   # --> tells us if path is present or not

