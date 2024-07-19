from tkinter import *
import turtle as t
from tkinter import messagebox  # Import messagebox

# Global variables
main_score = 0
highest_score = 0  # Variable to store highest score reached

def bounce_page():
    global main_score, highest_score

    def quit_game():
        global main_score, highest_score
        main_score = highest_score  # Set main_score to highest score reached
        win.bye()
        main.deiconify()
        main.title(f"Your highest score was: {highest_score}")

    def game_over():
        global highest_score
        nonlocal running, score
        running = False
        if score > highest_score:
            highest_score = score  # Update highest score if current score is higher
        win.bye()
        main.deiconify()
        main.title(f"You lose! Highest score: {highest_score}")
        # Add a messagebox to display "You lose"
        messagebox.showinfo("Game Over", f"You lose!\nHighest Score: {highest_score}")

    def game_over_0():
        nonlocal score, running
        if score == -3:
            running = False
            win.bye()
            main.deiconify()
            main.title(f"You lose! Highest score: {highest_score}")
            messagebox.showinfo("Game Over", "You lose!")

    # Setup a new turtle screen
    win = t.Screen()
    win.title('Bounce')
    win.bgcolor('white')
    win.setup(width=1000, height=400)
    win.tracer(0)

    # Draw the frame
    frame = t.Turtle()
    frame.speed(0)
    frame.color('black')
    frame.penup()
    frame.goto(-500, 150)
    frame.pendown()
    frame.pensize(3)
    for _ in range(2):
        frame.forward(1000)
        frame.right(90)
        frame.forward(300)
        frame.right(90)
    frame.hideturtle()

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
    ball.dx = 1.5  # Adjust initial speed
    ball.dy = 1.5

    # Pen for Score
    pen = t.Turtle()
    pen.speed(0)
    pen.color('black')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 110)
    pen.write("Score: 0", align="center", font=("Arial", 16, "normal"))

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
        global highest_score  # Use global keyword for highest_score
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
                pen.write("Score: {}".format(score), align="center", font=("Arial", 16, "normal"))

            # Right edge collision (no score change)
            if ball.xcor() > 490:
                ball.setx(490)
                ball.dx *= -1

            # Left edge collision (deduct score)
            if ball.xcor() < -490:
                if score > -3:
                    ball.goto(0, 0)  # Reset ball to center
                    ball.dx *= -1  # Change direction
                    score -= 1  # Deduct score
                    pen.clear()
                    pen.write("Score: {}".format(score), align="center", font=("Arial", 16, "normal"))
                else:
                    game_over_0()  # Check for game over condition

            # Stick figure collision
            if -460 < ball.xcor() < -440 and stick_figure.ycor() - 50 < ball.ycor() < stick_figure.ycor() + 50:
                ball.setx(-440)
                ball.dx *= -1

            # Increase speed at score milestones
            if score in {10, 15, 20, 25}:
                ball.dx *= 1.04
                ball.dy *= 1.04

    # Start the game loop
    main.withdraw()
    game_loop()

# Initialize main Tkinter window
main = Tk()
main.title("Game Selection")

# Buttons on main screen
bounce_button = Button(main, text='Bounce', font=('Arial', 15), bg="white", fg="black", height=2, width=30, command=bounce_page)
bounce_button.pack()

game2_button = Button(main, text='Game 2', font=('Arial', 15), bg="white", fg="black", height=2, width=30, command=lambda:())
game2_button.pack()

game3_button = Button(main, text='Game 3', font=('Arial', 15), bg="white", fg="black", height=2, width=30, command=lambda:())
game3_button.pack()

game4_button = Button(main, text='Game 4', font=('Arial', 15), bg="white", fg="black", height=2, width=30, command=lambda:())
game4_button.pack()

quit_button_main = Button(main, text='Quit', font=('Arial', 15), bg="white", fg="black", height=2, width=30, command=main.quit)
quit_button_main.pack()

# Start Tkinter main loop
main.mainloop()
