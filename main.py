import tkinter as tk
from PIL import Image, ImageTk
import random
import os

def read_score(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                return int(f.read())
            except:
                return 0
    return 0

def write_score(filename, score):
    with open(filename, "w") as f:
        f.write(str(score))

choices = {-1: "Rock", 0: "Paper", 1: "Scissors"}
youDict = {"Rock": -1, "Paper": 0, "Scissors": 1}

score = read_score("currentscore.txt")
highscore = read_score("highscore.txt")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("650x500")
root.config(bg="#282c34")

def load_image(path, size=(120,120)):
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

images = {
    "Rock": load_image("rock.png"),
    "Paper": load_image("paper.png"),
    "Scissors": load_image("scissors.png")
}

def play(player_choice):
    global score, highscore

    com = random.choice([-1, 0, 1])

    if com == youDict[player_choice]:
        result = "It's a draw!"
        color = "orange"
    elif (com == -1 and youDict[player_choice] == 0) or \
         (com == 0 and youDict[player_choice] == 1) or \
         (com == 1 and youDict[player_choice] == -1):
        result = "🎉 You WIN!"
        color = "green"
        score += 1
    else:
        result = "You lose!"
        color = "red"

    # Save current score
    write_score("currentscore.txt", score)

    # Update high score
    if score > highscore:
        highscore = score
        write_score("highscore.txt", highscore)

    # GUI
    lbl_player_choice.config(image=images[player_choice])
    lbl_com_choice.config(image=images[choices[com]])
    lbl_result.config(text=result, fg=color)
    lbl_score.config(text=f"Score: {score}   |   High Score: {highscore}")

def reset_score():
    global score
    score = 0
    write_score("currentscore.txt", score)
    lbl_score.config(text=f"Score: {score}   |   High Score: {highscore}")
    lbl_result.config(text="Scores reset! Play again!", fg="blue")
    lbl_player_choice.config(image="")
    lbl_com_choice.config(image="")

#  GUI Layout 
lbl_title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24, "bold"), fg="white", bg="#282c34")
lbl_title.pack(pady=10)

lbl_score = tk.Label(root, text=f"Score: {score}   |   High Score: {highscore}", font=("Arial", 14), fg="lightblue", bg="#282c34")
lbl_score.pack(pady=5)

frame_choices = tk.Frame(root, bg="#282c34")
frame_choices.pack(pady=20)

# Player and Computer labels
lbl_player_title = tk.Label(frame_choices, text="You", font=("Arial", 16), fg="white", bg="#282c34")
lbl_player_title.grid(row=0, column=0, padx=50)
lbl_com_title = tk.Label(frame_choices, text="Computer", font=("Arial", 16), fg="white", bg="#282c34")
lbl_com_title.grid(row=0, column=1, padx=50)

lbl_player_choice = tk.Label(frame_choices, bg="#282c34")
lbl_player_choice.grid(row=1, column=0, padx=20, pady=10)
lbl_com_choice = tk.Label(frame_choices, bg="#282c34")
lbl_com_choice.grid(row=1, column=1, padx=20, pady=10)

lbl_result = tk.Label(root, text="Choose your move!", font=("Arial", 18, "bold"), bg="#282c34", fg="yellow")
lbl_result.pack(pady=10)

# Buttons
frame_buttons = tk.Frame(root, bg="#282c34")
frame_buttons.pack(pady=20)

btn_rock = tk.Button(frame_buttons, image=images["Rock"], command=lambda: play("Rock"), bd=0, bg="#282c34", activebackground="#282c34")
btn_paper = tk.Button(frame_buttons, image=images["Paper"], command=lambda: play("Paper"), bd=0, bg="#282c34", activebackground="#282c34")
btn_scissors = tk.Button(frame_buttons, image=images["Scissors"], command=lambda: play("Scissors"), bd=0, bg="#282c34", activebackground="#282c34")

btn_rock.grid(row=0, column=0, padx=20)
btn_paper.grid(row=0, column=1, padx=20)
btn_scissors.grid(row=0, column=2, padx=20)

btn_reset = tk.Button(root, text="🔄 Reset Score", font=("Arial", 12, "bold"), command=reset_score, bg="red", fg="white", relief="raised", bd=3)
btn_reset.pack(pady=15)

root.mainloop()

