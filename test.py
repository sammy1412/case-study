from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.title('game')
window.geometry('1200x1000')
window.config(bg = 'black')

def select(event):
    b=event.widget
    value= b['text']

    for i in range(10):
        if value == correct_answers[i]:
            if value == correct_answers[9]:  #win and play again
                    
                def close():
                    root1.destroy()
                    window.destroy()

                def playagain():
                    root1.destroy()
                    question_area.delete(1.0,END )
                    question_area.insert(END, questions[0])

                    optionButton1.config(text= first_option[0])
                    optionButton2.config(text= second_option[0])
                    optionButton3.config(text= third_option[0])
                    optionButton4.config(text= fourth_option[0])

                root1 = Toplevel()
                root1.overrideredirect(True)
                root1.config(bg="black")
                root1.geometry('500x400+140+30')
                root1.title('Result')
                root1Label =Label(root1, image= centerimage, bd ='0')
                root1Label.pack(pady =5)

                winLabel= Label(root1, text = 'You WON', font = ('arial',40, 'bold'), bg= 'black',fg='white')
                winLabel.pack()

                playagainButton = Button(root1, text = "Play again", 
                    font = ('arial',20, 'bold'), bg= 'black',fg='white', command= playagain)
                playagainButton.pack()

                closeButton = Button(root1,text = "Close", 
                    font = ('arial',20,'bold'), bg = 'black', fg = 'white',
                    activebackground= 'black', activeforeground= 'white', 
                    bd= 0, cursor = 'hand2', command= close)
                closeButton.pack()
            
                root1.mainloop()
                break

            question_area.delete(1.0,END)
            question_area.insert(END, questions[i+1])

            optionButton1.config(text = first_option[i+1])        
            optionButton2.config(text = second_option[i+1])
            optionButton3.config(text = third_option[i+1])
            optionButton4.config(text = fourth_option[i+1])

        if value not in correct_answers:  #wrong answer
            def close():
                root.destroy()
                window.destroy()

            def tryagain():
                root.destroy()
                question_area.delete(1.0,END )
                question_area.insert(END, questions[0])

                optionButton1.config(text= first_option[0])
                optionButton2.config(text= second_option[0])
                optionButton3.config(text= third_option[0])
                optionButton4.config(text= fourth_option[0])

            root = Toplevel()
            root.overrideredirect(True)
            root.config(bg="black")
            root.geometry('500x400+140+30')
            root.title('Result')
            rootLabel =Label(root, image= centerimage, bd ='0')
            rootLabel.pack(pady =5)

            loseLabel= Label(root, text = 'You lose', font = ('arial',40, 'bold'), bg= 'black',fg='white')
            loseLabel.pack()

            tryagainButton = Button(root, text = "Try again", 
                font = ('arial',20, 'bold'), bg= 'black',fg='white', command= tryagain)
            tryagainButton.pack()

            closeButton = Button(root,text = "Close", 
                font = ('arial',20,'bold'), bg = 'black', fg = 'white',
                activebackground= 'black', activeforeground= 'white', 
                bd= 0, cursor = 'hand2', command= close)
            closeButton.pack()
        
            root.mainloop()
            break
        
        


#data -------------------------
#questions 
myfile = open("question.txt", 'r',encoding="utf-8")
data = myfile.read() 
questions = data.split("\n")
myfile.close()

#correct answer
myfile = open("correct_answer.txt", 'r',encoding="utf-8")
data = myfile.read() 
correct_answers = data.split("\n")
myfile.close()

#first option
myfile = open("first_option.txt", 'r',encoding="utf-8")
data = myfile.read() 
first_option = data.split("\n")
myfile.close()

#second option
myfile = open("second_option.txt", 'r',encoding="utf-8")
data = myfile.read() 
second_option = data.split("\n")
myfile.close()

#third option
myfile = open("third_option.txt", 'r',encoding="utf-8")
data = myfile.read() 
third_option = data.split("\n")
myfile.close()

#fourth option
myfile = open("fourth_option.txt", 'r',encoding="utf-8")
data = myfile.read() 
fourth_option = data.split("\n")
myfile.close()

#frame-----------------------------------

leftframe =Frame(window)
leftframe.grid(row=0,column=0)

topframe = Frame(leftframe)
topframe.grid()

centerframe = Frame(leftframe)
centerframe.grid(row=1, column=0)

bottomframe = Frame(leftframe)
bottomframe.grid(row=2, column=0)

rightframe = Frame(window)
rightframe.grid(row=0, column=1)

phoneimage = ImageTk.PhotoImage(Image.open("phone.jpg")) 

phonelayoutlabel = Label(topframe, image = phoneimage)
phonelayoutlabel.grid(row=0,column=0)

phoneimage1 = ImageTk.PhotoImage(Image.open("phone.jpg")) 

phonelayoutlabel1 = Label(topframe, image = phoneimage1)
phonelayoutlabel1.grid(row=0,column=1)

phoneimage2 = ImageTk.PhotoImage(Image.open("phone.jpg")) 

phonelayoutlabel2 = Label(topframe, image = phoneimage2)
phonelayoutlabel2.grid(row=0,column=2)

centerimage = ImageTk.PhotoImage(Image.open("phone.jpg")) 


layerimage = ImageTk.PhotoImage(Image.open("lay.png")) 

layerlabel = Label(bottomframe, image = layerimage, bg='black')
layerlabel.grid(row=0,column=0)

rightimage = PhotoImage(file="picture0.png") 

rightilabel = Label(rightframe, image = rightimage)
rightilabel.grid(row=0,column=0)

question_area = Text(bottomframe,bg='black',fg='orange', width =34, height =2, wrap = 'word',bd=0 )
question_area.place(x=70, y =10)
question_area.insert(END, questions[0])

labelA=Label(bottomframe, text ='A', bg='black', fg='white')
labelA.place(x=60,y=110)

optionButton1 =Button(bottomframe,text = first_option[0],bg='black', fg='white', bd= '0', 
                      activebackground= 'black', activeforeground='orange', cursor='hand2')
optionButton1.place(x=100, y=100)

labelB =Label(bottomframe, text ='B', bg='black', fg='white')
labelB.place(x=330,y=110)

optionButton2 =Button(bottomframe,text = second_option[0],bg='black', fg='white', bd= '0', 
                      activebackground= 'black', activeforeground='orange', cursor='hand2')
optionButton2.place(x=370, y=100)

labelC =Label(bottomframe, text ='C', bg='black', fg='white')
labelC.place(x=60,y=190)

optionButton3 =Button(bottomframe,text = third_option[0],bg='black', fg='white', bd= '0', 
                      activebackground= 'black', activeforeground='orange', cursor='hand2')
optionButton3.place(x=100, y=180)

labelD =Label(bottomframe, text ='D', bg='black', fg='white')
labelD.place(x=330,y=190)

optionButton4 =Button(bottomframe,text = fourth_option[0],bg='black', fg='white', bd= '0', 
                      activebackground= 'black', activeforeground='orange', cursor='hand2')
optionButton4.place(x=370, y=180)


optionButton1.bind('<Button-1>',select )
optionButton2.bind('<Button-1>',select )
optionButton3.bind('<Button-1>',select )
optionButton4.bind('<Button-1>',select )

window.mainloop()