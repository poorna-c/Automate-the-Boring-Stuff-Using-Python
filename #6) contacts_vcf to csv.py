f = open(r'c:\Users\Poorna Chand\Desktop\contacts.txt','r')
data = f.read()
contacts = []
while True:
    start = data.find("BEGIN:VCARD")
    end = data.find("END:VCARD")+len("END:VCARD")
    if start == -1 or end == -1:
        break
    contacts.append(data[start:end])
    data = data[end:]


'''
# Extracts names only...
for i in range(len(contacts)):
    fn_start = contacts[i].find("FN:")
    fn_line_end = contacts[i][fn_start:].find("\n")
    # print(contacts[i][fn_start:fn_start+fn_line_end])
    # print(fn_start,fn_start+fn_line_end)
'''

contacts_dict = {}
for i in range(len(contacts)):
    con = contacts[i].split("\n")
    con.remove("BEGIN:VCARD")
    con.remove("END:VCARD")
    con.remove("VERSION:2.1")
    con.pop(0)
    try:
        name = con[0][3:]
        number = con[1].split(":")[-1]
        number = number.replace("+91","")
        number = number.replace(" ","")
        number = int(number)
        contacts_dict[number]=name
    except:
        pass
    # print(con)


clipboard_copy_text = "name,number\n"
for i in contacts_dict:
    clipboard_copy_text += contacts_dict[i]+","+str(i)+"\n"

import pyperclip
pyperclip.copy(clipboard_copy_text)
# spam = pyperclip.paste()
print("All the contacts are copied to clipboard... Paste using(Ctrl + V)")
with open("contacts.csv","w") as f:
    f.write(pyperclip.paste())
