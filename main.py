import turtle
import random
import time
from english_words import english_words_alpha_set as words

yellow = "#cfbc57"
gray = "#525454"
green = "#5a855a"

screen = turtle.Screen()
screen.setup(516, 660)
screen.addshape("Wordle.gif")
screen.bgpic("Wordle.gif")
screen.title("Wordle")

class letter_box:
    def __init__ (self, letter, hint, x, y):
        self.letter = letter.upper()
        self.hint = hint
        self.x = x
        self.y = y
    def generate_square(self):
        self.letter1 = turtle.Turtle()
        self.letter1.shape("square")
        if self.hint<0:
            self.letter1.color(gray)
        elif self.hint<1:
            self.letter1.color(yellow)
        else:
            self.letter1.color(green)
        self.letter1.shapesize(stretch_wid=4.5, stretch_len=4.5)
        self.letter1.penup()
        self.letter1.hideturtle()
        self.letter1.goto(self.x, self.y)
        self.letter1.showturtle()
        screen.update()
    def make_letter(self):
        self.letter2 = turtle.Turtle()
        self.letter2.hideturtle()
        self.letter2.penup()
        self.letter2.goto(self.x, self.y-22)
        self.letter2.color("white")
        self.letter2.write(self.letter, font= ("Helvetica Neue",30,"bold"), align="center")
        screen.update()

def letters_animation(lives, hints, guessword):
    letter_list = []
    y=260+lives*103
    for i in range(5):
        letter1 = letter_box(guessword[i], hints[i], -207+i*103, y)
        letter1.generate_square()
        letter1.make_letter()

file = open("wordList.txt","r")
wordList = file.readlines()
word = wordList[random.randint(0, len(wordList)-1)]

def algorithm():
    screen.update()
    numberlives = 6
    guess = [""] * 5
    hints = [-1, -1, -1, -1, -1]
    print(word)
    while numberlives > 0 and guess != word:
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
        numberlives-=1
        letters_animation(numberlives, hints, guess)
        if sum(hints) == 5:
            print("You won!")
            break
        time.sleep(0.01)
screen.update()
algorithm()
#turtle.mainloop()
