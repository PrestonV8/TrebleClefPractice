from tkinter import *
from Prestons_Circles import Notes
import random


def generate_note(select):
    space_E = Notes(canvas, 31, 48, "E")
    space_C = Notes(canvas, 49, 66, "C")
    space_A = Notes(canvas, 66, 83, "A")
    space_F = Notes(canvas, 83, 100, "F")
    line_E = Notes(canvas, 93, 110, "E")
    line_G = Notes(canvas, 76, 93, "G")
    line_B = Notes(canvas, 59, 76, "B")
    line_D = Notes(canvas, 41, 58, "D")
    line_F = Notes(canvas, 24, 40, "F")
    notes_available = [space_E, space_C, space_A, space_F, line_E, line_G, line_B, line_D, line_F]
    #notes_available = [space_F, space_A]
    chosen_note = notes_available[select]
    # chosen_note = random.choice(notes_available)
    for i in range(0, 9):
        if notes_available[i] != chosen_note:
            notes_available[i].clear()
        else:
            notes_available.append(chosen_note)
    return chosen_note


def random_pick():
    select = random.randint(0, 8)
    return select


def move_note():
    global WIDTH
    global HEIGHT
    global canvas
    global treble
    canvas.destroy()
    # after destroying the whole canvas, we're going to rebuild it :)
    canvas = Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.grid(row=2, column=0)
    treble = PhotoImage(file="treble.PNG")
    canvas.create_image(360, 70, image=treble)
    # spawning in the notes
    note = generate_note(random_select)

    def animate():
        if note.move():
            note.next_animate = canvas.after(25, animate)
            wrong()
        else:
            note.next_animate = canvas.after(25, animate)
    animate()
    # balls = [generate_note(random_select)]
    #
    # def balls_go(evt):
    #     for ball in balls:
    #         ball.go()
    #
    # def balls_stop(evt):
    #     for ball in balls:
    #         ball.stop()
    # balls_go(None)

    # if generate_note(random_select).move() == WIDTH:
    #     wrong()


def new_game():
    global SCORE
    global WRONG
    global score_frame
    global F
    global G
    global A
    global B
    global C
    global D
    global E
    global Quit_button
    global random_select
    SCORE = 0
    WRONG = 0
    score_frame.destroy()
    score_frame = Label(window, text="Score: {}\nMistakes: {}".format(SCORE, WRONG))
    score_frame.configure(bg="black", fg="yellow", font="Times 20 italic bold")
    score_frame.grid(row=1, column=0, columnspan=6)
    F.destroy()
    G.destroy()
    A.destroy()
    B.destroy()
    C.destroy()
    D.destroy()
    E.destroy()
    Quit_button.destroy()
    Quit_button = Button(button_frame, text="Quit", padx=25, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
                         command=quit_game)
    F = Button(button_frame, text="F", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
               borderwidth=0, command=button_F)
    G = Button(button_frame, text="G", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
               borderwidth=0, command=button_G)
    A = Button(button_frame, text="A", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
               borderwidth=0, command=button_A)
    B = Button(button_frame, text="B", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
               borderwidth=0, command=button_B)
    C = Button(button_frame, text="C", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
               borderwidth=0, command=button_C)
    D = Button(button_frame, text="D", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
               borderwidth=0, command=button_D)
    E = Button(button_frame, text="E", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
               borderwidth=0, command=button_E)
    Quit_button.grid(row=0, column=1, columnspan=10)
    F.grid(row=1, column=0)
    G.grid(row=1, column=1)
    A.grid(row=1, column=2)
    B.grid(row=1, column=3)
    C.grid(row=1, column=4)
    D.grid(row=1, column=5)
    E.grid(row=1, column=6)
    random_select = random_pick()
    move_note()
    # give_notes()


def correct():
    global SCORE
    global score_frame
    global random_select
    # when score frame is rebuilt, then it should rebuild with a point added on
    SCORE += 1
    score_frame = Label(window, text="Score: {}\nMistakes: {}".format(SCORE, WRONG))
    score_frame.configure(bg="black", fg="yellow", font="Times 20 italic bold")
    score_frame.grid(row=1, column=0, columnspan=6)
    # after scoring a point, the game will then present another note to move!
    random_select = random_pick()
    move_note()


