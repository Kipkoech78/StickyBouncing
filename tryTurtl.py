from tkinter import *
from tkinter import messagebox
import turtle as t

main = Tk()  # main screen
text_field = Entry()
text_field.pack()
greeting_label = Label(text="Choose a game!")
greeting_label.pack()

game_running = False  # Flag to indicate if the game is running
main_score = 0  # Store the main score to be shown on the main page

def bounce_page():
    global game_running, main_score
    if game_running:
        return  # Avoid multiple instances

    game_running = True
    main.withdraw()  # Hide the main window

    win = t.Screen()
    win.title('Bounce')
    win.bgcolor('white')
    win.setup(width=1000, height=300)
    win.tracer(0)  # draw at once

    # score
    score = 0

    # Stick figure
    stick_figure = t.Turtle()
    stick_figure.speed(0)
    stick_figure.shape('square')
    stick_figure.color('black')
    stick_figure.shapesize(stretch_wid=3, stretch_len=1)
    stick_figure.penup()
    stick_figure.goto(-450, -100)

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
    pen.write("Score: 0", align="center", font=("Arial", 16, "normal"))

    def jump():
        y = stick_figure.ycor()
        y += 60  # Jump by 60 pixels
        stick_figure.sety(y)
        main.after(500, lambda: stick_figure.sety(-100))  # Fall back after 500ms

    # Quit button
    def quit_game():
        global game_running, main_score
        game_running = False
        main_score = score
        win.bye()
        main.deiconify()
        main.title(f"Score: {main_score}")
        
    # keyboard binding
    win.listen()  # tells it to listen for keyboard input
    win.onkeypress(jump, "space")

    # Create a quit button in the turtle window
    quit_button = t.Turtle()
    quit_button.hideturtle()
    quit_button.penup()
    quit_button.goto(400, 130)
    quit_button.write("Quit", align="center", font=("Arial", 16, "normal"))
    
    def check_click(x, y):
        if 370 < x < 430 and 110 < y < 150:
            quit_game()
    
    win.onscreenclick(check_click)
    
    def game_loop():
        nonlocal score
        if not game_running:
            return

        try:
            win.update()  # continually update w tracer
            ball.setx(ball.xcor() + ball.dx)  # goes 3 pixels every loop while in bounds (x axis)
            ball.sety(ball.ycor() + ball.dy)  # 3 pixels every loop.  pairs with dx in balls

            # Borders that bounce and score
            if ball.ycor() > 140:
                ball.sety(140)  # eliminates complications
                ball.dy *= -1  # reverses the direction

            if ball.ycor() < -140:
                ball.sety(-140)  # eliminates complications
                ball.dy *= -1
                score += 1
                if score in [10, 15, 20, 25]:
                    ball.dx *= 1.5
                    ball.dy *= 1.5
                pen.clear()
                pen.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

            # borders that take away points and restarts ball
            if ball.xcor() > 490:  # off screen past paddle
                ball.goto(0, 0)  # back to center
                ball.dx *= -1  # change direction
                score -= 1  # take away point
                if score == -3:
                    messagebox.showinfo("Game Over", "You lose!")
                    quit_game()
                pen.clear()  # or it will just keep writing on itself
                pen.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

            if ball.xcor() < -490:  # off screen past paddle
                ball.goto(0, 0)  # back to center
                ball.dx *= -1

            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
            main.after(10, game_loop)  # Schedule the next game loop
        except t.Terminator:
            return

    game_loop()

# buttons main screen
bounce_button = Button(main, text='Bounce',
                       font=('Arial', 15), bg="white", fg="black",
                       height=2, width=30, command=bounce_page)
bounce_button.pack()

game2_button = Button(main, text='Game 2',
                      font=('Arial', 15), bg="white", fg="black",
                      height=2, width=30, command=lambda: print("Game 2"))
game2_button.pack()

game3_button = Button(main, text='Game 3',
                      font=('Arial', 15), bg="white", fg="black",
                      height=2, width=30, command=lambda: print("Game 3"))
game3_button.pack()

game4_button = Button(main, text='Game 4',
                      font=('Arial', 15), bg="white", fg="black",
                      height=2, width=30, command=lambda: print("Game 4"))
game4_button.pack()

game5_button = Button(main, text='Quit',
                      font=('Arial', 15), bg="white", fg="black",
                      height=2, width=30, command=main.quit)
game5_button.pack()

main.mainloop()
