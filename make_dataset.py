import re
import os
import zipfile
import shutil

print("\n Make sure you have all your zipped/unzipped chat in a folder before continuing. \n")

# ! unzip=False
unzip_yn = input("Have you unzipped the chat (y/n) ---> ")
unzip = False if unzip_yn == 'y' else True



path_dir_chats = "chats/"
if os.path.isdir(path_dir_chats)==False:
    os.makedirs(path_dir_chats)
if unzip:
    path_dir_zipchat = input("Where are the chat located? Insert the path ---> ")
    count =sum(1 for file_name in os.listdir(path_dir_zipchat) if file_name.startswith('WhatsApp'))
    print("Found " + str(count) + " chats.")
    for x in os.listdir(path_dir_zipchat):
        if x.startswith("WhatsApp"):
            print(x)
            with zipfile.ZipFile(path_dir_zipchat+"/"+x, 'r') as zip_ref:
                zip_ref.extractall(path_dir_chats)
                os.rename(path_dir_chats+"/_chat.txt",path_dir_chats+"/chat"+str(len(os.listdir(path_dir_chats)))+".txt")
else:
    path_dir_zipchat = input("Where are the chat located? Insert the path ---> ")
    count =sum(1 for file_name in os.listdir(path_dir_zipchat) if file_name.startswith('chat'))
    print("Found " + str(count) + " chats.")

if count!=0:
    # regex for what you want to delete
    to_remove =  r'((?:immagine omessa|audio omesso|sticker non incluso|video omesso|Chiamata vocale persa|Videochiamata persa|Hai bloccato questo contatto|Hai sbloccato questo contatto|image omitted|audio omitted|sticker omitted|video omitted|Missed group voice call|Missed group video call|Missed voice call|Missed video call|You blocked this contact|You unblocked this contact))'
    unicode_remove = r'[\u202a\u202d\u200e\u202c\u200e]'
    space_pattern = r"\s{2,}"
    def clean_text(s):
        s=re.sub(to_remove, "", s)
        s=re.sub(unicode_remove, "", s)
        s=re.sub(space_pattern, "", s)
        return s.lower()
        
    pattern = r"^\[\d{2}/\d{2}/\d{2}, \d{2}:\d{2}:\d{2}\] (.*?): (.*)"
    # ! user ="INSERT_YOUR_NAME_ON_WHATSAPP"
    
    with open("data.txt","w", encoding="utf-8") :
        pass
    for file in os.listdir(path_dir_chats):
        with open(path_dir_chats+file, "r", encoding="utf-8",errors='replace') as f:
            
            lines = f.readlines()
            i=2
            line = clean_text(lines[1])
            match = re.findall(pattern, line)
            
            while len(match)==0:
                    line = clean_text(lines[i])
                    match = re.findall(pattern, line)
                    i+=1
            sender, message =  match[0][0],match[0][1]
            user=sender
            while i<len(lines):
                prompt =""
                while i<len(lines) and sender.startswith(user):
                    prompt+=" "+message
                    line = clean_text(lines[i])
                    match = re.findall(pattern, line)
                    if len(match)==0:
                            message = ""
                    else:
                            sender, message =  match[0][0],match[0][1]
                        
                    
                    i+=1
                name = "unknown" if  bool(re.match(r"\+\d{11}", user))  else user
                user=sender
                
                prompt = re.sub(r'\s{2,}', ' ', prompt)[1:]
                if re.match(r'^\s*$',prompt)==None and len(prompt)<=1000 : 
                    with open("data.txt","a", encoding="utf-8") as f:
                        f.write(name+":\n")
                        f.write(prompt+"\n")
                        f.write("\n")
                        
                
    # Fake chats with personal info
    data=[]  #ex. {"prompt":"How old are you?","completion":"Hello, I am 23 years old"}
                
    if len(data)>0:
        for x in data:
            with open("data.txt","a", encoding="utf-8") as f:
                            f.write("unknown"+":\n")
                            f.write(x["prompt"].lower()+"\n")
                            f.write("\n")
                            f.write(user+":\n")
                            f.write(x["completion"].lower()+"\n")
                            f.write("\n")
    shutil.rmtree("chats/")
else:
    print("No data available! Check the path")