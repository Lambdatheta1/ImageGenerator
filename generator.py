#Import the required Libraries
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import urllib.request
import openai

openai.api_key = ("Enter your API key")

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("1500x600")


def display_text():
    global entry
    string= entry.get()
    label.configure(text=string)
    try:
        label.configure(text="done")
        response = openai.Image.create(prompt=string,n=10,size="256x256")
        for i in range(10):
            image_url = response['data'][i]['url']
            urllib.request.urlretrieve(image_url,"temp/gfg"+str(i)+".png")
    except:
        label.configure(text="Error")
    
    
def reload_picture():
    label.configure(text="displayed")
    for i in range(10):
        myimage1 = Image.open("temp/gfg"+str(i)+".png")
        mytest = ImageTk.PhotoImage(myimage1)
        labels[i].configure(image=mytest)
        labels[i].image=mytest
imgs=[]
labels = []
for i in range(10):
#    imgs.append(ImageTk.PhotoImage(Image.open("gfg"+str(i)+".png")))
    #try:
        #imgs.append(ImageTk.PhotoImage(Image.open("temp/gfg"+str(i)+".png")))
        #labels.append(Label(win, image=imgs[-1], width=256, height=256))#.grid()
    #except:
    labels.append(Label(win, width=256, height=256))
    if i<5:
        labels[i].place(x=i*300+30, y=200)
    elif i>=5:
        labels[i].place(x=(i-5)*300+30, y=456)
#Initialize a Label to display the User Input
label=Label(win,text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)
ttk.Button(win, text= "Refresh Pictures",width= 20, command= reload_picture).pack(pady=20)


win.mainloop()