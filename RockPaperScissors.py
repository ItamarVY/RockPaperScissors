import turtle
from time import sleep
import random
import math

Rock = turtle.Turtle()
paper = turtle.Turtle()
Scissors = turtle.Turtle()
stutos = turtle.Turtle()
wn = turtle.Screen()

# Image filenames
paper_image1 = "Paper clicked1.gif" 
paper_image2 = "Paper Unclicked1.gif"
Rock_image2 = "Rock clicked1.gif"
Rock_image1 = "Rock Unclicked1.gif"
Scissors_image2 = "Scissors clicked1.gif"
Scissors_image1 = "Scissors Unclicked1.gif"
Won_image = "Won.gif"
Lost_image = "Lost.gif"
none_image = "None.gif"
tie_image = "Tie.gif"

# Adding the images to the turtle window
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

# Changing the turtle shape to the images
paper.shape(paper_image1)
Rock.shape(Rock_image1)
Scissors.shape(Scissors_image1)
stutos.shape(none_image)

# Setting th turtles pos
paper.pu() 
paper.setpos(100, 0)
Rock.pu()
Rock.setpos(0, 0)
Scissors.pu()
Scissors.setpos(-100, 0)
stutos.pu()
stutos.setpos(0, 300)

# Creating a function that will happend when each button clicked
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

# When the turtle is clicked it calls the functions
paper.onclick(PaperClicked)
Rock.onclick(RockClicked)
Scissors.onclick(ScissorsClicked)



turtle.mainloop()