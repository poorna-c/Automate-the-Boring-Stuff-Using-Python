import os

basepath = input("Enter Path: ")
os.chdir(basepath)
whitelist = ["Videos","Images","Files","Music","compressed_iso_and_exegutables","Others"]

if not os.path.exists("Images"):
    print("Creating Images Folder")
    os.mkdir("Images")
if not os.path.exists("Videos"):
    print("Creating Videos Folder")
    os.mkdir("Videos")
if not os.path.exists("Files"):
    print("Creating Files Folder")
    os.mkdir("Files")
if not os.path.exists("Music"):
    print("Creating Files Folder")
    os.mkdir("Music")
if not os.path.exists("compressed_iso_and_exegutables"):
    os.mkdir("compressed_iso_and_exegutables")
if not os.path.exists("Others"):
    os.mkdir("Others")

def moveItems(basepath,path,fmt,folder):
    if os.path.basename(path) not in whitelist:
        _ = os.system(rf'move "{path}\*.{fmt}" "{basepath}\{folder}"')
        print(rf'move "{path}\*.{fmt}" "{basepath}\{folder}"')

music_file_ext = ["mp3","wav"]
video_file_ext = ["mp4","avi","3gp","webm","flv","mov","mkv"]
image_file_ext = ["jpg","png","jpeg","tiff","gif","tif"]
files_file_ext = ["js","css","py","csv","html","txt","doc","docx","xml","pdf","xls","xlsx","ppt"]
exe_cmp_ext = ["exe","zip","rar","msi","tar","xz","7z","tgz","iso"]

for path,dirs,files in os.walk(os.getcwd()):
    extentions_present = []
    for item in image_file_ext:
        if item in str(files).lower():
            extentions_present.append((item,"Images"))

    for item in video_file_ext:
        if item in str(files).lower():
            extentions_present.append((item,"Videos"))

    for item in music_file_ext:
        if item in str(files).lower():
            extentions_present.append((item,"Music"))

    for item in files_file_ext:
        if item in str(files).lower():
            extentions_present.append((item,"Files"))

    for item in exe_cmp_ext:
        if item in str(files).lower():
            extentions_present.append((item,"compressed_iso_and_exegutables"))

    for extention in extentions_present:
        moveItems(basepath,path,extention[0],extention[1])
    moveItems(basepath,path,"*","Others")
