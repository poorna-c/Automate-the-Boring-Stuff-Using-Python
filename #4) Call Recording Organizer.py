import os
import re

done = False
while not done:
	done = True
	choice = input("Do you want to specify the path(y/N)? ")[0].lower()
	if choice == 'y':
		BASEDIR = input("Enter Path: ")
	elif choice == 'n':
		BASEDIR = os.path.dirname(__file__)
	else:
		print("Invalid Input!!!\a")
		done = False
os.chdir(BASEDIR)
recordings = os.listdir(os.getcwd())

for recording in recordings:
    try:
        phone = re.findall("\(\d+\)",recording)
        name = re.findall(".*\(", recording)[0][:-1].strip()
        if os.path.exists(name):
            os.system(f'move "{recording}" "{name}/"')
            print(f'move "{recording}" "{name}/"')
        else:
            os.makedirs(name)
            os.system(f'move "{recording}" "{name}/"')
            print(f'move "{recording}" "{name}/"')
    except:
        pass

# for recording in recordings:
#     data = recording.split(')_')[0].split('(')
#     if len(data) == 2:
#         name,phone = data
#         name=name.strip()
#         if os.path.exists(name):
#             os.system(f'move "{recording}" "{name}/"')
#             print(f'move "{recording}" "{name}/"')
#         else:
#             os.makedirs(name)
#             os.system(f'move "{recording}" "{name}/"')
#             print(f'move "{recording}" "{name}/"')
