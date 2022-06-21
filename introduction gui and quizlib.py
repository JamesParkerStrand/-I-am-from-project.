import tkinter as tk
from tkinter import ttk

def anscheck(ans, inp):
    correct = False
    inp = inp.lower()
    for i in ans:
        c = inp.find(i)
        if c != -1:
            correct = True
            break
        else:
            correct = False
    return correct

def quizlib():
    print("This is a mad-libs/quiz styled challenge (make sure you add periods to your inputs or it might look off)")
    correct = 0
    ans1c = ["united states", "us", "u.s"]
    ans1c2 = ["american indian"]
    ans2c = ["non religious", "non-religious", "not religious", "not-religious", "atheist", "atheism"]
    ans3c = ["genz", "gen z", "gen zer", "gen z'er", "gen-zer","gen-z","gen-z'er"]
    ans4c = ["he", "him", "his", "man", "boy", "manly", "masculine"]
    ans5c = ["tacoma washington", "tacoma wa", "tacoma, wa", "tacoma, washington"]
    ans5c2 = ["kent, wa", "kent wa", "kent, washington", "kent washington"]
    ans7c = ["drawing", "doodling", "doodled", "doodle", "draw", "drawn","drew","illustrating", "illustrated","illustrate","sketch", "sketching", "sketched", "sketcher"]
    ans7c2 = ["computer games","pc games", "pc game", "computer game", "games","gaming","gamed","gamer", "video games", "video game", "game"]
    ans7c3 = ["programming", "programmer", "program","programmed", "programs", "code", "coder", "coding", "coded","codes", "script", "scripting", "scripted", "scripts", "scripter", "develop", "developed", "developing", "developer"]
    ans7c4 = ["puzzle game", "puzzle gaming", "puzzle games", "puzzling", "puzzle", "puzzled"]


    ans1 = input("What is my nationality and ethnic background? (answers are spelling sensitive!): ")

    check = anscheck(ans=ans1c, inp=ans1)
    check2 = anscheck(ans=ans1c2, inp=ans1)
    if check and check2:
        print("that is correct! 1 point!")
        correct += 1
    else:
        print("incorrect! no point!")

    ans2 = input("What is my religion?: ")

    check = anscheck(ans2c, ans2)
    if check:
        print("that is correct! 1 point!")
        correct += 1
    else:
        print("incorrect! no point!")

    ans3 = input("What is my age generation? what is my age? (input a number for age!): ")


    match = ans3.find("19")
    check = anscheck(ans3c, ans3)
    if check and match != -1:
        print("that is correct! 1 point!")
        correct += 1
    else:
        print("incorrect! no point!")

    ans4 = input("what is my gender?: ")
    check = anscheck(ans4c, ans4)
    if check:
        print("that is correct! 1 point!")
        correct += 1
    else:
        print("incorrect! no point!")

    ans5 = input("Where Do I Currently live in? Where was I born and raised?: ")

    check = anscheck(ans5c, ans5)
    check2 = anscheck(ans5c2, ans5)
    if check and check2:
        print("that is correct! 1 point!")
        correct += 1
    else:
        print("incorrect! no point!")

    ans6 = input("What is one game I play with friends and family?: ")

    check = anscheck(["minecraft"], ans6)
    if check:
        print("that is correct! 1 point!")
        correct += 1
    else:
        print("incorrect! no point!")

    ans7 = input("what were my 4 hobbies listed?: ")


    check1 = anscheck(ans7c, ans7)
    check2 = anscheck(ans7c2, ans7)
    check3 = anscheck(ans7c3, ans7)
    check4 = anscheck(ans7c4, ans7)

    if check1 and check2 and check3 and check4:
        print("that is correct! 1 point!")
        correct += 1
    else:
        print("incorrect! no point!")
    print(f"You got {correct} / 7! here's the following mad-libs, you can post what you got.")
    print(ans1, ans2, ans3, ans4, ans5, ans6, "lastly, " + ans7)

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Introduce yourself project By James Parker Strand")
        self.geometry("450x590")

        self.label = ttk.Label(self,text="Choose any of the buttons below!",font=25)
        self.label.pack(pady=5)

        self.Nationalitybutton = ttk.Button(self,text="Your nationality and ethnic background", command=self.nationality)
        self.Nationalitybutton.pack(pady=15)

        self.relbutton = ttk.Button(self, text="Your religion", command=self.religion)
        self.relbutton.pack(pady=15)

        self.socialbutton = ttk.Button(self, text="social class", command=self.social)
        self.socialbutton.pack(pady=15)

        self.agebutton = ttk.Button(self, text="age generation", command=self.age)
        self.agebutton.pack(pady=15)

        self.gendbutton = ttk.Button(self, text="gender", command=self.gender)
        self.gendbutton.pack(pady=15)

        self.areabutton = ttk.Button(self, text="Area you lived/in now", command=self.area)
        self.areabutton.pack(pady=15)

        self.groupbutton = ttk.Button(self, text="What groups your part of", command=self.group)
        self.groupbutton.pack(pady=15)

        self.hobbiesbutton = ttk.Button(self, text="Hobbies", command=self.hobbies)
        self.hobbiesbutton.pack(pady=15)

        self.quizbutton = ttk.Button(self, text="Take the mad-libs/quiz!", command=self.quiz)
        self.quizbutton.pack(pady=15)

        self.answer = ttk.Label(self, text="", font=25)
        self.answer.pack()
        self.mainloop()

    def nationality(self):
        self.answer.config(text="* Born in the United States. \n* For my ethnicity I am a American Indian.")
    def religion(self):
        self.answer.config(text="* Non-religious.")
    def social(self):
        self.answer.config(text="* I would say I am getting by in life just fine.")
    def age(self):
        self.answer.config(text="* Age 19 (about to be 20 in june).\n* I am part of gen z.")
    def gender(self):
        self.answer.config(text="* He/Him.")
    def area(self):
        self.answer.config(text="* I was raised in Kent Wa. \n* I now currently live in Tacoma.")
    def group(self):
        self.geometry("520x600")
        self.answer.config(text="* As far as groups go,\n I play on a minecraft server with some friends and family.")
    def hobbies(self):
        self.answer.config(text="* Drawing, pc games, programming\n (obvious one), puzzle games")
    def quiz(self):
        self.destroy()
        quizlib()

if __name__ == "__main__":
    App = app()