def wrong():
    global score_frame
    global WRONG
    global canvas
    global WIDTH
    global HEIGHT
    global random_select
    score_frame.destroy()
    WRONG += 1
    score_frame = Label(window, text="Score: {}\nMistakes: {}".format(SCORE, WRONG))
    score_frame.configure(bg="black", fg="yellow", font="Times 20 italic bold")
    score_frame.grid(row=1, column=0, columnspan=6)
    if WRONG == 3:
        # the "canvas" lines are repeated from spawn_note(), might have to create a class?
        canvas.destroy()
        F.destroy()
        G.destroy()
        A.destroy()
        B.destroy()
        C.destroy()
        D.destroy()
        E.destroy()
        Quit_button.destroy()
        canvas = Canvas(window, width=WIDTH, height=HEIGHT)
        canvas.grid(row=0, column=0)
        game_over = canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", font="Times 75 italic bold")
    else:
        random_select = random_pick()
        move_note()


def ID_note():
    return generate_note(random_select).give_letter()


def right_or_wrong(correct_letter):
    if ID_note() == correct_letter:
        # call correct function
        correct()
    else:
        # call wrong function
        wrong()


def button_F():
    right_or_wrong("F")


def button_G():
    right_or_wrong("G")


def button_A():
    right_or_wrong("A")


def button_B():
    right_or_wrong("B")


def button_C():
    right_or_wrong("C")


def button_D():
    right_or_wrong("D")


def button_E():
    right_or_wrong("E")


def quit_game():
    window.quit()


window = Tk()

# random_select isolates the random generator so that there won't be any repeats of any functions
random_select = random_pick()

window.title("Music Zapper")
window.geometry("720x600")
window.configure(bg="black")


introduction = Label(window, text="Welcome to Treble Clef Practice!", bg="black", fg="yellow",
                     font="Times 20 italic bold")
introduction.grid(row=0, column=0)

# score of notes
SCORE = 0
WRONG = 0
score_frame = Label(window, text="Score: {}\nMistakes: {}".format(SCORE, WRONG))
score_frame.configure(bg="black", fg="yellow", font="Times 20 italic bold")
score_frame.grid(row=1, column=0, columnspan=6)

# canvas for circles
WIDTH = 720
HEIGHT = 125
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.grid(row=2, column=0)

treble = PhotoImage(file="treble.PNG")
canvas.create_image(360, 70, image=treble)
# label = Label(window, image=treble)
# label.grid(row=2, column=0)

# button frame
button_frame = Frame(window)
button_frame.configure(bg="black", borderwidth=2)
button_frame.grid(row=3, column=0, columnspan=2, rowspan=2, sticky="w")

# note buttons
New_game_button = Button(button_frame, text="New Game", padx=40, pady=20, bg="black", fg="yellow",
                         font="Times 20 italic bold", command=new_game)
Quit_button = Button(button_frame, text="Quit", padx=25, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
                     command=quit_game)
F = Button(button_frame, text="F", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
           borderwidth=0, command=button_F)
G = Button(button_frame, text="G", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
           borderwidth=0, command=button_G)
A = Button(button_frame, text="A", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
           borderwidth=0, command=button_A)
B = Button(button_frame, text="B", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
           borderwidth=0, command=button_B)
C = Button(button_frame, text="C", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
           borderwidth=0, command=button_C)
D = Button(button_frame, text="D", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
           borderwidth=0, command=button_D)
E = Button(button_frame, text="E", padx=30, pady=20, bg="black", fg="yellow", font="Times 20 italic bold",
           borderwidth=0, command=button_E)

# button placement
New_game_button.grid(row=0, column=0, columnspan=5)
Quit_button.grid(row=0, column=1, columnspan=10)
F.grid(row=1, column=0)
G.grid(row=1, column=1)
A.grid(row=1, column=2)
B.grid(row=1, column=3)
C.grid(row=1, column=4)
D.grid(row=1, column=5)
E.grid(row=1, column=6)

window.mainloop()
