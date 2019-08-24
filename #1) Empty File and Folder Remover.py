import os
BASEDIR = input("Enter your Drive/Folder Path to delete empty directories : ") 
os.chdir(BASEDIR)
FoundEmptyDirs = True
FolderCount = 0
FileCount = 0
FileDelete = False
while FoundEmptyDirs:
    DriveList = list(os.walk(os.getcwd()))
    pastDriveListLength = len(DriveList)
    for path,directories,files in DriveList:
        FileDelete = False
        for file in files:
            delFile = path+'\\'+file
            if os.stat(delFile).st_size == 0:
                print("FILE :",delFile)
                os.remove(delFile)
                FileCount+=1
                FileDelete = True
        if directories == [] and files == [] and path!=BASEDIR:
        	print(path)
        	os.rmdir(path)
        	FolderCount+=1
        	DriveList.remove((path,directories,files))
    # When ever the folder contains files, The folder won't delete. And Only the empty files will be deleted.
    # On the first loop the empty file will be deleted.
    # In some cases only files will be deleted and the folder count remain same.
    # Since we have used the logic of Folder count to break the loop. The Script only deletes the file and Exit since folder count remain same.
    # Hence, Just for re-verifing continueing the script once again to confirm no folder to delete....
    if FileDelete:
        continue
        
    if len(DriveList) == pastDriveListLength:
        FoundEmptyDirs = False

print("\n\nTOTAL EMPTY FOLDERS DELETED :",FolderCount)
print("TOTAL EMPTY FILES DELETED :",FileCount)