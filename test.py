# get 10 right consencutive answers you win!!!!!!!
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.title('QUIZ GAME')
window.geometry('1600x900')
window.config(bg="black")
backgroundimage = ImageTk.PhotoImage(Image.open("layout.png")) 
windowLabel =Label(window, image= backgroundimage)
windowLabel.pack()

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
                root1.geometry('700x400+600+350')
                root1.title('Result')
                root1Label =Label(root1, image= winimage, bd ='0')
                root1Label.pack()

                playagainButton = Button(root1, text = "Play Again", 
                font = ('arial',20, 'bold'), bg= 'black',fg='white', bd =3, command= playagain)
                playagainButton.place(x= 270, y =240)

                closeButton = Button(root1,text = "Exit", 
                font = ('arial',10,'bold'), bg = 'blue', fg = 'white',
                activebackground= 'black', activeforeground= 'white',bd=5, cursor = 'hand2', command= close)
                closeButton.place(x= 330, y =310)
            
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
            root.geometry('700x400+600+350')
            root.title('Result')
            rootLabel =Label(root, image= loseimage, bd ='0')
            rootLabel.pack()

            tryagainButton = Button(root, text = "Try again", 
                font = ('arial',20, 'bold'), bg= 'black',fg='white', bd =3, command= tryagain)
            tryagainButton.place(x= 280, y =240)

            closeButton = Button(root,text = "Exit", 
                font = ('arial',10,'bold'), bg = 'cyan', fg = 'black',
                activebackground= 'black', activeforeground= 'white', width= 6, height= 1,
                bd=6, cursor = 'hand2', command= close)
            closeButton.place(x= 320, y = 340)
            
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

#layout, button, image-----------------------------------


loseimage = ImageTk.PhotoImage(Image.open("lose.png")) 
winimage = ImageTk.PhotoImage(Image.open("win.png")) 


question_area = Text(window,font = ('Monoton', 35 , 'bold'),bg = "#120544", fg ="white", width =25, height =2, wrap = 'word',bd=0 )
question_area.place(x=470, y =400)
question_area.insert(END, questions[0])

labelA =Label(window, text ='A', font = ('Monoton',30, 'bold'), bg='#163A6C', fg='white')
labelA.place(x=240,y=615)
labelB =Label(window, text ='B', font = ('Monoton',30, 'bold'),bg='#163A6C', fg='white')
labelB.place(x=920,y=615)
labelC =Label(window, text ='C', font = ('Monoton',30, 'bold'), bg='#163A6C', fg='white')
labelC.place(x=240,y=735)
labelD =Label(window, text ='D', font = ('Monoton',30, 'bold'), bg='#163A6C', fg='white')
labelD.place(x=920,y=730)


optionButton1 =Button(window,text = first_option[0],font = ('Monoton',20, 'bold'),bg='#163A6C', fg='white', bd= '0', 
                      activebackground= '#163A6C', activeforeground='white', cursor='hand2')
optionButton1.place(x=280, y=615)


optionButton2 =Button(window,text = second_option[0],font = ('Monoton',20, 'bold'),bg='#163A6C', fg='white', bd= '0', 
                      activebackground= '#163A6C', activeforeground='white', cursor='hand2')
optionButton2.place(x=960, y=615)


optionButton3 =Button(window,text = third_option[0], font = ('Monoton',20, 'bold'),bg='#163A6C', fg='white', bd= '0', 
                      activebackground= 'black', activeforeground='white', cursor='hand2')
optionButton3.place(x=280, y=735)


optionButton4 =Button(window,text = fourth_option[0], font = ('Monoton',20, 'bold'),bg='#163A6C', fg='white', bd= '0', 
                      activebackground= '#163A6C', activeforeground='white', cursor='hand2')
optionButton4.place(x=960, y=730)


optionButton1.bind('<Button-1>',select )
optionButton2.bind('<Button-1>',select )
optionButton3.bind('<Button-1>',select )
optionButton4.bind('<Button-1>',select )

window.mainloop()