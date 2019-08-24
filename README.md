# Automate-the-Boring-Stuff-Using-Python
Simple Scripts that automate your daily tasks.

### #1) Empty File Folder Remover
  #### Problem:
        When I plug my Memory Card to My System, I Found lots of EMPTY Files and Folders (Created Since I installed
    many apps on android and Uninstall them later on). I want to remove all the empty folder and files(Most of the
    Files that i no longer need are in the range of 0-100 Bytes - But i may have some notes with smaller size too).

        I have written a script that loop through the Drive/directory infinitely and delete all files and folders 
    until I found no files and folders to delete.
  #### ISSUE:
#1) It can't identify the notes that i may have with less than 100 Bytes, and delete all the files with less than 100 Bytes.
        
   
### #2) Junk File Folder Generator
  #### Problem:
        In my Previous Script, Solved the problem of deleting the empty files and folders. To test the preformence
    I have written another script that creates lot of Empty Folders and Files.
        
  #### Warning:
        This script uses/creates lots of system interrupts if it run infinitely and may cause harm. So to Create
    junk files and folders use only fixed no. of iterations. If the script run Infinitely It keeps on generate 
    lots of junk folders and files in them.
  #### Legality:
        Running this script infinitely on someones system would fill his/her harddisk with lots of junk files.
        
![003](https://user-images.githubusercontent.com/46214838/63634331-74d1f900-c672-11e9-9116-0122275a42a2.PNG)
![004](https://user-images.githubusercontent.com/46214838/63634448-2d4c6c80-c674-11e9-82c9-5aaa72c80704.PNG)

      The script tool only 50 Sec to generate 3884 Folders and 432725 Files. But to delete those files it took
      387 Sec == 6.45 Min. 
![005](https://user-images.githubusercontent.com/46214838/63634431-fd9d6480-c673-11e9-8d45-b3613b3ffbec.PNG)
