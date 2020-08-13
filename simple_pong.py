# Classic Pong Game using Python 3
# By Gabrielle Viray

import turtle # graphics
import winsound

# Create Customized Window
window = turtle.Screen()
window.title("Classic Pong Game by @gabrielle_viray")
window.bgcolor("black")
window.setup(width=1000, height = 600) # Size of screen.
window.tracer(0)	# Stops window from updating to speed up game

# Score
player_1_score = 0
player_2_score = 0

# Ball
ball = turtle.Turtle()
ball.speed(0)	# Max Speed.
ball.shape("square")	# Square paddle.
ball.color("white")	
ball.penup() # No drawing when in motion.
ball.goto(0,0) # Middle of screen.
ball.dx = .4	# Moves by 2 pixels x-axis.
ball.dy = -.4 # Moves by 2 pixels y-axis.

# Scoring Pen
scoring_pen = turtle.Turtle()
scoring_pen.speed(0) # Animation Speed
scoring_pen.color("white")
scoring_pen.penup()
scoring_pen.hideturtle() 
scoring_pen.goto(0, 250)
scoring_pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Player 1 Paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)	# Max Speed.
paddle_1.shape("square")	# Square paddle.
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("white")	
paddle_1.penup() # No drawing when in motion.
paddle_1.goto(-450,0) # Left side of screen.

# Player 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)	# Max Speed.
paddle_2.shape("square")	# Square paddle.
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("white")	
paddle_2.penup() # No drawing when in motion.
paddle_2.goto(450,0) # Right side of screen.


#################################################
#                                               #
#            Player 1 Paddle Motion             #
#                                               #
#################################################

def paddle_1_up():
	y_coordinate = paddle_1.ycor() # ycor = turtle module that returns y coordinate.
	y_coordinate += 25
	paddle_1.sety(y_coordinate)

def paddle_1_down():
	y_coordinate = paddle_1.ycor() # ycor = turtle module that returns y coordinate.
	y_coordinate -= 25
	paddle_1.sety(y_coordinate)

#################################################
#                                               #
#            Player 2 Paddle Motion             #
#                                               #
#################################################

def paddle_2_up():
	y_coordinate = paddle_2.ycor() # ycor = turtle module that returns y coordinate.
	y_coordinate += 25
	paddle_2.sety(y_coordinate)

def paddle_2_down():
	y_coordinate = paddle_2.ycor() # ycor = turtle module that returns y coordinate.
	y_coordinate -= 25
	paddle_2.sety(y_coordinate)

#################################################
#                                               #
#                   Ball Motion                 #
#                                               #
#################################################

# Key Binding
window.listen() # Listen for input from keyboard.
window.onkeypress(paddle_1_up, "w") 
window.onkeypress(paddle_1_down, "s")

window.onkeypress(paddle_2_up, "Up") 
window.onkeypress(paddle_2_down, "Down")

# Main 
while True:
	window.update() # Updates Screen every iteration.
	scoring_pen.clear()
	scoring_pen.write("Player 1: {} Player 2: {}".format(player_1_score, player_2_score), align="center", font=("Courier", 24, "normal"))

	# Move ball.
	ball.setx(ball.xcor() + ball.dx) 
	ball.sety(ball.ycor() + ball.dy)

	# Top border.
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1	# Reverse ball direction.
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	# Bottom Border.
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1	# Reverse ball direction.
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	# Right Border.
	if ball.xcor() > 490:
		ball.goto(0,0)
		ball.dx *= -1	# Reverse ball direction.
		player_1_score += 1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	# Left Border.
	if ball.xcor() < -490:
		ball.goto(0,0)
		ball.dx *= -1	# Reverse ball direction.
		player_2_score += 1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	# Handle Collisions.
	if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
		ball.setx(440)
		ball.dx *= -1 
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
		ball.setx(-440)
		ball.dx *= -1 
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)