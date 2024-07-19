from tkinter import *
import turtle as t

# Global variables
main_score = 0
main = Tk()  # main screen
text_field = Entry()
text_field.pack()
greeting_label = Label(text="Choose a game!")
greeting_label.pack()

def bounce_page():
    global main_score

    def quit_game():
        global main_score
        main_score = score
        win.bye()
        main.deiconify()
        main.title(f"Your final score was: {score}")

    def game_over():
        nonlocal running
        running = False
        win.bye()
        main.deiconify()
        main.title(f"Your final score was: {score}")

    # Setup a new turtle screen
    win = t.Screen()
    win.title('Bounce')
    win.bgcolor('white')
    win.setup(width=1000, height=300)
    win.tracer(0)

    # Score
    score = 0
    running = True

    # Stick Figure (Left Paddle)
    stick_figure = t.Turtle()
    stick_figure.speed(0)
    stick_figure.shape('square')
    stick_figure.color('black')
    stick_figure.shapesize(stretch_wid=5, stretch_len=1)
    stick_figure.penup()
    stick_figure.goto(-450, -100)

    # Ball
    ball = t.Turtle()
    ball.speed(0)
    ball.shape('circle')
    ball.color('blue')
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1.5
    ball.dy = 1.5

    # Pen for Score
    pen = t.Turtle()
    pen.speed(0)
    pen.color('black')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 110)
    pen.write("Score: 0", align="center", font=("Ariel", 16, "normal"))

    # Stick Figure Jump
    def stick_figure_jump():
        y = stick_figure.ycor()
        y += 100  # Jump height
        stick_figure.sety(y)
        win.ontimer(lambda: stick_figure.sety(-100), 200)  # Return to ground after 200ms

    # Keyboard Binding
    win.listen()
    win.onkey(stick_figure_jump, "space")

        # Quit button
    quit_button = Button(win._root, text='Quit', font=('Arial', 15), bg="white", fg="black", height=2, width=10, command=quit_game)
    quit_button.place(x=450, y=150)

    # Game Loop
    def game_loop():
        nonlocal score, running

        while running:
            try:
                win.update()
            except t.Terminator:
                break

            # Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Top and bottom border collision
            if ball.ycor() > 140:
                ball.sety(140)
                ball.dy *= -1

            if ball.ycor() < -140:
                ball.sety(-140)
                ball.dy *= -1
                score += 1
                pen.clear()
                pen.write("Score: {}".format(score), align="center", font=("Ariel", 16, "normal"))

            # Right edge collision (no score change)
            if ball.xcor() > 490:
                ball.setx(490)
                ball.dx *= -1

            # Left edge collision (game over)
            if ball.xcor() < -490:
                game_over()

            # Stick figure collision
            if ball.xcor() > -460 and ball.xcor() < -440 and ball.ycor() < stick_figure.ycor() + 50 and ball.ycor() > stick_figure.ycor() - 50:
                ball.setx(-440)
                ball.dx *= -1

            # Increase speed at score milestones
            if score in {10, 15, 20, 25}:
                ball.dx *= 1.1
                ball.dy *= 1.1

            # Game over at -3 points
            if score <= -3:
                game_over()

    # Start the game loop
    main.withdraw()
    game_loop()

# Buttons on main screen
bounce_button = Button(main, text='Bounce', font=('Ariel', 15), bg="white", fg="black", height=2, width=30, command=bounce_page)
bounce_button.pack()

game2_button = Button(main, text='Game 2', font=('Ariel', 15), bg="white", fg="black", height=2, width=30, command=lambda:())
game2_button.pack()

game3_button = Button(main, text='Game 3', font=('Ariel', 15), bg="white", fg="black", height=2, width=30, command=lambda:())
game3_button.pack()

game4_button = Button(main, text='Game 4', font=('Ariel', 15), bg="white", fg="black", height=2, width=30, command=lambda:())
game4_button.pack()

quit_button = Button(main, text='Quit', font=('Ariel', 15), bg="white", fg="black", height=2, width=30, command=main.quit)
quit_button.pack()

main.mainloop()
