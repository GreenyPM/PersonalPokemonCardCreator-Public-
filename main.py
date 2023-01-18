import camera
import cardAssembly
import tkinter as tk
from tkinter import *
from tkinter import ttk


def questionBase(question, ans1, ans2, ans3, ans4,):
    global points
    localPoints = -1
    print(question,"\n 1)",ans1, "\n 2)", ans2, "\n 3)", ans3, "\n 4)", ans4)
    while localPoints == -1:
        try:
            ans = int(input())
            if (1 is ans):
                localPoints = 1
            if (2 is ans):
                localPoints = 2
            if (3 is ans):
                localPoints = 5
            if (4 is ans):
                localPoints = 0
        except ValueError:
            print("Invalid Entry: Pleas enter a Number ex.(1, 2, 3, or, 4)")
    points += localPoints

def questionGUIBase1(question, ans1, ans2, ans3, ans4):
    global questionCounter
    question1 = Label(root, text=question, font=('Helvetica', 35), bg = 'blue')
    question1.place(x= 60, y=50)
    ans1 = Button(root, text=ans1, font=('Helvetica', 20), height=2, width=60, bg ='light blue',command=lambda: choice11())
    ans1.place(x=0, y=170)
    ans2 = Button(root, text=ans2, font=('Helvetica', 20), height=2, width=60, bg ='light blue', command=lambda: choice12())
    ans2.place(x=0, y=270)
    ans3 = Button(root, text=ans3, font=('Helvetica', 20), height=2, width=60, bg ='light blue',command=lambda: choice13())
    ans3.place(x=0, y=370)
    ans4 = Button(root, text=ans4, font=('Helvetica', 20), height=2, width=60, bg ='light blue', command=lambda: choice14())
    ans4.place(x=0, y=470)
    def choice11():
        global points
        localPoints = 1
        points += localPoints
        questionGUIBase2("There is a person you like, you wanna get their attention.\nWhat do you do?",
                         "Bravely Declare my love.", "Might say hello...", "Pull a prank to get attention.",
                         "Look from afar.")
        question1.destroy()
        ans1.destroy()
        ans2.destroy()
        ans3.destroy()
        ans4.destroy()

    def choice12():
        global points
        localPoints = 2
        points += localPoints
        questionGUIBase2("There is a person you like, you wanna get their attention.\nWhat do you do?",
                         "Bravely Declare my love.", "Might say hello...", "Pull a prank to get attention.",
                         "Look from afar.")
        question1.destroy()
        ans1.destroy()
        ans2.destroy()
        ans3.destroy()
        ans4.destroy()

    def choice13():
        global points
        localPoints = 5
        points += localPoints
        questionGUIBase2("There is a person you like, you wanna get their attention.\nWhat do you do?",
                         "Bravely Declare my love.", "Might say hello...", "Pull a prank to get attention.",
                         "Look from afar.")
        question1.destroy()
        ans1.destroy()
        ans2.destroy()
        ans3.destroy()
        ans4.destroy()

    def choice14():
        global points
        localPoints = 0
        points += localPoints
        questionGUIBase2("There is a person you like, you wanna get their attention.\nWhat do you do?",
                         "Bravely Declare my love.", "Might say hello...", "Pull a prank to get attention.",
                         "Look from afar.")
        question1.destroy()
        ans1.destroy()
        ans2.destroy()
        ans3.destroy()
        ans4.destroy()

