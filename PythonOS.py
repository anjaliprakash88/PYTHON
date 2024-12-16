import os

# # posix', 'nt', 'os2', 'ce', 'java' and 'riscos'.
# print(os.name)
# os.mkdir("d:\\newdir")

# printing current directory
# print(os.getcwd())

# print ("Process abort after printing this line")
# #Abort the current running process
# os.abort()
# print ("Process abort before printing this line")


print("Current directory:" , os.getcwd())
#Create a new directory
os.mkdir("c:\\mydir")
#Change current working directory
os.chdir("c:\\mydir")
#Print new current working directory
print("Current directory now:" , os.getcwd())

