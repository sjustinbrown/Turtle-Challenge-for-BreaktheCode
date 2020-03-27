#How BREAKTHECODE works

#LEVEL 1 
#Solve the maze using myPen Commands - see bottom of the code below for an example
#LEVEL 2 
#Use a loop to simplify + navigate the maze to finish
#LEVEL 3 - Month of Code Coaching
#Add a 4th level to the maze in a new color + restructure your code so that your turtle completes the maze with a for loop

#****Prizes only available for new clients not in Code Coaching or Code Class****


import turtle

screen = turtle.Screen()
screen.tracer(0)

mazeWidth=150

myMaze = turtle.Turtle()
myMaze.width(5)
myMaze.hideturtle()

myMaze.speed(0)

myMaze.penup()
myMaze.goto(-mazeWidth,190)


def drawMazeSection(color):
  myMaze.color(color)
  myMaze.pendown()
  myMaze.forward(mazeWidth)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(mazeWidth)
  myMaze.right(90)
  myMaze.forward(100)
  myMaze.right(90)
  myMaze.forward(mazeWidth)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(mazeWidth)
  myMaze.right(90)
  myMaze.forward(100)
  myMaze.right(90)
  x,y = myMaze.pos()
  myMaze.penup()  
  myMaze.goto(x, y-50)
  myMaze.pendown()
  myMaze.forward(30)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(200)
  myMaze.penup()
  myMaze.forward(40)
  myMaze.pendown()
  myMaze.forward(30)
  myMaze.penup()
  myMaze.goto(x,y-110)

for color in ["#FF0000","#0000FF","#00FF00"]:
  drawMazeSection(color)

screen.tracer(1)    
#Turtle Starting Point
myPen=turtle.Turtle()
myPen.penup()
myPen.goto(20,-180)
myPen.pendown()
myPen.shape('turtle')
myPen.color("#DB148E")
myPen.width(5)
myPen.left(90)

#Start of maze and sample commands
myPen.forward(70)
myPen.right(90)
myPen.forward(120)


  