def questionGUIBase2(question, ans1, ans2, ans3, ans4):
    question2 = Label(root, text=question, font=('Helvetica', 30), bg = 'blue')
    question2.place(x=0, y=50)
    ans21 = Button(root, text=ans1, font=('Helvetica', 20), height=2, width=60, command=lambda: choice21(), bg = 'light blue')
    ans21.place(x=0, y=170)
    ans22 = Button(root, text=ans2, font=('Helvetica', 20), height=2, width=60, command=lambda: choice22(),bg = 'light blue')
    ans22.place(x=0, y=270)
    ans23 = Button(root, text=ans3, font=('Helvetica', 20), height=2, width=60, command=lambda: choice23(), bg= 'light blue')
    ans23.place(x=0, y=370)
    ans24 = Button(root, text=ans4, font=('Helvetica', 20), height=2, width=60, command=lambda: choice24(), bg = 'light blue')
    ans24.place(x=0, y=470)

    def choice21():
        global points
        localPoints = 1
        points += localPoints
        questionGUIBase3("How quickly do you respond to a text?", "Reply right away.", "May reply, may not.", "Too much trouble.", "I don't.")
        question2.destroy()
        ans21.destroy()
        ans22.destroy()
        ans23.destroy()
        ans24.destroy()

    def choice22():
        global points
        localPoints = 2
        points += localPoints
        questionGUIBase3("How quickly do you respond to a text?", "Reply right away.", "May reply, may not.",
                         "Too much trouble.", "I don't.")
        question2.destroy()
        ans21.destroy()
        ans22.destroy()
        ans23.destroy()
        ans24.destroy()

    def choice23():
        global points
        localPoints = 5
        points += localPoints
        questionGUIBase3("How quickly do you respond to a text?", "Reply right away.", "May reply, may not.",
                         "Too much trouble.", "I don't.")
        question2.destroy()
        ans21.destroy()
        ans22.destroy()
        ans23.destroy()
        ans24.destroy()

    def choice24():
        global points
        localPoints = 0
        points += localPoints
        questionGUIBase3("How quickly do you respond to a text?", "Reply right away.", "May reply, may not.",
                         "Too much trouble.", "I don't.")
        question2.destroy()
        ans21.destroy()
        ans22.destroy()
        ans23.destroy()
        ans24.destroy()

def questionGUIBase3(question, ans1, ans2, ans3, ans4):
    question3 = Label(root, text=question, font=('Helvetica', 30), bg= 'blue')
    question3.place(x=160, y=40)
    ans31 = Button(root, text=ans1, font=('Helvetica', 20), height=2, width=60, command=lambda: choice31(), bg = 'light blue')
    ans31.place(x=0, y=130)
    ans32 = Button(root, text=ans2, font=('Helvetica', 20), height=2, width=60, command=lambda: choice32(), bg = 'light blue')
    ans32.place(x=0, y=230)
    ans33 = Button(root, text=ans3, font=('Helvetica', 20), height=2, width=60, command=lambda: choice33(), bg = 'light blue')
    ans33.place(x=0, y=330)
    ans34 = Button(root, text=ans4, font=('Helvetica', 20), height=2, width=60, command=lambda: choice34(), bg = 'light blue')
    ans34.place(x=0, y=430)

    def choice31():
        global points
        localPoints = 1
        points += localPoints
        questionGUIBase4("A human hand extends out of a toilet!\nWhat do you do?", "Scream and run.", "Close the Lid without a word.", "Shake Hands with it.", "Praise it like a god.")
        question3.destroy()
        ans31.destroy()
        ans32.destroy()
        ans33.destroy()
        ans34.destroy()

    def choice32():
        global points
        localPoints = 2
        points += localPoints
        questionGUIBase4("A human hand extends out of a toilet!\nWhat do you do?", "Scream and run.", "Close the Lid without a word.", "Shake Hands with it.", "Praise it like a god.")
        question3.destroy()
        ans31.destroy()
        ans32.destroy()
        ans33.destroy()
        ans34.destroy()

    def choice33():
        global points
        localPoints = 5
        points += localPoints
        questionGUIBase4("A human hand extends out of a toilet!\nWhat do you do?", "Scream and run.",
                         "Close the Lid without a word.", "Shake Hands with it.", "Praise it like a god.")
        question3.destroy()
        ans31.destroy()
        ans32.destroy()
        ans33.destroy()
        ans34.destroy()

    def choice34():
        global points
        localPoints = 0
        points += localPoints
        questionGUIBase4("A human hand extends out of a toilet!\nWhat do you do?", "Scream and run.",
                         "Close the Lid without a word.", "Shake Hands with it.", "Praise it like a god.")
        question3.destroy()
        ans31.destroy()
        ans32.destroy()
        ans33.destroy()
        ans34.destroy()

