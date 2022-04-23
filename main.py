import turtle
import random
import time
import tkinter as tk
import nltk
from nltk.stem.snowball import SnowballStemmer

nltk.download("words")
snow_stemmer = SnowballStemmer(language="english")
eng_words = set(nltk.corpus.words.words())
wordle_words_set = set(line.strip() for line in open('wordList.txt'))

yellow = "#b69f42"
gray = "#525454"
green = "#5a855a"
black = "#121213"
grey = "#3c3c3c"

screen = turtle.Screen()
screen.setup(516, 660)
screen.addshape("Wordle.gif")
screen.bgpic("Wordle.gif")
screen.title("Wordle")

root = tk.Tk()
root.title("Wordle")

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
entry1.config(bg=grey, fg="white", font=("Helvetica Neue", 12, "bold"))
canvas1.create_window(200, 140, window=entry1)
canvas1.config(bg=grey)

label1 = None
topLabel = tk.Label(root, text="ENTER YOUR TEXT:", fg="white", bg=grey)
topLabel.config(font=("Helvetica Neue", 15, "bold"))
canvas1.create_window(200, 70, window=topLabel)

def getWord():
    global label1
    if label1 != None:
        label1.destroy()
    x = entry1.get()
    msg = newAlg(x)
    if msg != None:
        label1 = tk.Label(root, text=msg, fg="white", bg=grey, font=("Helvetica Neue", 10))
        canvas1.create_window(200, 240, window=label1)
        root.update()
        if msg == "You win!" or "lose" in msg:
            time.sleep(2)
            turtle.bye()
            root.destroy()
    else:
        label1 = tk.Label(root, text="",  fg="white", bg=grey, font=("Helvetica Neue", 10))
        canvas1.create_window(200, 240, window=label1)

button1 = tk.Button(root, text="ENTER", command=getWord, font=("Helvetica Neue", 10, "bold"), bg="white")
canvas1.create_window(200, 190, window=button1)

class letter_box:
    def __init__ (self, letter, hint, x, y):
        self.letter = letter.upper()
        self.hint = hint
        self.x = x
        self.y = y
    def generate_square(self):
        self.letter1 = turtle.Turtle()
        self.letter1.hideturtle()
        self.letter1.penup()
        self.letter1.goto(self.x, self.y)
        self.letter1.shape("square")
        if self.hint<0:
            self.letter1.color(gray)
        elif self.hint<1:
            self.letter1.color(yellow)
        else:
            self.letter1.color(green)
        self.letter1.shapesize(stretch_wid=4.5, stretch_len=4.5)
        self.letter1.showturtle()
        self.letter1.stamp()
        screen.update()
    def make_letter(self):
        self.letter1.hideturtle()
        self.letter1.goto(self.x, self.y-22)
        self.letter1.color("white")
        self.letter1.write(self.letter, font= ("Helvetica Neue",30,"bold"), align="center")
        screen.update()

def letters_animation(lives, hints, guessword):
    letter_list = []
    y=260-lives*103
    for i in range(5):
        letter1 = letter_box(guessword[i], hints[i], -207+i*103, y)
        letter1.generate_square()
        letter1.make_letter()

file = open("wordList.txt","r")
wordList = file.readlines()
word = wordList[random.randint(0, len(wordList)-1)]
numberlives = 0
hints = [-1, -1, -1, -1, -1]

def newAlg(guess):
    global numberlives
    global hints
    hints = [-1, -1, -1, -1, -1]
    if guess not in eng_words and guess not in wordle_words_set and snow_stemmer.stem(guess) not in eng_words:
        return "Not a word."
    if len(guess) > 5:
        return "Make sure you guess a five letter word."
    for index in range(5):
        if guess[index] in word:
            if guess[index] == word[index]:
                hints[index] = 1
            else:
                hints[index] = 0
    letters_animation(numberlives, hints, guess)
    numberlives += 1
    if sum(hints) == 5:
         return "You win!"
    if numberlives >= 6:
        return "You lose! \n The word was: "+word

def algorithm():
    screen.update()
    numberlives = 0
    guess = [""] * 5
    hints = [-1, -1, -1, -1, -1]
    print(word)
    while numberlives <= 6 and guess != word:
        screen.update()
        guess = list(input("Guess a five letter word."))
        while len(guess) != 5:
            guess = list(input("Make sure you guess a five letter word."))
        for index in range(5):
            if guess[index] in word:
                if guess[index] == word[index]:
                    hints[index] = 1
                else:
                    hints[index] = 0
        letters_animation(numberlives, hints, guess)
        numberlives += 1
        if sum(hints) == 5:
            print("You won!")
            break
        time.sleep(0.01)
screen.update()
root.mainloop()
turtle.mainloop()