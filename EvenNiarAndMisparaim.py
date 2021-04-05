import turtle
from time import sleep
import random
import math
Rock = turtle.Turtle()
paper = turtle.Turtle()
Scissors = turtle.Turtle()
stutos = turtle.Turtle()
wn = turtle.Screen()

paper_image1 = "Paper clicked1.gif"
paper_image2 = "Paper Unclicked1.GIf"
Rock_image2 = "Rock clicked1.GIF"
Rock_image1 = "Rock Unclicked1.GIF"
Scissors_image2 = "Scissors clicked1.GIF"
Scissors_image1 = "Scissors Unclicked1.GIF"
Won_image = "Won.GIF"
Lost_image = "Lost.GIF"
none_image = "None.GIF"
tie_image = "Tie.GIF"
wn.addshape(paper_image1)
wn.addshape(Won_image)
wn.addshape(Lost_image)
wn.addshape(tie_image)
wn.addshape(none_image)
wn.addshape(paper_image2)
wn.addshape(Rock_image1)
wn.addshape(Rock_image2)
wn.addshape(Scissors_image1)
wn.addshape(Scissors_image2)
paper.shape(paper_image1)
Rock.shape(Rock_image1)
Scissors.shape(Scissors_image1)
stutos.shape(none_image)
paper.pu()
paper.setpos(100, 0)
Rock.pu()
Rock.setpos(0, 0)
Scissors.pu()
Scissors.setpos(-100, 0)
stutos.pu()
stutos.setpos(0, 300)
def PaperClicked(X, Y) :
    paper.shape(paper_image2)
    randomNum = math.floor(random.random() * 3)
    if (randomNum == 0):
        print("you won")
        stutos.shape(Won_image)
    elif (randomNum == 1):
        stutos.shape(tie_image)
        print("tie")
    else:
        print("you lost")
        stutos.shape(Lost_image)
    sleep(0.5)
    paper.shape(paper_image1)
def RockClicked(X, Y) :
    Rock.shape(Rock_image2)
    randomNum = math.floor(random.random() * 3)
    if (randomNum == 0):
        print("you won")
        stutos.shape(Won_image)
    elif (randomNum == 1):
        stutos.shape(tie_image)
        print("tie")
    else:
        print("you lost")
        stutos.shape(Lost_image)
    sleep(0.5)
    Rock.shape(Rock_image1)
def ScissorsClicked(X, Y) :
    Scissors.shape(Scissors_image2)
    randomNum = math.floor(random.random() * 3)
    if (randomNum == 0):
        print("you won")
        stutos.shape(Won_image)
    elif (randomNum == 1):
        stutos.shape(tie_image)
        print("tie")
    else:
        print("you lost")
        stutos.shape(Lost_image)
    sleep(0.5)
    Scissors.shape(Scissors_image1)


paper.onclick(PaperClicked)
Rock.onclick(RockClicked)
Scissors.onclick(ScissorsClicked)



turtle.mainloop()