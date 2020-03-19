import os
try:
    os.chdir(input('Enter Path :'))
except Exception as e:
    print("Error :",e)
print("initializing...")
video_count,audio_count,image_count,file_count,compress_count,count = 0, 0, 0, 0, 0, 0

audio_file_ext = ["mp3","wav"]
video_file_ext = ["mp4","avi","3gp","webm","flv","mov","mkv"]
image_file_ext = ["jpg","png","jpeg","tiff","gif","tif"]
files_file_ext = ["js","css","py","csv","html","txt","doc","docx","xml","pdf","xls","xlsx","ppt"]
exe_cmp_ext = ["exe","zip","rar","msi","tar","xz","7z","tgz","iso"]


def get_file_name(ext):
    global video_count,audio_count,image_count,file_count,compress_count,count
    if ext in video_file_ext:
        video_count += 1
        return 'video_'+str(video_count).zfill(4)
    elif ext in audio_file_ext:
        audio_count += 1
        return 'audio_'+str(audio_count).zfill(4)
    elif ext in image_file_ext:
        image_count += 1
        return 'image_'+str(image_count).zfill(4)
    elif ext in files_file_ext:
        files_count += 1
        return 'file_'+str(files_count).zfill(4)
    elif ext in ext_cmp_ext:
        compress_count += 1
        return 'exe_cmp_'+str(compress_count).zfill(4)
    else:
        count+=1
        return 'Unidentified_'+str(count).zfill(4)

print("Starting Process:")

items = os.listdir(os.getcwd())
print("Found {} items".format(len(items)))
for item in items:
    ext = os.path.splitext(item)[-1][1:]
    if os.path.isfile(item):
        new_name = get_file_name(ext)+'.'+str(ext)
        try:
            os.rename(item,new_name)
            print("Renaming : {item} -> {new_name}".format(item=item,new_name=new_name))
        except Exception as e:
            print("Skipping file : {}".format(item))
