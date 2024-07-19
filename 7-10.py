from tkinter import *
import turtle as t
main_score = 0
main = Tk()  # main screen
text_field = Entry()
text_field.pack()
greeting_label = Label(text="Choose a game!")
greeting_label.pack()

def bounce_page():
    win = t.Screen()
    win.title('Bounce')
    win.bgcolor('white')
    win.setup(width=1000, height=300)
    win.tracer(0)  # draw at once

    # score
    score = 0

    # Left Paddle
    left_pad = t.Turtle()  # assign it w animation
    left_pad.speed(0)  # speed of animation
    left_pad.shape('circle')
    left_pad.color('black')
    left_pad.shapesize(stretch_wid=5, stretch_len=.5)  # stretch paddle
    left_pad.penup()
    left_pad.goto(-450, 0)
    # Right Paddle
    right_pad = t.Turtle()  # assign it w animation
    right_pad.speed(0)  # speed of animation
    right_pad.shape('circle')
    right_pad.color('black')
    right_pad.shapesize(stretch_wid=5, stretch_len=.5)  # stretch paddle
    right_pad.penup()
    right_pad.goto(450, 0)
    # ball
    ball = t.Turtle()  # assign it w animation
    ball.speed(0)  # speed of animation
    ball.shape('circle')
    ball.color('blue')
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 3  # speed, setting x to move
    ball.dy = 3  # so every time the ball moves, it moves by 2 pixels.
    # add scoring system by drawing
    pen = t.Turtle()
    pen.speed(0)  # animation speed not movement
    pen.color('black')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 110)  # top of board is 300 and we want at tope so
    pen.write("Score 0", align="center", font=("Ariel", 16, "normal"))

    #  everytime score made it needs to be updated

    # movement
    def left_pad_up():  # this function moves paddle a
        y = left_pad.ycor()  # returns y coordinate as y from turtle module
        y += 20  # adds 20 pixels to y coordinate
        left_pad.sety(y)  # sets y to new y

    def left_pad_down():  # this function moves paddle a
        y = left_pad.ycor()  # returns y coordinate as y from turtle module
        y -= 20  # adds 20 pixels to y coordinate
        left_pad.sety(y)  # sets y to new y

    def right_pad_up():  # this function moves paddle a
        y = right_pad.ycor()  # returns y coordinate as y from turtle module
        y += 20  # adds 20 pixels to y coordinate
        right_pad.sety(y)  # sets y to new y

    def right_pad_down():  # this function moves paddle a
        y = right_pad.ycor()  # returns y coordinate as y from turtle module
        y -= 20  # adds 20 pixels to y coordinate
        right_pad.sety(y)  # sets y to new y

    # keyboard binding
    win.listen()  # tells it to listen for keyboard input

    win.onkeypress(left_pad_up, "q")  # when user presses w, call function paddle_a_up.
    win.onkeypress(left_pad_down, "a")  # when user presses s, down.
    win.onkeypress(right_pad_up, "p")
    win.onkeypress(right_pad_down, "l")
    # main game loop
    while True:
        win.update()  # continually update w tracer
        ball.setx(ball.xcor() + ball.dx)  # goes 2 pixels every loop while in bounds (x axis)
        ball.sety(ball.ycor() + ball.dy)  # 2 pixels every loop.  pairs with dx in balls

        # Borders that bounce and score
        if ball.ycor() > 140:
            ball.sety(140)  # eliminates complications
            ball.dy *= -1  # reverses the direction
            #cscore += 1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Ariel", 16, "normal"))

        if ball.ycor() < -140:
            ball.sety(-140)  # eliminates complications
            ball.dy *= -1
            score += 1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Ariel", 16, "normal"))
        # borders that take away points and restarts ball
        if ball.xcor() > 490:  # off screen past paddle
            ball.goto(0, 0)  # back to center
            ball.dx *= -1  # change direction
            score -= 1  # take away point
            pen.clear()  # or it will just keep writing on itself
            pen.write("Score: {}".format(score), align="center", font=("Ariel", 16, "normal"))
        #  update score in format form to print new score as {}
        if ball.xcor() < -490:  # off screen past paddle
            ball.goto(0, 0)  # back to center
            ball.dx *= -1
            score -= 1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Ariel", 16, "normal"))
        # right paddle hit
        if ball.xcor() > 440 and ball.xcor() < 450 and ball.ycor() < right_pad.ycor() + 40 and ball.ycor() > right_pad.ycor() - 40:
            ball.setx(440)  # kept getting stuck paddle
            ball.dx *= -1  # reverse direction
        #left paddle hit
        if ball.xcor() < -440 and ball.xcor() > -450 and ball.ycor() < left_pad.ycor() + 40 and ball.ycor() > left_pad.ycor() - 40:
            ball.setx(-440)  # kept getting stuck paddle
            ball.dx *= -1
# buttons main screen
bounce_button = Button(main, text = 'Bounce',
                    font = ('Ariel',15), bg="white", fg="black",
                    height = 2, width = 30, command=lambda:bounce_page())
bounce_button.pack()

game2_button = Button(main, text = 'Game 2',
                         font = ('Ariel', 15), bg="white", fg="black",
                         height = 2, width = 30, command=lambda:())  # fixme add game
game2_button.pack()

game3_button = Button(main, text = 'Game 3',
                         font = ('Ariel', 15), bg="white", fg="black",
                         height = 2, width = 30, command=lambda:())
game3_button.pack()

game4_button = Button(main, text = 'Game 4',
                         font = ('Ariel', 15), bg="white", fg="black",
                         height = 2, width = 30, command=lambda:())
game4_button.pack()

game5_button = Button(main, text = 'Quit',
                         font = ('Ariel', 15), bg="white", fg="black",
                         height = 2, width = 30, command=lambda:quit())
game5_button.pack()
main.mainloop()












