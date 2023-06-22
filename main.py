
import turtle
import pandas
import string
from show_state import ShowState
game_is_on = True

### Setting up Game Screen

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=800, height=600)
turtle.shape(image)

### Reading CSV

data = pandas.read_csv("50_states.csv")

states = data["state"]
old_list = states.to_list()
states_list = []

for state in old_list:
    states_list.append(state.lower())

print(states_list)

show_state = ShowState()

### Guessing
states_correct = 0
def guess():

    global states_correct
    global data

    if states_correct == 0:
        title_name = "Guess The State Bud"
    else:
        title_name = f"{states_correct}/50 States Correct"

    answer_state = screen.textinput(title=title_name, prompt="Your Guess :")
    lower_answer = answer_state.lower()

    if lower_answer in states_list:
        states_correct += 1
        states_list.remove(lower_answer)

        cap_answer = string.capwords(lower_answer)
        x_cor = int(data[data["state"] == cap_answer].x)
        y_cor = int(data[data["state"] == cap_answer].y)

        show_state.update_state(cap_answer, x_cor, y_cor)


### While Game is on

while game_is_on:
    guess()


turtle.mainloop()

