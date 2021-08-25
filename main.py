import turtle 
import random
import time

#-------------------------Game Code----------------------------
#-----Basic Setup------
#screen
screen= turtle.getscreen()
screen.bgcolor("white")
screen.setup(width=750, height=500)
turtle.ht()

#-----------------cover page: ------------
#bg color
bg2 = turtle.Turtle()
bg2.speed(0)
bg2.ht()
bg2.penup()
bg2.goto(-400, 250)
bg2.pendown()
bg2.color('navy blue')
bg2.begin_fill()
for i in range(2):
  bg2.forward(800)
  bg2.right(90)
  bg2.forward(500)
  bg2.right(90)
bg2.end_fill()

#lines
def travel (x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()


t = turtle.Turtle()
t.speed(0)
t.ht()

t.color ("steel blue")
travel(-170, 250)
t.width(40)
t.right(35)
t.forward(850)

t.color ("light sky blue")
travel(-240, 260)
t.forward(850)

t.color ("sky blue")
travel(-290, 250)
t.forward(850)

t.color ("powder blue")
travel(-340, 250)
t.forward(900)

t.color ("cornflower blue")
travel(-390, 250)
t.forward(900)

t.color ("royal blue")
travel(-440, 250)
t.forward(900)


#Title
travel(10, 10)
t.color ("white")
t.write("PONG", font = ("Times New Roman", 40, 'bold'), align = "center")
travel(0, -25)
t.color ("navy blue")
t.write("AI-liance", font = ("Times New Roman", 15, 'bold'), align = "center")
#---------------------Game intro and input-------------
print("Welcome to pong! Press the 'up' and 'down' keys to control the right paddle, 'w' and 's' keys to control the left paddle :)")

#------------Get game mode + info--------------------
single = False

def gamemode():
  while True:
    gamemodeinput = input ("Enter 's' for single player or 'm' for multiplayer: ")
    gamemodeinput = gamemodeinput.lower()
    global single
    if gamemodeinput == 's':
      single = True 
      print ("You're the right paddle!")
      break
    elif gamemodeinput == 'm': 
      break
    else:
      print ("Please enter s or m.")
gamemode()

#number of balls
twoball = False

def numballs():
  while True:
    try: 
      getnumball = int(input("Enter # of balls (1 or 2): "))
      if getnumball == 1 or getnumball == 2:
        if getnumball == 1:
          break
        else:
          global twoball
          twoball = True  
          break
      else:
        print ("Please enter 1 or 2. ")
    except:
      print("Not a number. Enter 1 or 2.")
numballs()

increasespeed = False
def growspeed():
  while True:
    usergrowspeed = input("Wanna have the speed increase as you go? (y/n): ")
    usergrowspeed = usergrowspeed.lower()
    if usergrowspeed == 'y' or usergrowspeed == 'n':
      if usergrowspeed == 'y':
        global increasespeed
        increasespeed = True
        break
      else:
        break
    else:
      print ("Not y or n. Try again.")
growspeed()

time.sleep(2)
t.clear()
bg2.clear()

#-------------------------GAME---------------

bg = turtle.Turtle()
bg.speed(0)
bg.ht()
bg.penup()
bg.goto(-340, 180)
bg.pendown()
bg.color(0, 0, 50)
bg.begin_fill()
for i in range(2):
  bg.forward(680)
  bg.right(90)
  bg.forward(370)
  bg.right(90)
bg.end_fill()

#paddle shape
screen.register_shape("paddle", ((0,0), (13,0),(13,100),(0,100)))

#---------Rectangle border for the game--------
border = turtle.Turtle()
border.speed(0)
border.ht()
border.penup()
border.goto(-340, 180)
border.pendown()
border.color('gold')
border.width(8)
for i in range(2):
  border.forward(680)
  border.right(90)
  border.forward(370)
  border.right(90)


# Middle line 
midline = turtle.Turtle()
midline.speed(0)
midline.ht()
midline.penup()
midline.goto(3,178)
midline.pendown()
midline.right(90)
midline.color("gold")
midline.width(8)
for line in range(9):
  midline.forward(15)
  midline.penup()
  midline.forward(29)
  midline.pendown()

#---------left paddle---------
leftpad = turtle.Turtle()
leftpad.speed(0)
leftpad.color("white")   #we can change this later
leftpad.shape("paddle")
leftpad.setheading(90)
leftpad.penup()
leftpad.goto(-308, -50) #we can change this after border is made

#--------right paddle--------
rightpad = turtle.Turtle()
rightpad.speed(0)
rightpad.color("white")   #we can change this later
rightpad.shape("paddle")
rightpad.setheading(90)
rightpad.penup()
rightpad.goto(328, -50) #we can change this after border is made

#--------ball 1-------------
ball1 = turtle.Turtle()
ball1.speed(1)
ball1.color("white")  #we can change this later
ball1.shape("circle")
ball1.penup()
ball1.goto(0,0)

if twoball == True:
  ball2 = turtle.Turtle()
  ball2.color("white")
  ball2.speed(0)
  ball2.shape("circle")
  ball2.penup()
  ball2.goto(0,0)

#------variables for how much the ball's x and y change----
ball1.dx = 4
ball1.dy = 4

if twoball == True:
  ball2.dx = -4
  ball2.dy = -4
  ball2.origspeed = -4

ball1.origspeed = 4

balls = [ball1]
if twoball == True:
  balls.append(ball2)

#----------players initial score--------
#Multiplayer
leftscore = 0
rightscore = 0

#single player
singlescore = 0
lives = 5

#-----------Show the score above the rectangle border------
score = turtle.Turtle()
score.speed(0)
score.ht()
score.color(0, 0, 50)
score.penup()
score.goto(0,190)
style = ('Times New Roman', 18, 'bold')

if single == False:
  score.write("Player 1: 0          Player 2: 0", font = style, align = 'center')
else:
  score.write("Lives left: 5          Score: 0", font = style, align = 'center')

#winner display
winner = turtle.Turtle()
winner.speed(0)
winner.ht()
winner.penup()

def winnerbox():
  winner.goto(-150,50)
  winner.pendown()
  #light cyan
  winner.color(255, 214, 0, 0.95)
  winner.begin_fill()
  for i in range (2):
    winner.forward (300)
    winner.right(90)
    winner.forward(100)
    winner.right(90)
  winner.end_fill()
  winner.penup()
  winner.goto(0,-5)
  winner.color(0, 0, 50)  

#------------------------Quit Button--------------
quit = turtle.Turtle()
quit.speed(0)
quit.ht()
#quit button 
def drawquit():
  quit.color(255, 214, 0)
  quit.penup()
  quit.goto(270, -210)
  quit.pendown()
  quit.begin_fill()
  for i in range (2):
    quit.forward(60)
    quit.right(90)
    quit.forward(40)
    quit.right (90)
  quit.end_fill()
  quit.color(0, 0, 50)
  quit.penup()
  quit.goto(286, -233)
  quit.write("QUIT", font=("Times New Roman", 10, "bold"))
drawquit()

#---------------------quit functionality------------------
running = True

#QUIT FUNCTIONALITY
def gameend(x, y):
  if (x >= 270 and x <= 330 and y >= -250 and y <= -210):
    global running
    running = False
#send click info
screen.onscreenclick(gameend)

#----------Functions to move paddles up and down------------
#-------left paddle move up--------
def leftpadup():
  leftpad.forward(50)
#------left paddle move down-----
def leftpaddown():
  leftpad.backward(50)

#-----right paddle move up------
def rightpadup():
  rightpad.forward(50)

#-----right paddle move down----
def rightpaddown():
  rightpad.backward(50)

#-------------Assign keys to paddle movement------------
screen.listen()
screen.onkey(leftpadup, 'w')
screen.onkey(leftpaddown,'s')
screen.onkey(rightpadup, 'Up')
screen.onkey(rightpaddown, 'Down')

#---------------Run more smoothly----------
screen.tracer(0)
#---------------------------MAIN LOOP --------------------
while running == True:
  #updates the screen
  screen.update()

  for ball in balls:
    #set ball x and ball y by adding the xcor and y xor with the variable for how much the x and y change
    ball.setx(ball.xcor() + ball.dx)  
    ball.sety(ball.ycor() + ball.dy)

    #set up border so ball bounces off top and bottom
    #bottom border
    if ball.ycor() <= -190:
      ball.dy *= -1
    #top border
    if ball.ycor() >= 180:
      ball.dy *= -1
    #--------------left and right border -----------------
    #increase score
    #left border BALL----------------------
    if ball.xcor() <= -332:
      #if multiplayer, add score to whoever wins and restart ball at center
      if single == False:
        if ball.dx < 0:
          ball.dx = -ball.origspeed
        else:
          ball.dx = ball.origspeed
        if ball.dy < 0:
          ball.dy = -ball.origspeed
        else: 
          ball.dy = ball.origspeed
        #add one to right player
        rightscore += 1
        #erase old score
        score.clear()
        #write new score
        score.write( "Player 1: {}          Player 2: {}".format(leftscore, rightscore), align = "center", font = style)

        #if right hasn't won (we can change the 3 point to something else later)
        if rightscore < 5: 
          #give player a second to recover
          time.sleep(1)
          #go to center
          ball.goto(0,0)
          #random angle
          ball.setheading(random.randint(-30, 30))
          #change direction
          ball.dx *= 1
      #if single is true, restart ball and give 3 extra points to player
      else:
        #make ball go back to center
        ball.goto(0,0)
        #random angle
        ball.setheading(random.randint(-180, 180))
        #change direction
        ball.dx *= 1
        #increase score
        singlescore += 3
        #erase old score
        score.clear()
        #write new score
        score.write("Lives left: {}          Score: {}".format (lives, singlescore), font = style, align = 'center')

    #right border BALL -----------------------------------
    elif ball.xcor() >= 332:
      if ball.dx < 0:
        ball.dx = -ball.origspeed
      else:
        ball.dx = ball.origspeed
      if ball.dy < 0:
        ball.dy = -ball.origspeed
      else: 
        ball.dy = ball.origspeed
      #if multiplayer
      if single == False:
        #add one to left player score
        leftscore += 1
        #erase old score
        score.clear()
        #write new score
        score.write("Player 1: {}          Player 2: {}".format(leftscore, rightscore), align = "center", font = style)

        #if left hasn't won
        if leftscore < 5:
          time.sleep(1)
          #make ball go back to center
          ball.goto(0,0)
          #random angle
          ball.setheading(random.randint(-180, 180))
          #change direction
          ball.dx *= 1
      #if single player, make player lose a life. 
      else:
        time.sleep(1)
        #make ball go back to center
        ball.goto(0,0)
        #random angle
        ball.setheading(random.randint(-180, 180))
        #change direction
        ball.dx *= 1
        lives -= 1
        #erase old score
        score.clear()
        #write new score
        score.write("Lives left: {}          Score: {}".format (lives, singlescore), font = style, align = 'center')

    #-------------paddle collision-------------------
    #check if ball touches paddles and make it bounce back
    #left paddle 
    if abs(leftpad.xcor() - ball.xcor()) <= 10 and (leftpad.ycor() <= ball.ycor() <= leftpad.ycor() + 100):
      ball.dx *= -1   
      if increasespeed == True:
        if ball.dx < 1:
          ball.dx -= 0.1
        else: 
          ball.dx += 0.1

        if ball.dy < 1:
          ball.dy -= 0.1
        else: 
          ball.dy += 0.1

    #right paddle
    elif abs(ball.xcor() - rightpad.xcor()) <= 10 and (rightpad.ycor() <= ball.ycor() <= rightpad.ycor() + 100):
      ball.dx *= -1
      #if user wants increasing speed
      if increasespeed == True:
        if ball.dx < 1:
          ball.dx -= 0.5
        else: 
          ball.dx += 0.5

        if ball.dy < 1:
          ball.dy -= 0.5
        else: 
          ball.dy += 0.5

      #if it's single player, add to player's score
      if single == True:
        #increase score
        singlescore += 1
        #erase old score
        score.clear()
        #write new score
        score.write("Lives left: {}          Score: {}".format (lives, singlescore), font = style, align = 'center')

  #computer player (single player mode)
  if single == True:  
    #figure out which ball is closer if there are two
    closestball = balls[0]
    for ball in balls:
      if ball.xcor() < closestball.xcor():
        closestball = ball

    #AI
    if leftpad.ycor() < closestball.ycor() and abs(leftpad.xcor() - closestball.xcor()) <= 25 and abs(leftpad.ycor() - closestball.ycor()) > 15:
      leftpadup()

    elif leftpad.ycor() > closestball.ycor() and abs(leftpad.xcor() - closestball.xcor()) <= 25 and abs(leftpad.ycor() - closestball.ycor()) > 15:
      leftpaddown()

    #winner/loser announcement
  #if multiplayer, announce winner
  if single == False:
    if leftscore == 5 or rightscore == 5:
      break
  #if single player and lives == 0, exit.
  else:
    if lives <= 0:
      break


      

#updates screen
screen.tracer(1)

#hide ball
for ball in balls: 
  #after game end display
  ball.ht()


if single == False: 
  winnerbox()
  if leftscore == 5:
    winner.write("Player 1 won!", align = "center", font = style)
  elif rightscore == 5:
    winner.write("Player 2 won!", align = "center", font = style)
else: 
  winnerbox()
  winner.write("You scored {} points!".format(singlescore), align = "center", font = style)

time.sleep(1)
winner.clear()
winnerbox()
winner.write("Thanks For Playing!", align = "center", font = style)