def questionGUIBase4(question, ans1, ans2, ans3, ans4):
    question4 = Label(root, text=question, font=('Helvetica', 30), bg='blue')
    question4.place(x=160, y=20)
    ans41 = Button(root, text=ans1, font=('Helvetica', 20), height=2, width=60, command=lambda: choice41(), bg = 'light blue')
    ans41.place(x=0, y=130)
    ans42 = Button(root, text=ans2, font=('Helvetica', 20), height=2, width=60, command=lambda: choice42(), bg = 'light blue')
    ans42.place(x=0, y=230)
    ans43 = Button(root, text=ans3, font=('Helvetica', 20), height=2, width=60, command=lambda: choice43(), bg = 'light blue')
    ans43.place(x=0, y=330)
    ans44 = Button(root, text=ans4, font=('Helvetica', 20), height=2, width=60, command=lambda: choice44(), bg = 'light blue')
    ans44.place(x=0, y=430)

    def choice41():
        global points
        localPoints = 1
        points += localPoints
        questionGUIBase5("There is an Alien Invasion!\nWhat will you do?", "Fight.", "Run.", "Ignore It.", "Make Peace.")
        question4.destroy()
        ans41.destroy()
        ans42.destroy()
        ans43.destroy()
        ans44.destroy()

    def choice42():
        global points
        localPoints = 2
        points += localPoints
        questionGUIBase5("There is an Alien Invasion!\nWhat will you do?", "Fight.", "Run.", "Ignore It.", "Make Peace.")
        question4.destroy()
        ans41.destroy()
        ans42.destroy()
        ans43.destroy()
        ans44.destroy()

    def choice43():
        global points
        localPoints = 5
        points += localPoints
        questionGUIBase5("There is an Alien Invasion!\nWhat will you do?", "Fight.", "Run.", "Ignore It.", "Make Peace.")
        question4.destroy()
        ans41.destroy()
        ans42.destroy()
        ans43.destroy()
        ans44.destroy()

    def choice44():
        global points
        localPoints = 0
        points += localPoints
        questionGUIBase5("There is an Alien Invasion!\nWhat will you do?", "Fight.", "Run.", "Ignore It.", "Make Peace.")
        question4.destroy()
        ans41.destroy()
        ans42.destroy()
        ans43.destroy()
        ans44.destroy()

def questionGUIBase5(question, ans1, ans2, ans3, ans4):
    question5 = Label(root, text=question, font=('Helvetica', 30), bg='blue')
    question5.place(x=270, y=50)
    ans51 = Button(root, text=ans1, font=('Helvetica', 20), height=2, width=60, command=lambda: choice51(), bg = 'light blue')
    ans51.place(x=0, y=170)
    ans52 = Button(root, text=ans2, font=('Helvetica', 20), height=2, width=60, command=lambda: choice52(), bg = 'light blue')
    ans52.place(x=0, y=270)
    ans53 = Button(root, text=ans3, font=('Helvetica', 20), height=2, width=60, command=lambda: choice53(), bg = 'light blue')
    ans53.place(x=0, y=370)
    ans54 = Button(root, text=ans4, font=('Helvetica', 20), height=2, width=60, command=lambda: choice54(), bg = 'light blue')
    ans54.place(x=0, y=470)

    def choice51():
        global points
        localPoints = 1
        points += localPoints
        questionGUIBase6("It's Summer Vacation!\nWhere do you go?", "The Beach.", "The Spa.", "The Mall.", "The Mountains")
        question5.destroy()
        ans51.destroy()
        ans52.destroy()
        ans53.destroy()
        ans54.destroy()

    def choice52():
        global points
        localPoints = 2
        points += localPoints
        questionGUIBase6("It's Summer Vacation!\nWhere do you go?", "The Beach.", "The Spa.", "The Mall.", "The Mountains")
        question5.destroy()
        ans51.destroy()
        ans52.destroy()
        ans53.destroy()
        ans54.destroy()

    def choice53():
        global points
        localPoints = 5
        points += localPoints
        questionGUIBase6("It's Summer Vacation!\nWhere do you go?", "The Beach.", "The Spa.", "The Mall.", "The Mountains")
        question5.destroy()
        ans51.destroy()
        ans52.destroy()
        ans53.destroy()
        ans54.destroy()

    def choice54():
        global points
        localPoints = 0
        points += localPoints
        questionGUIBase6("It's Summer Vacation!\nWhere do you go?", "The Beach.", "The Spa.", "The Mall.", "The Mountains")
        question5.destroy()
        ans51.destroy()
        ans52.destroy()
        ans53.destroy()
        ans54.destroy()


