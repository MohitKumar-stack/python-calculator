from tkinter import *

def click(event):    
    global data,entrydata
    input_data =event.widget.cget("text") 
    if input_data =="=":
        if data.get().isdigit():
            value =int(data.get())
        else:
            value =eval(entrydata.get())
            data.set(value)
            entrydata.update()
    elif input_data =="C":
        data.set(" ")
        entrydata.update()
    else:
        data.set(data.get()+input_data)
        entrydata.update()


def done():
    root =Tk()
    root.geometry("250x338")
    root.resizable(0,0)
    root.title("Calucater")
    # root.wm_iconbitmap("pic.jpg")

    global data,entrydata
    data =StringVar()

    entrydata =Entry(root,textvariable =data,font ="lucida 20",justify=RIGHT)
    entrydata.pack(fill =X,pady =9,ipady =10)

    frame1 =Frame(root)
    button1 =Button(frame1,text ="1",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame1,text ="2",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame1,text ="3",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame1,text ="+",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    frame1.pack()
    
    frame2 =Frame(root)
    button1 =Button(frame2,text ="4",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame2,text ="5",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame2,text ="6",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame2,text ="-",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    frame2.pack()
    
    frame3 =Frame(root)
    button1 =Button(frame3,text ="7",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame3,text ="8",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame3,text ="9",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame3,text ="*",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    frame3.pack()
    
    frame4 =Frame(root)
    button1 =Button(frame4,text ="C",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame4,text ="0",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame4,text ="=",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    button1 =Button(frame4,text ="/",width =3,font ="lucida 25")
    button1.bind("<Button-1>",click)
    button1.pack(side =LEFT,expand =True)
    frame4.pack()

    root.mainloop()

if __name__=="__main__":
   done() 
     
