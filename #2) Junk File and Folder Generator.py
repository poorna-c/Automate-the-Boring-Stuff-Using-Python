import string
import random
import os

BASEDIR = input("Enter the drive/folder path where Folders need to be generated: ")
count = int(input("Enter no. of folders to generate: "))
deep = input("Want to increase depth of junk Folders:(y/n)? ")[0]
deep = True if deep=='y' else False
if not os.path.exists(BASEDIR):
    print("Your Junk Folder Is being created")
    os.mkdir(BASEDIR)
charset = string.ascii_letters+string.digits+"!@#$%^&()_+}{[]';,."

def createJunk(path,count,deep=False):
    for i in range(count):
        os.chdir(path)
        ustr = "".join(random.sample(charset,k=30))
        os.mkdir(ustr)
        if deep:
            for i in range(count):
                os.chdir(os.path.join(path,ustr))
                lstr = "".join(random.sample(charset,k=30))
                os.mkdir(lstr)
                # The Following code crates only one empty file in every folder
            	# os.chdir(os.path.join(path,ustr,lstr))
            	# istr = "".join(random.sample(charset,k=30))
            	# open(f"{istr}.txt",'w').close()

                # The below code creates Lots of empty files in one folder
                for i in range(count):
                	os.chdir(os.path.join(path,ustr,lstr))
                	istr = "".join(random.sample(charset,k=30))
                	open(f"{istr}.txt",'w').close()

createJunk(BASEDIR,count,deep)