def questionGUIBase6(question, ans1, ans2, ans3, ans4):
    question6 = Label(root, text=question, font=('Helvetica', 30), bg='blue')
    question6.place(x=290, y=50)
    ans61 = Button(root, text=ans1, font=('Helvetica', 20), height=2, width=60, command=lambda: choice61(), bg = 'light blue')
    ans61.place(x=0, y=170)
    ans62 = Button(root, text=ans2, font=('Helvetica', 20), height=2, width=60, command=lambda: choice62(), bg = 'light blue')
    ans62.place(x=0, y=270)
    ans63 = Button(root, text=ans3, font=('Helvetica', 20), height=2, width=60, command=lambda: choice63(), bg = 'light blue')
    ans63.place(x=0, y=370)
    ans64 = Button(root, text=ans4, font=('Helvetica', 20), height=2, width=60, command=lambda: choice64(), bg = 'light blue')
    ans64.place(x=0, y=470)

    def choice61():
        global points
        localPoints = 1
        points += localPoints
        typeResult()
        question6.destroy()
        ans61.destroy()
        ans62.destroy()
        ans63.destroy()
        ans64.destroy()

    def choice62():
        global points
        localPoints = 2
        points += localPoints
        typeResult()
        question6.destroy()
        ans61.destroy()
        ans62.destroy()
        ans63.destroy()
        ans64.destroy()

    def choice63():
        global points
        localPoints = 5
        points += localPoints
        typeResult()
        question6.destroy()
        ans61.destroy()
        ans62.destroy()
        ans63.destroy()
        ans64.destroy()

    def choice64():
        global points
        localPoints = 0
        points += localPoints
        typeResult()
        question6.destroy()
        ans61.destroy()
        ans62.destroy()
        ans63.destroy()
        ans64.destroy()

def typeResult():
    global type
    typColor = 'white'
    if points in range(0, 4):
        type = "Normal"
        print(type)
        # print("Normal")
    elif points in range(4, 7):
        type = "Fire"
        typColor = 'red'
        print(type)
    elif points in range(7, 11):
        type = "Water"
        typColor = 'light blue'
        print(type)
    elif points in range(11, 14):
        type = "Grass"
        typColor = 'green'
        print(type)
    elif points in range(14, 17):
        type = "Fighting"
        typColor = 'orange'
        print(type)
    elif points in range(17, 20):
        type = "Psychic"
        typColor = 'purple'
        print(type)
    elif points in range(20, 23):
        type = "Steel"
        typColor = 'grey'
        print(type)
    elif points in range(23, 26):
        type = "Electric"
        typColor = 'yellow'
        print(type)
    elif points in range(26, 29):
        type = "Fairy"
        typColor = 'pink'
        print(type)
    elif points == 29:
        type = "Dark"
        print(type)
    elif points == 30:
        type = "Dragon"
        typColor = 'brown'
        print(type)
    congrat = Label(root, text="Congratulations Your Type is:", font='Helvetica 40 underline', bg= 'blue')
    congrat.place(x=140, y=0)
    typeResult = Label(root, text=type, font=('Helvetica', 150), bg = typColor)
    typeResult.place(x=200, y=100)
    make = Button(root, text="Press Here to make Your Own Card!", font=('Helvetica', 15), height=5, width=60, command=lambda: takePic())
    make.place(x=150, y=400)
    def takePic():
        camera.takePicture()
        cardAssembly.cardCreator(type, playerName)
        result()
    def result():
        congrat.destroy()
        typeResult.destroy()
        make.destroy()
        cardInfo = Label(root,text="Here's your very own Card!", font= ('Helvetica', 60))
        cardInfo.place(x =15, y= 250)
        restartButt= Button(root, text = "Press Here to Restart", font = ('Helvetica', 25), height = 2, width = 30, command=lambda: resetToOriginal())
        restartButt.place(x=200, y=500)

        def resetToOriginal():
            cardInfo.destroy()
            restartButt.destroy()
            # header=Label(root, text = "PPCM", font = ('Helvetica', 90), bg = 'yellow')
            header = Label(root, image=titleimg, bg='blue')
            header.place(x=170, y=0)
            # subtitle= Label(root, text = "The Personal Pokemon Card Machine", font = ('Helvetica', 20), bg = 'blue')
            subtitle = Label(root, image=subtitleimg, bg='blue')
            subtitle.place(x=230, y=330)
            instruction = Label(root, text="Type in your Name to Begin:", font=('Helvetica', 20), bg='blue')
            instruction.place(x=320, y=420)
            nameEntry = Entry(root, font=('Arial', 30))
            nameEntry.place(x=280, y=460)
            startButton = Button(root, text="Press Here to Start!", font=('Helvetica', 15), height=2, width=30, command=lambda: restartDissapear())
            startButton.place(x=330, y=525)

            def restartDissapear():
                global points
                global playerName
                playerName = nameEntry.get()
                header.destroy()
                subtitle.destroy()
                instruction.destroy()
                nameEntry.destroy()
                startButton.destroy()
                questionGUIBase1("What is your Favorite Color out of these?", "Blue", "Green", "Red", "Yellow")
                points -= points


