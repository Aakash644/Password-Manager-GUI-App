from tkinter  import * 
from tkinter import messagebox  
import random

import pyperclip 
import json
window=Tk()   
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passfunc(num=10):   
    password_entry.delete(0,END)
    password="1234567890qwertyuioplkjhgfdsazxcvbnm!@$%&*" 
    #8 digits of password   
    pass1=""
    for i in range(0,num):
       pass1+=(password[random.randint(0,len(password)-1)])  
    password_entry.insert(0,pass1) 
    pyperclip.copy(pass1)
    



# ---------------------------- SAVE PASSWORD ------------------------------- # 

def save():
    username=website_entry.get()
    useremail=email_entry.get()
    userpassword=password_entry.get()   
    inform={username:{"email":useremail,"password":userpassword}}
    if(len(username)==0 or len(useremail)==0 or len(userpassword)==0 ):
        messagebox.showinfo(title="Oops",message="You left some field empty!") 
        
    else:
        response=messagebox.askokcancel(title="Website",message=f"These are your entered details:\nEmail:{username}\nPassword:{userpassword}\nIs that correct or not?")
        if(response==True):
            try:
                with open(r"C:\Users\Acer\Downloads\password-manager-start\data.json","r") as data:
                  old_data=json.load(data)
                  old_data.update(inform) 
            except FileNotFoundError:
                with open(r"C:\Users\Acer\Downloads\password-manager-start\data.json","w") as data:
                  json.dump(inform,data,indent=4)
            else:
                with open(r"C:\Users\Acer\Downloads\password-manager-start\data.json","w") as data:
                  json.dump(old_data,data,indent=4)
    
            website_entry.delete(0,END) 
            email_entry.delete(0,END) 
            password_entry.delete(0,END)

    
def search ():
    try:
        with open(r"C:\Users\Acer\Downloads\password-manager-start\data.json","r") as data:
            old_data=json.load(data)
            search_data=website_entry.get() 
            if search_data in old_data:
                email=old_data[search_data]["email"] 
                password=old_data[search_data]["password"]
                messagebox.showinfo(title="Details",message=f"Your details are:\nemail:{email}\npassword:{password}")
            else:
                messagebox.showinfo(title="Oops",message="Your details are not found!")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops",message="Your details are not found!")
    

                    
                    
# ---------------------------- UI SETUP ------------------------------- # 

window.config(padx=20,pady=20,bg="white")
window.title("Password Manager")
canvas=Canvas(width=200,height=200,bg="white",highlightthickness=0)  
tomato=PhotoImage(file=r"C:\Users\Acer\Downloads\password-manager-start\logo.png") # adding photoimage 
canvas.create_image(100,100,image=tomato)
canvas.grid(row=0,column=1,columnspan=2) 
website_label=Label(text="Website:",bg="white",font=("Arial",15,"normal")) 
website_label.grid(row=1,column=0)
email_label=Label(text="Email:",bg="white",font=("Arial",15,"normal"))
email_label.grid(row=2,column=0)
password_label=Label(text="Password:",bg="white",font=("Arial",15,"normal"))
password_label.grid(row=3,column=0) 

#entries
website_entry=Entry(width=22,border=2)  

website_entry.focus() 
search_button=Button(width=15,text="search",command=search)
search_button.grid(column=2,row=1)
website_entry.grid(row=1,column=1,columnspan=1) 
email_entry=Entry(width=42,border=2) 

email_entry.grid(row=2,column=1,columnspan=2)
password_entry=Entry(width=21,border=2) 

password_entry.grid(row=3,column=1) 

# adding buttons 
gener_password=Button(text="Generate Password",command=passfunc) 
gener_password.grid(row=3,column=2) 

add_button=Button(text="Add",width=35,command=save) 
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()


