import turtle
import pandas
from states import State

screen=turtle.Screen()
screen.title("Indian States Game")
image="india.gif"
screen.addshape(image)
screen.setup(width=750,height=770)
turtle.shape(image)


# def get_mouse_click(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click)
i=1
while i<30:
    answer_state=screen.textinput(title="Guess the State?" ,prompt="Enter the next state")
    data=pandas.read_csv("indian_states.csv")
    states=data["states"].to_dict()
    for j in range(29):
        if(states[j]==answer_state):
            guess_state=data[data["states"]==answer_state]["states"]
            x=data[data["states"]==answer_state]["x"]
            y=data[data["states"]==answer_state]["y"]
            datas=[]
            datas.append(guess_state.to_list())
            datas.append(x.to_list())
            datas.append(y.to_list())
            tim=State(datas[1][0],datas[2][0],answer_state)
            i+=1
        else:
            continue

turtle.mainloop()
