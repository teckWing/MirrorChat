
import gpt_2_simple as gpt2
from datetime import datetime
import random


# ! sender = "one_of_your_contacts"
# ! user ="INSERT_YOUR_NAME_ON_WHATSAPP"

user = input("Enter your Whatsapp name ---> ")
sender = input("Enter who you want to chat with ---> ")


save_yn = input("Do you want to save the chat? (y/n) ---> ")
save = True if save_yn == 'y' else False

print("To end the chat press CTRL+C \n")

prefix=""
c=0
chat =""
sess = gpt2.start_tf_sess()

gpt2.load_gpt2(sess, checkpoint_dir="checkpoint/", run_name='mirrorChat',reuse=True)
while True:
    try:
    
        prompt = input("Enter the message: ")
        prefix += sender +":\n"+ prompt +"\n"+"\n"
        results = gpt2.generate(sess, run_name='mirrorChat', temperature=0.9, nsamples=3, batch_size=3, prefix=prefix + "\n\n" + user + ":\n", length=250, return_as_list=True, include_prefix=False, truncate="\n\n")
        res_split = random.choice(results).split('\n')[0]
        print(user+": "+res_split)

        chat+= sender +":\n"+ prompt +"\n"+"\n" + user +":\n"+res_split+"\n"+"\n"
        c+=1
        if c<=5:
            prefix+=user +":\n"+res_split+"\n"+"\n"
        else:
            c=0
            lines = prefix.splitlines()
            lines = lines[6:]
            prefix= '\n'.join(lines)
    except KeyboardInterrupt:
        if save:
          with open("chat.txt","w") as f:
            f.write(chat)
        break  
      

