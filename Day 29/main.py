from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
# ------------------- Read Data ----------------------------------------
try:
    data=pandas.read_csv("Day 29\data\words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("Day 29\data\French_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

# -------------------- Functions ---------------------------------------
def generate_new_random_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=front_image)
    flip_timer=window.after(3000,func=flip)

def flip():
    canvas.itemconfig(card_background,image=back_image)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")


def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("Day 29\data\words_to_learn.csv",index=False)
    generate_new_random_word()

# -------------------- UI SETUP ----------------------------------------
window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip)
front_image=PhotoImage(file="Day 29\images\card_front.png")
back_image=PhotoImage(file="Day 29\images\card_back.png")
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_background=canvas.create_image(400,263,image=front_image)
card_title=canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Arial",60,"bold"),tags=("French"))
canvas.grid(column=0,row=0,columnspan=2)

# ----------------- Wrong Logo ---------------------
wrong_logo=PhotoImage(file="Day 29\images\wrong.png")
wrong=Button(image=wrong_logo,highlightthickness=0,command=generate_new_random_word)
wrong.grid(column=0,row=1)

# ----------------- Right Logo ---------------------
right_logo=PhotoImage(file="Day 29\images\Right.png")
right=Button(image=right_logo,command=is_known)
right.grid(row=1,column=1)





generate_new_random_word()
window.mainloop()