points = 0
type = 'Normal'
playerName = ''

root = Tk()
root.title("Personal Pokemon Card Machine")
root.geometry("1000x720")
root.config(background = 'blue')
root.resizable(False,False)
titleimg = PhotoImage(file= 'C:/Users/AlienUser/Documents/Python/PokemonTypeTest/Card Bases/PPCMTitle.png')
subtitleimg = PhotoImage(file= 'C:/Users/AlienUser/Documents/Python/PokemonTypeTest/Card Bases/subTitle.png')
copywriteMrk= Label(root, text= 'Patrick Madonna 2023', font=('Helvetica', 20), bg = 'yellow')
copywriteMrk.place(x=360, y=685)

#header=Label(root, text = "PPCM", font = ('Helvetica', 90), bg = 'yellow')
header=Label(root, image=titleimg, bg = 'blue')
header.place(x=170, y=0)
#subtitle= Label(root, text = "The Personal Pokemon Card Machine", font = ('Helvetica', 20), bg = 'blue')
subtitle= Label(root, image=subtitleimg, bg = 'blue' )
subtitle.place(x=230, y=330)
instruction = Label(root, text = "Type in your Name to Begin:", font = ('Helvetica', 20), bg = 'blue')
instruction.place(x=320, y=420)
nameEntry = Entry(root, font=('Arial', 30))
nameEntry.place(x=280, y= 460)

def startDissapear():
    global playerName
    playerName = nameEntry.get()
    header.destroy()
    subtitle.destroy()
    instruction.destroy()
    nameEntry.destroy()
    startButton.destroy()
    questionGUIBase1("What is your Favorite Color out of these?","Blue", "Green", "Red", "Yellow")

startButton = Button(root, text = "Press Here to Start!", font = ('Helvetica', 15), height = 2, width = 30, command=lambda: startDissapear())
startButton.place(x=330, y=525)

mainloop()






#Tkinter Ends

#Hard Code Below


#print("Pokemon Card Test: What Type are you?")
#playerName = input("But First What Is your name?:")
#questionBase("What is your Favorite Color out of these?", "Blue", "Green", "Red", "Yellow")
#questionBase("There is a person you like, but there's no opportunity to get close. What do you do?", "Bravely Declare my love.", "Might say hello...", "Pull a prank to get attention.", "Look from afar.")
#questionBase("How quickly do you respond to a text?", "Reply right away.", "May reply, may not.", "Too much trouble.", "I don't.")
#questionBase("A human hand extends out of a toilet! what do you do?", "Scream and run.", "Close the Lid without a word.", "Shake Hands with it.", "Praise it like a god.")
#questionBase("There is an Alien Invasion! What will you do?", "Fight.", "Run.", "Ignore It.", "Make Peace.")
#questionBase("It's Summer! Where do you go?", "The Beach.", "The Spa.", "The Mall.", "The Mountains")


#camera.takePicture()
#cardAssembly.cardCreator(type, playerName)
