from tkinter import *
from PIL import Image,ImageTk
from random import randint

frame=Tk()
frame.title("rock papaer scissor")
frame.configure(background='black')
image_rock1=ImageTk.PhotoImage(Image.open('rock.png'))
image_paper1=ImageTk.PhotoImage(Image.open('paper.png'))
image_scissor1=ImageTk.PhotoImage(Image.open('scissors.png'))
image_rock2=ImageTk.PhotoImage(Image.open('rock.png'))
image_paper2=ImageTk.PhotoImage(Image.open('paper.png'))
image_scissor2=ImageTk.PhotoImage(Image.open('scissors.png'))

label_player=Label(frame,image=image_scissor2)
label_computer=Label(frame,image=image_scissor1)
label_computer.grid(row=1,column=1)
label_player.grid(row=1,column=4)
score_computer=Label(frame,text="0",font=("arial",40,"bold"),fg='blue')
score_player=Label(frame,text="0",font=("arial",40,"bold"),fg="blue")
score_computer.grid(row=1,column=2)
score_player.grid(row=1,column=3)

name_score_computer=Label(frame,text="computer",height=1,width=7,font=("arial",16,"bold"),bg="blue",fg="white")
name_score_computer.grid(row=0,column=1)
name_score_player=Label(frame,text="player",font=("arial",16,"bold"),bg="blue",fg="white")
name_score_player.grid(row=0,column=4)
final_message=Label(frame,font=("arial",30,"bold"),bg="yellow",fg="red")
final_message.grid(row=3,column=2)

def Message_Updation(a):
    final_message['text']=a

def Computer_Updation():
    final=int(score_computer['text'])
    final=final+1
    score_computer['text']=str(final)
def User_Updation():
    final=int(score_player['text'])
    final=final+1
    score_player['text']=str(final)
def Winner_Cheack(p,c):
    if(p==c):
        Message_Updation('It is a Draw !!')
    if p=="rock":
        if c=="paper":
            Message_Updation("Computer Wins !!")
            Computer_Updation()
        if c=="scissor":
            Message_Updation("Player Wins !!")
            User_Updation()
    elif p=="paper":
        if c=="scissor":
            Message_Updation("Computer Wins !!")
            Computer_Updation()
        if c=="rock":
            Message_Updation("Player Wins !!")
            User_Updation()
    elif p=="scissor":
        if c=="rock":
            Message_Updation("Computer Wins !!")
            Computer_Updation()
        if c=="paper":
            Message_Updation("Player Wins !!")
            User_Updation()
comp_select=['rock','paper','scissor']

def choice_update(choice_user):
    choice_computer=comp_select[randint(0,2)]
    if(choice_computer=='rock'):
        label_computer.configure(image=image_rock1)
    elif(choice_computer=="paper"):
        label_computer.configure(image=image_paper1)
    else:
        label_computer.configure(image=image_scissor1)
    
    if(choice_user=='rock'):
        label_player.configure(image=image_rock2)
    elif(choice_user=='paper'):
        label_player.configure(image=image_paper2)
    else:
        label_player.configure(image=image_scissor2)
    Winner_Cheack(choice_user,choice_computer)
def reset():
    score_computer['text']="0"
    score_player["text"]="0"
    label_computer.configure(image=image_scissor1)
    label_computer.configure(image=image_scissor2)
    final_message["text"]=None
        
    
    
    




rock_button=Button(frame,width=10,height=2,text='ROCK',font=("Times New Roman",20,"bold"),bg='red',fg='white',command=lambda:choice_update('rock')).grid(row=2,column=1)
paper_button=Button(frame,width=10,height=2,text="PAPER",font=("Times New Roman",20,"bold"),bg="red",fg="white",command=lambda:choice_update('paper')).grid(row=2,column=2)
scissor_button=Button(frame,width=10,height=2,text="SCISSOR",font=("Times New Roman",20,"bold"),bg="red",fg="white",command=lambda:choice_update('scissor')).grid(row=2,column=3)
reset_button=Button(frame,width=10,height=2,text='RESET',font=("Times New Roman",20,"bold"),bg="blue",fg="white",command=reset).grid(row=3,column=4)



frame.mainloop()
